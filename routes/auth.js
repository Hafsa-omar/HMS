const express = require('express');
const bcrypt  = require('bcrypt');
const router  = express.Router();

module.exports = (db) => {

    // Register new patient
    router.post('/register', async (req, res) => {
        const { fname, lname, address, nic, dob, email, password } = req.body;
        const fullName = `${fname} ${lname}`;
        db.query("SELECT * FROM webuser WHERE email = ?", [email], async (err, rows) => {
            if (err) return res.send("<script>alert('Server error'); window.location='/register';</script>");
            if (rows.length > 0) return res.send("<script>alert('Email already registered!'); window.location='/register';</script>");
            const hashed = await bcrypt.hash(password, 10);
            db.query(
                "INSERT INTO patient (pname, paddress, pnic, pdob, pemail, ppassword) VALUES (?, ?, ?, ?, ?, ?)",
                [fullName, address, nic, dob, email, hashed],
                (err) => {
                    if (err) return res.send("<script>alert('Registration error. Please try again.'); window.location='/register';</script>");
                    db.query("INSERT INTO webuser (email, usertype) VALUES (?, 'p')", [email]);
                    res.redirect('/login');
                }
            );
        });
    });

    // Login — checks usertype then redirects to the right dashboard
    router.post('/login', (req, res) => {
        const { email, password } = req.body;
        db.query("SELECT * FROM webuser WHERE email = ?", [email], (err, users) => {
            if (err || users.length === 0) {
                return res.send("<script>alert('No account found for this email.'); window.location='/login';</script>");
            }
            const usertype = users[0].usertype;

            if (usertype === 'p') {
                db.query("SELECT * FROM patient WHERE pemail = ?", [email], async (err, rows) => {
                    if (err || !rows || rows.length === 0) {
                        return res.send("<script>alert('Account not set up properly.'); window.location='/register';</script>");
                    }
                    const match = await bcrypt.compare(password, rows[0].ppassword);
                    if (!match) return res.send("<script>alert('Wrong password! Please try again.'); window.location='/login';</script>");
                    req.session.user = { pid: rows[0].pid, name: rows[0].pname, email, usertype: 'p' };
                    res.redirect('/dashboard');
                });
            } else if (usertype === 'd') {
                db.query("SELECT * FROM doctor WHERE docemail = ?", [email], async (err, results) => {
                    if (err || !results || results.length === 0) {
                        return res.send("<script>alert('Doctor account not found.'); window.location='/login';</script>");
                    }
                    const match = await bcrypt.compare(password, results[0].docpassword);
                    if (!match) return res.send("<script>alert('Wrong password!'); window.location='/login';</script>");
                    req.session.user = { pid: results[0].docid, name: results[0].docname, email, usertype: 'd' };
                    res.redirect('/doctor');
                });
            } else if (usertype === 'a') {
                db.query("SELECT * FROM admin WHERE aemail = ?", [email], async (err, results) => {
                    if (err || !results || results.length === 0) {
                        return res.send("<script>alert('Admin account not found.'); window.location='/login';</script>");
                    }
                    const match = await bcrypt.compare(password, results[0].apassword);
                    if (!match) return res.send("<script>alert('Wrong password!'); window.location='/login';</script>");
                    req.session.user = { pid: 0, name: 'Admin', email, usertype: 'a' };
                    res.redirect('/admin');
                });
            }
        });
    });

    // Logout
    router.get('/logout', (req, res) => {
        req.session.destroy();
        res.redirect('/');
    });

    return router;
};
