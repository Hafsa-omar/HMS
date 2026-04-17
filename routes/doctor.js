const express = require('express');
const bcrypt  = require('bcrypt');
const router  = express.Router();

module.exports = (db, requireLogin) => {

    router.get('/me', requireLogin, (req, res) => {
        db.query(
            `SELECT d.*, s.sname FROM doctor d
             LEFT JOIN specialties s ON d.specialties = s.id
             WHERE d.docid = ?`,
            [req.session.user.pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results[0]);
            }
        );
    });

    router.get('/appointments', requireLogin, (req, res) => {
        db.query(
            `SELECT a.appoid, a.appodate, a.status, a.apponum,
                    p.pname, p.ptel, p.pemail, p.pid
             FROM appointment a JOIN patient p ON a.pid = p.pid
             WHERE a.scheduleid = ? ORDER BY a.appodate ASC`,
            [req.session.user.pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.post('/appointments/update', requireLogin, (req, res) => {
        const { appoid, status } = req.body;
        db.query("UPDATE appointment SET status = ? WHERE appoid = ?", [status, appoid], (err) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ success: true });
        });
    });

    router.get('/patients', requireLogin, (req, res) => {
        db.query(
            `SELECT DISTINCT p.pid, p.pname, p.pemail, p.ptel, p.pnic, p.pdob, p.paddress,
                    COUNT(a.appoid) as total_appointments
             FROM appointment a JOIN patient p ON a.pid = p.pid
             WHERE a.scheduleid = ? AND a.status != 'CANCELLED'
             GROUP BY p.pid ORDER BY p.pname ASC`,
            [req.session.user.pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.post('/update', requireLogin, async (req, res) => {
        const docid = req.session.user.pid;
        const { docname, doctel, password } = req.body;
        let sql = "UPDATE doctor SET docname=?, doctel=? WHERE docid=?";
        let params = [docname, doctel, docid];
        if (password && password.length > 0) {
            const hashed = await bcrypt.hash(password, 10);
            sql = "UPDATE doctor SET docname=?, doctel=?, docpassword=? WHERE docid=?";
            params = [docname, doctel, hashed, docid];
        }
        db.query(sql, params, (err) => {
            if (err) return res.status(500).json({ error: err.message });
            req.session.user.name = docname;
            res.json({ success: true });
        });
    });

    router.get('/results', requireLogin, (req, res) => {
        db.query(
            `SELECT r.*, p.pname FROM lab_result r
             JOIN patient p ON r.pid = p.pid
             WHERE r.docid = ? ORDER BY r.created_at DESC`,
            [req.session.user.pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.post('/results/add', requireLogin, (req, res) => {
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

    return router;
};
