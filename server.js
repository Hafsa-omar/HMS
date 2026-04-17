require('dotenv').config();
const express = require('express');
const mysql = require('mysql2');
const path = require('path');
const session = require('express-session');
const app = express();

// Middleware setup
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Session config — keeps user logged in for 24 hours
app.use(session({
    secret: 'hms-secret-key-2026',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 24 * 60 * 60 * 1000 }
}));

// Database connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'hms123',
    database: 'hospital_management',
    port: 3306
});

db.connect((err) => {
    if (err) { console.error('DB Error: ' + err.message); return; }
    console.log('✅ Database connected!');
});

// Blocks pages from loading if user is not logged in
function requireLogin(req, res, next) {
    if (!req.session.user) return res.redirect('/login');
    next();
}

// =====================
// PAGE ROUTES
// =====================

// Public pages
app.get('/', (req, res) => {
    if (req.session.user) {
        const t = req.session.user.usertype;
        if (t === 'd') return res.redirect('/doctor');
        if (t === 'a') return res.redirect('/admin');
        return res.redirect('/dashboard');
    }
    res.sendFile(path.join(__dirname, 'public/pages/index.html'));
});
app.get('/login', (req, res) => res.sendFile(path.join(__dirname, 'public/pages/login.html')));
app.get('/register', (req, res) => res.sendFile(path.join(__dirname, 'public/pages/register.html')));

