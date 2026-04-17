const express = require('express');
const bcrypt  = require('bcrypt');
const router  = express.Router();

module.exports = (db, requireLogin) => {

    router.get('/patients', requireLogin, (req, res) => {
        db.query("SELECT pid, pname, pemail, ptel, paddress, pdob FROM patient ORDER BY pname ASC",
            (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.get('/appointments', requireLogin, (req, res) => {
        db.query(
            `SELECT a.appoid, a.appodate, a.status, p.pname, d.docname, s.sname
             FROM appointment a
             JOIN patient p ON a.pid = p.pid
             JOIN doctor d ON a.scheduleid = d.docid
             LEFT JOIN specialties s ON d.specialties = s.id
             ORDER BY a.appodate DESC`,
            (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.post('/doctors/add', requireLogin, async (req, res) => {
        const { docname, docemail, docpassword, doctel, docnic, specialties } = req.body;
        const hashed = await bcrypt.hash(docpassword, 10);
        db.query(
            "INSERT INTO doctor (docname, docemail, docpassword, doctel, docnic, specialties) VALUES (?, ?, ?, ?, ?, ?)",
            [docname, docemail, hashed, doctel, docnic, specialties],
            (err, result) => {
                if (err) return res.status(500).json({ error: err.message });
                db.query("INSERT IGNORE INTO webuser (email, usertype) VALUES (?, 'd')", [docemail]);
                res.json({ success: true, docid: result.insertId });
            }
        );
    });

    router.post('/doctors/delete/:docid', requireLogin, (req, res) => {
        db.query("DELETE FROM doctor WHERE docid = ?", [req.params.docid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
    });

    router.post('/patients/delete/:pid', requireLogin, (req, res) => {
        db.query("DELETE FROM patient WHERE pid = ?", [req.params.pid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
    });

    router.post('/appointments/cancel/:appoid', requireLogin, (req, res) => {
        db.query("UPDATE appointment SET status = 'CANCELLED' WHERE appoid = ?",
            [req.params.appoid], (err) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json({ success: true });
            }
        );
    });

    router.post('/appointments/delete/:appoid', requireLogin, (req, res) => {
        db.query("DELETE FROM appointment WHERE appoid = ?", [req.params.appoid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
    });

    return router;
};