// Patient pages
app.get('/dashboard', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/dashboard.html')));
app.get('/book', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/book.html')));
app.get('/doctors', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/doctors.html')));
app.get('/mybookings', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/mybookings.html')));
app.get('/results', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/results.html')));
app.get('/healthrecord', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/healthrecord.html')));
app.get('/settings', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/settings.html')));

// Doctor pages
app.get('/doctor', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/doctor.html')));
app.get('/mypatients', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/mypatients.html')));
app.get('/addresult', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/addresult.html')));
app.get('/doctorsettings', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/doctorsettings.html')));

// Admin page
app.get('/admin', requireLogin, (req, res) => res.sendFile(path.join(__dirname, 'public/pages/admin.html')));

// =====================
// PATIENT APIs
// =====================

// Returns current logged-in user info
app.get('/api/me', requireLogin, (req, res) => {
    res.json({
        pid: req.session.user.pid,
        name: req.session.user.name,
        email: req.session.user.email,
        usertype: req.session.user.usertype
    });
});

// Get all specialties for booking/filtering
app.get('/api/specialties', (req, res) => {
    db.query("SELECT * FROM specialties ORDER BY sname ASC", (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Get all doctors with their specialty
app.get('/api/doctors', (req, res) => {
    db.query(`SELECT d.docid, d.docname, d.docemail, d.doctel, d.docnic,
                     d.country, d.city, d.hospital_branch, d.available, s.sname
              FROM doctor d
              LEFT JOIN specialties s ON d.specialties = s.id
              ORDER BY d.docname ASC`,
    (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Get doctors filtered by specialty, country, city, or type
app.get('/api/doctors/specialty/:specId', (req, res) => {
    const { country, city, type } = req.query;
    let sql = `SELECT d.docid, d.docname, d.country, d.city, d.hospital_branch,
                      d.available, d.hospital_type, d.consultation_fee, d.rating, d.review_count,
                      s.sname
               FROM doctor d LEFT JOIN specialties s ON d.specialties = s.id
               WHERE d.specialties = ?`;
    const params = [req.params.specId];
    if (country) { sql += ' AND d.country = ?'; params.push(country); }
    if (city)    { sql += ' AND d.city = ?';    params.push(city); }
    if (type)    { sql += ' AND d.hospital_type = ?'; params.push(type); }
    sql += ' ORDER BY d.available DESC, d.rating DESC';
    db.query(sql, params, (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Get reviews for a specific doctor
app.get('/api/doctor/reviews/:docid', (req, res) => {
    db.query(`SELECT r.rating, r.review_text, r.created_at, p.pname
              FROM doctor_review r JOIN patient p ON r.pid = p.pid
              WHERE r.docid = ? ORDER BY r.created_at DESC LIMIT 10`,
        [req.params.docid], (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results);
        });
});

// Patient submits a review for a doctor
app.post('/api/doctor/review', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const { docid, rating, review_text } = req.body;
    db.query('INSERT INTO doctor_review (pid,docid,rating,review_text) VALUES (?,?,?,?)',
        [pid, docid, rating, review_text], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            // Update doctor's average rating after new review
            db.query(`UPDATE doctor SET rating=ROUND((SELECT AVG(rating) FROM doctor_review WHERE docid=?),1),
                      review_count=(SELECT COUNT(*) FROM doctor_review WHERE docid=?) WHERE docid=?`,
                [docid, docid, docid]);
            res.json({ success: true });
        });
});

// Get list of doctors the patient is sharing health data with
app.get('/api/health-sharing', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    db.query('SELECT docid FROM health_sharing WHERE pid=?', [pid], (err, r) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(r.map(x => x.docid));
    });
});

// Toggle health sharing on/off for a doctor
app.post('/api/health-sharing/toggle', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const { docid } = req.body;
    db.query('SELECT id FROM health_sharing WHERE pid=? AND docid=?', [pid, docid], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        if (rows.length > 0) {
            db.query('DELETE FROM health_sharing WHERE pid=? AND docid=?', [pid, docid],
                () => res.json({ shared: false }));
        } else {
            db.query('INSERT INTO health_sharing (pid,docid) VALUES (?,?)', [pid, docid],
                () => res.json({ shared: true }));
        }
    });
});

// Get all appointments for the logged-in patient
app.get('/api/appointments', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const sql = `
        SELECT a.appoid, a.appodate, a.status, a.apponum,
               d.docname, s.sname
        FROM appointment a
        JOIN doctor d ON a.scheduleid = d.docid
        LEFT JOIN specialties s ON d.specialties = s.id
        WHERE a.pid = ?
        ORDER BY a.appodate ASC
    `;
    db.query(sql, [pid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Get appointments filtered by date
app.get('/api/appointments/filter', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const { date } = req.query;
    let sql = `
        SELECT a.appoid, a.appodate, a.status, a.apponum,
               d.docname, s.sname
        FROM appointment a
        JOIN doctor d ON a.scheduleid = d.docid
        LEFT JOIN specialties s ON d.specialties = s.id
        WHERE a.pid = ?
    `;
    const params = [pid];
    if (date) { sql += " AND a.appodate = ?"; params.push(date); }
    sql += " ORDER BY a.appodate ASC";
    db.query(sql, params, (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Patient books a new appointment
app.post('/api/book', requireLogin, (req, res) => {
    const { docid, appodate } = req.body;
    const pid = req.session.user.pid;
    db.query(
        "INSERT INTO appointment (pid, scheduleid, apponum, appodate, status) VALUES (?, ?, 1, ?, 'BOOKED')",
        [pid, docid, appodate],
        (err, result) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true, appointmentId: result.insertId });
        }
    );
});

// Patient cancels their appointment
app.post('/api/appointments/cancel/:appoid', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    db.query(
        "UPDATE appointment SET status = 'CANCELLED' WHERE appoid = ? AND pid = ?",
        [req.params.appoid, pid],
        (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        }
    );
});

// Get patient's own profile info
app.get('/api/patient/profile', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    db.query("SELECT * FROM patient WHERE pid = ?", [pid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results[0]);
    });
});

// Patient updates their name, phone, address, or password
app.post('/api/patient/update', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const { pname, paddress, ptel, password } = req.body;
    let sql = "UPDATE patient SET pname=?, paddress=?, ptel=? WHERE pid=?";
    let params = [pname, paddress, ptel, pid];
    if (password && password.length > 0) {
        sql = "UPDATE patient SET pname=?, paddress=?, ptel=?, ppassword=? WHERE pid=?";
        params = [pname, paddress, ptel, password, pid];
    }
    db.query(sql, params, (err) => {
        if (err) return res.status(500).json({ error: err.message });
        req.session.user.name = pname;
        res.json({ success: true });
    });
});

// Patient deletes their own account
app.post('/api/patient/delete', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const email = req.session.user.email;
    db.query("DELETE FROM appointment WHERE pid = ?", [pid], () => {
        db.query("DELETE FROM patient WHERE pid = ?", [pid], () => {
            db.query("DELETE FROM webuser WHERE email = ?", [email], () => {
                req.session.destroy();
                res.json({ success: true });
            });
        });
    });
});

// Admin deletes a specific appointment
app.post('/api/admin/appointments/delete/:appoid', requireLogin, (req, res) => {
    db.query("DELETE FROM appointment WHERE appoid = ?", [req.params.appoid], (err) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ success: true });
    });
});

// Full health record — patient sees own, doctor passes ?pid= to view a patient
app.get('/api/health-record', requireLogin, (req, res) => {
    const user = req.session.user;
    const pid  = (user.usertype === 'd' && req.query.pid) ? req.query.pid : user.pid;

    const profile = new Promise((resolve, reject) =>
        db.query('SELECT * FROM patient WHERE pid = ?', [pid], (e, r) => e ? reject(e) : resolve(r[0]))
    );
    const appointments = new Promise((resolve, reject) =>
        db.query(`SELECT a.appoid, a.appodate, a.status, d.docname, d.country, d.city, s.sname
                  FROM appointment a
                  JOIN doctor d ON a.scheduleid = d.docid
                  LEFT JOIN specialties s ON d.specialties = s.id
                  WHERE a.pid = ? ORDER BY a.appodate DESC`, [pid], (e, r) => e ? reject(e) : resolve(r))
    );
    const labResults = new Promise((resolve, reject) =>
        db.query(`SELECT r.*, d.docname
                  FROM lab_result r LEFT JOIN doctor d ON r.docid = d.docid
                  WHERE r.pid = ? ORDER BY r.created_at DESC`, [pid], (e, r) => e ? reject(e) : resolve(r))
    );

    Promise.all([profile, appointments, labResults])
        .then(([p, a, l]) => res.json({ profile: p, appointments: a, labResults: l }))
        .catch(err => res.status(500).json({ error: err.message }));
});

// =====================
// DOCTOR APIs
// =====================

// Get logged-in doctor's own profile
app.get('/api/doctor/me', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    db.query(`SELECT d.*, s.sname FROM doctor d
              LEFT JOIN specialties s ON d.specialties = s.id
              WHERE d.docid = ?`, [docid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results[0]);
    });
});

// Get all appointments assigned to this doctor
app.get('/api/doctor/appointments', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    const sql = `
        SELECT a.appoid, a.appodate, a.status, a.apponum,
               p.pname, p.ptel, p.pemail, p.pid
        FROM appointment a
        JOIN patient p ON a.pid = p.pid
        WHERE a.scheduleid = ?
        ORDER BY a.appodate ASC
    `;
    db.query(sql, [docid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Doctor updates appointment status (e.g. CHECKED_IN, COMPLETED)
app.post('/api/doctor/appointments/update', requireLogin, (req, res) => {
    const { appoid, status } = req.body;
    db.query("UPDATE appointment SET status = ? WHERE appoid = ?",
        [status, appoid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
});

// Get all patients who have booked with this doctor
app.get('/api/doctor/patients', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    const sql = `
        SELECT DISTINCT p.pid, p.pname, p.pemail, p.ptel, p.pnic, p.pdob, p.paddress,
               COUNT(a.appoid) as total_appointments
        FROM appointment a
        JOIN patient p ON a.pid = p.pid
        WHERE a.scheduleid = ? AND a.status != 'CANCELLED'
        GROUP BY p.pid
        ORDER BY p.pname ASC
    `;
    db.query(sql, [docid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Doctor updates their name, phone, or password
app.post('/api/doctor/update', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    const { docname, doctel, password } = req.body;
    let sql = "UPDATE doctor SET docname=?, doctel=? WHERE docid=?";
    let params = [docname, doctel, docid];
    if (password && password.length > 0) {
        sql = "UPDATE doctor SET docname=?, doctel=?, docpassword=? WHERE docid=?";
        params = [docname, doctel, password, docid];
    }
    db.query(sql, params, (err) => {
        if (err) return res.status(500).json({ error: err.message });
        req.session.user.name = docname;
        res.json({ success: true });
    });
});

// =====================
// LAB RESULTS APIs
// =====================

// Patient views their own lab results
app.get('/api/results', requireLogin, (req, res) => {
    const pid = req.session.user.pid;
    const sql = `
        SELECT r.*, d.docname
        FROM lab_result r
        LEFT JOIN doctor d ON r.docid = d.docid
        WHERE r.pid = ?
        ORDER BY r.created_at DESC
    `;
    db.query(sql, [pid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Doctor views all results they have added
app.get('/api/doctor/results', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    const sql = `
        SELECT r.*, p.pname
        FROM lab_result r
        JOIN patient p ON r.pid = p.pid
        WHERE r.docid = ?
        ORDER BY r.created_at DESC
    `;
    db.query(sql, [docid], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Doctor adds a new lab result for a patient
app.post('/api/doctor/results/add', requireLogin, (req, res) => {
    const docid = req.session.user.pid;
    const { pid, test_name, result, notes } = req.body;
    db.query(
        "INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES (?, ?, ?, ?, ?, NOW())",
        [pid, docid, test_name, result, notes],
        (err, r) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true, id: r.insertId });
        }
    );
});

// =====================
// ADMIN APIs
// =====================

// Admin gets list of all patients
app.get('/api/admin/patients', requireLogin, (req, res) => {
    db.query("SELECT pid, pname, pemail, ptel, paddress, pdob FROM patient ORDER BY pname ASC",
        (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results);
        });
});

// Admin gets all appointments across the system
app.get('/api/admin/appointments', requireLogin, (req, res) => {
    const sql = `
        SELECT a.appoid, a.appodate, a.status,
               p.pname, d.docname, s.sname
        FROM appointment a
        JOIN patient p ON a.pid = p.pid
        JOIN doctor d ON a.scheduleid = d.docid
        LEFT JOIN specialties s ON d.specialties = s.id
        ORDER BY a.appodate DESC
    `;
    db.query(sql, (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(results);
    });
});

// Admin adds a new doctor
app.post('/api/admin/doctors/add', requireLogin, (req, res) => {
    const { docname, docemail, docpassword, doctel, docnic, specialties } = req.body;
    db.query(
        "INSERT INTO doctor (docname, docemail, docpassword, doctel, docnic, specialties) VALUES (?, ?, ?, ?, ?, ?)",
        [docname, docemail, docpassword, doctel, docnic, specialties],
        (err, result) => {
            if (err) return res.status(500).json({ error: err.message });
            db.query("INSERT IGNORE INTO webuser (email, usertype) VALUES (?, 'd')", [docemail]);
            res.json({ success: true, docid: result.insertId });
        }
    );
});

// Admin deletes a doctor
app.post('/api/admin/doctors/delete/:docid', requireLogin, (req, res) => {
    db.query("DELETE FROM doctor WHERE docid = ?", [req.params.docid], (err) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ success: true });
    });
});

// Admin deletes a patient
app.post('/api/admin/patients/delete/:pid', requireLogin, (req, res) => {
    db.query("DELETE FROM patient WHERE pid = ?", [req.params.pid], (err) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ success: true });
    });
});

// Admin cancels any appointment
app.post('/api/admin/appointments/cancel/:appoid', requireLogin, (req, res) => {
    db.query("UPDATE appointment SET status = 'CANCELLED' WHERE appoid = ?",
        [req.params.appoid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
});

// =====================
// AUTH ROUTES
// =====================

// New patient registers an account
app.post('/auth/register', (req, res) => {
    const { fname, lname, address, nic, dob, email, password } = req.body;
    const fullName = `${fname} ${lname}`;
    db.query("SELECT * FROM webuser WHERE email = ?", [email], (err, rows) => {
        if (err) return res.send("<script>alert('Server error'); window.location='/register';</script>");
        if (rows.length > 0) {
            return res.send("<script>alert('Email already registered!'); window.location='/register';</script>");
        }
        db.query(
            "INSERT INTO patient (pname, paddress, pnic, pdob, pemail, ppassword) VALUES (?, ?, ?, ?, ?, ?)",
            [fullName, address, nic, dob, email, password],
            (err, result) => {
                if (err) return res.send("<script>alert('Error: " + err.message + "'); window.location='/register';</script>");
                db.query("INSERT INTO webuser (email, usertype) VALUES (?, 'p')", [email]);
                res.redirect('/login');
            }
        );
    });
});

// Login — checks usertype then redirects to the right dashboard
app.post('/auth/login', (req, res) => {
    const { email, password } = req.body;
    db.query("SELECT * FROM webuser WHERE email = ?", [email], (err, users) => {
        if (err || users.length === 0) {
            return res.send("<script>alert('No account found for this email.'); window.location='/login';</script>");
        }
        const usertype = users[0].usertype;
        if (usertype === 'p') {
            db.query("SELECT * FROM patient WHERE pemail = ?", [email], (err, rows) => {
                if (err || !rows || rows.length === 0) {
                    return res.send("<script>alert('Account not set up properly. Please register again.'); window.location='/register';</script>");
                }
                if (rows[0].ppassword !== password) {
                    return res.send("<script>alert('Wrong password! Please try again.'); window.location='/login';</script>");
                }
                req.session.user = {
                    pid: rows[0].pid,
                    name: rows[0].pname,
                    email: email,
                    usertype: 'p'
                };
                res.redirect('/dashboard');
            });
        } else if (usertype === 'd') {
            db.query("SELECT * FROM doctor WHERE docemail = ? AND docpassword = ?",
                [email, password], (err, results) => {
                    if (results && results.length > 0) {
                        req.session.user = {
                            pid: results[0].docid,
                            name: results[0].docname,
                            email: email,
                            usertype: 'd'
                        };
                        res.redirect('/doctor');
                    } else {
                        res.send("<script>alert('Wrong password!'); window.location='/login';</script>");
                    }
                });
        } else if (usertype === 'a') {
            db.query("SELECT * FROM admin WHERE aemail = ? AND apassword = ?",
                [email, password], (err, results) => {
                    if (results && results.length > 0) {
                        req.session.user = {
                            pid: 0,
                            name: 'Admin',
                            email: email,
                            usertype: 'a'
                        };
                        res.redirect('/admin');
                    } else {
                        res.send("<script>alert('Wrong password!'); window.location='/login';</script>");
                    }
                });
        }
    });
});

// Logout — destroys session and sends back to home
app.get('/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/');
});

// =====================
// CHATBOT API
// =====================

// Rule-based chatbot
app.post('/api/chat', requireLogin, (req, res) => {
    const { message } = req.body;
    const user = req.session.user;
    const pid  = user.pid;
    const msg  = (message || '').toLowerCase().trim();

    // ── Greetings ──────────────────────────────────────────────────────────
    if (/^(hi|hello|hey|good morning|good afternoon|good evening|howdy|greetings)/.test(msg)) {
        return res.json({ reply: `Hello ${user.name}! 👋 How can I help you today?\n\nYou can ask me about:\n• Your appointments\n• Available doctors\n• Your lab results\n• How to book or cancel an appointment` });
    }

    // ── Appointments ───────────────────────────────────────────────────────
    if (/appointment|booking|schedule|booked/.test(msg)) {
        db.query(
            `SELECT a.appoid, a.appodate, a.status, d.docname, s.sname AS specialty
             FROM appointment a
             JOIN doctor d ON a.scheduleid = d.docid
             LEFT JOIN specialties s ON d.specialties = s.id
             WHERE a.pid = ? ORDER BY a.appodate DESC LIMIT 5`,
            [pid], (err, rows) => {
                if (err || !rows.length) return res.json({ reply: 'You have no appointments yet. Visit the Book page to schedule one!' });
                let reply = `📅 Your recent appointments:\n\n`;
                rows.forEach(r => {
                    reply += `• ${r.appodate?.toString().slice(0,10)} — Dr. ${r.docname} (${r.specialty || 'General'})\n  Status: ${r.status}\n\n`;
                });
                reply += 'To book a new appointment, go to the Book page. To cancel, visit My Bookings.';
                res.json({ reply });
            }
        );
        return;
    }

    // ── Doctors ────────────────────────────────────────────────────────────
    if (/doctor|specialist|physician|find.*doc|available doc/.test(msg)) {
        db.query(
            `SELECT d.docname, d.country, d.city, d.consultation_fee, d.rating, s.sname AS specialty
             FROM doctor d LEFT JOIN specialties s ON d.specialties = s.id
             WHERE d.available = 1 ORDER BY d.rating DESC LIMIT 6`,
            (err, rows) => {
                if (err || !rows.length) return res.json({ reply: 'No doctors available at the moment.' });
                let reply = `👨‍⚕️ Top available doctors:\n\n`;
                rows.forEach(r => {
                    reply += `• Dr. ${r.docname} — ${r.specialty || 'General'}\n  ${r.city}, ${r.country} | ⭐ ${r.rating} | $${r.consultation_fee}\n\n`;
                });
                reply += 'Visit the Doctors page to see all available doctors and book an appointment.';
                res.json({ reply });
            }
        );
        return;
    }

    // ── Lab results ────────────────────────────────────────────────────────
    if (/lab|result|test|blood|report/.test(msg)) {
        db.query(
            `SELECT r.test_name, r.result, r.created_at, d.docname
             FROM lab_result r LEFT JOIN doctor d ON r.docid = d.docid
             WHERE r.pid = ? ORDER BY r.created_at DESC LIMIT 5`,
            [pid], (err, rows) => {
                if (err || !rows.length) return res.json({ reply: 'No lab results found on your record yet.' });
                let reply = `🧪 Your recent lab results:\n\n`;
                rows.forEach(r => {
                    reply += `• ${r.test_name}: ${r.result}\n  Added by Dr. ${r.docname} on ${r.created_at?.toString().slice(0,10)}\n\n`;
                });
                reply += 'Visit the Results page for full details and notes.';
                res.json({ reply });
            }
        );
        return;
    }

    // ── Booking help ───────────────────────────────────────────────────────
    if (/how.*book|book.*how|make.*appointment|create.*appointment/.test(msg)) {
        return res.json({ reply: `To book an appointment:\n\n1. Click "Book Appointment" in the menu\n2. Choose a medical specialty\n3. Select a doctor\n4. Pick a date\n5. Confirm your booking\n\nYou can also view and manage your bookings under "My Bookings".` });
    }

    // ── Cancel help ────────────────────────────────────────────────────────
    if (/cancel|cancell/.test(msg)) {
        return res.json({ reply: `To cancel an appointment:\n\n1. Go to "My Bookings" in the menu\n2. Find the appointment you want to cancel\n3. Click the Cancel button next to it\n\nOnly BOOKED appointments can be cancelled.` });
    }

    // ── Health record ──────────────────────────────────────────────────────
    if (/health record|medical record|my record|health history/.test(msg)) {
        return res.json({ reply: `Your health record is available under the "Health Record" section in the menu. It includes:\n\n• All past and upcoming appointments\n• Lab test results\n• Doctor notes\n\nYou can also control which doctors can view your record under Settings → Health Sharing.` });
    }

    // ── Settings / profile ─────────────────────────────────────────────────
    if (/setting|profile|update|password|phone|address/.test(msg)) {
        return res.json({ reply: `You can update your profile details under the Settings page:\n\n• Change your name\n• Update phone number\n• Update address\n• Change password\n\nClick "Settings" in the navigation menu to get there.` });
    }

    // ── Emergency ──────────────────────────────────────────────────────────
    if (/emergency|urgent|critical|911|ambulance/.test(msg)) {
        return res.json({ reply: `🚨 For emergencies, please call your local emergency number immediately.\n\nDo not use this chat for medical emergencies. Go to the nearest emergency room or call an ambulance right away.` });
    }

    // ── Thanks ─────────────────────────────────────────────────────────────
    if (/thank|thanks|thank you|appreciate/.test(msg)) {
        return res.json({ reply: `You're welcome, ${user.name}! 😊 Feel free to ask if you need anything else.` });
    }

    // ── Default ────────────────────────────────────────────────────────────
    res.json({ reply: `I can help you with the following:\n\n• 📅 **Appointments** — view, book, or cancel\n• 👨‍⚕️ **Doctors** — find available doctors\n• 🧪 **Lab Results** — view your test results\n• 📋 **Health Record** — your full medical history\n• ⚙️ **Settings** — update your profile\n\nJust ask me about any of these!` });
});

// =====================
// START SERVER
// =====================
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`\n🏥 HMS running at: http://localhost:${PORT}\n`);
});
