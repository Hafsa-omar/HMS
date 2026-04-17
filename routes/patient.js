const express = require('express');
const bcrypt  = require('bcrypt');
const router  = express.Router();

module.exports = (db, requireLogin) => {

    router.get('/me', requireLogin, (req, res) => {
        res.json({
            pid:      req.session.user.pid,
            name:     req.session.user.name,
            email:    req.session.user.email,
            usertype: req.session.user.usertype
        });
    });

    router.get('/specialties', (req, res) => {
        db.query("SELECT * FROM specialties ORDER BY sname ASC", (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results);
        });
    });

    router.get('/doctors', (req, res) => {
        db.query(
            `SELECT d.docid, d.docname, d.docemail, d.doctel, d.docnic,
                    d.country, d.city, d.hospital_branch, d.available, s.sname
             FROM doctor d LEFT JOIN specialties s ON d.specialties = s.id
             ORDER BY d.docname ASC`,
            (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.get('/doctors/specialty/:specId', (req, res) => {
        const { country, city, type } = req.query;
        let sql = `SELECT d.docid, d.docname, d.country, d.city, d.hospital_branch,
                          d.available, d.hospital_type, d.consultation_fee, d.rating, d.review_count, s.sname
                   FROM doctor d LEFT JOIN specialties s ON d.specialties = s.id
                   WHERE d.specialties = ?`;
        const params = [req.params.specId];
        if (country) { sql += ' AND d.country = ?';        params.push(country); }
        if (city)    { sql += ' AND d.city = ?';           params.push(city); }
        if (type)    { sql += ' AND d.hospital_type = ?';  params.push(type); }
        sql += ' ORDER BY d.available DESC, d.rating DESC';
        db.query(sql, params, (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results);
        });
    });

    router.get('/doctor/reviews/:docid', (req, res) => {
        db.query(
            `SELECT r.rating, r.review_text, r.created_at, p.pname
             FROM doctor_review r JOIN patient p ON r.pid = p.pid
             WHERE r.docid = ? ORDER BY r.created_at DESC LIMIT 10`,
            [req.params.docid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.post('/doctor/review', requireLogin, (req, res) => {
        const pid = req.session.user.pid;
        const { docid, rating, review_text } = req.body;
        db.query('INSERT INTO doctor_review (pid,docid,rating,review_text) VALUES (?,?,?,?)',
            [pid, docid, rating, review_text], (err) => {
                if (err) return res.status(500).json({ error: err.message });
                db.query(
                    `UPDATE doctor SET
                       rating=(SELECT ROUND(AVG(rating),1) FROM doctor_review WHERE docid=?),
                       review_count=(SELECT COUNT(*) FROM doctor_review WHERE docid=?)
                     WHERE docid=?`,
                    [docid, docid, docid]
                );
                res.json({ success: true });
            }
        );
    });

    router.get('/health-sharing', requireLogin, (req, res) => {
        db.query('SELECT docid FROM health_sharing WHERE pid=?', [req.session.user.pid], (err, r) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(r.map(x => x.docid));
        });
    });

    router.post('/health-sharing/toggle', requireLogin, (req, res) => {
        const pid = req.session.user.pid;
        const { docid } = req.body;
        db.query('SELECT id FROM health_sharing WHERE pid=? AND docid=?', [pid, docid], (err, rows) => {
            if (err) return res.status(500).json({ error: err.message });
            if (rows.length > 0) {
                db.query('DELETE FROM health_sharing WHERE pid=? AND docid=?', [pid, docid], () => res.json({ shared: false }));
            } else {
                db.query('INSERT INTO health_sharing (pid,docid) VALUES (?,?)', [pid, docid], () => res.json({ shared: true }));
            }
        });
    });

    router.get('/appointments', requireLogin, (req, res) => {
        const pid = req.session.user.pid;
        db.query(
            `SELECT a.appoid, a.appodate, a.status, a.apponum, d.docname, s.sname
             FROM appointment a
             JOIN doctor d ON a.scheduleid = d.docid
             LEFT JOIN specialties s ON d.specialties = s.id
             WHERE a.pid = ? ORDER BY a.appodate ASC`,
            [pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    router.get('/appointments/filter', requireLogin, (req, res) => {
        const pid = req.session.user.pid;
        const { date } = req.query;
        let sql = `SELECT a.appoid, a.appodate, a.status, a.apponum, d.docname, s.sname
                   FROM appointment a
                   JOIN doctor d ON a.scheduleid = d.docid
                   LEFT JOIN specialties s ON d.specialties = s.id
                   WHERE a.pid = ?`;
        const params = [pid];
        if (date) { sql += ' AND a.appodate = ?'; params.push(date); }
        sql += ' ORDER BY a.appodate ASC';
        db.query(sql, params, (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results);
        });
    });

    router.post('/book', requireLogin, (req, res) => {
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

    router.post('/appointments/cancel/:appoid', requireLogin, (req, res) => {
        db.query(
            "UPDATE appointment SET status = 'CANCELLED' WHERE appoid = ? AND pid = ?",
            [req.params.appoid, req.session.user.pid],
            (err) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json({ success: true });
            }
        );
    });

    router.get('/patient/profile', requireLogin, (req, res) => {
        db.query("SELECT * FROM patient WHERE pid = ?", [req.session.user.pid], (err, results) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(results[0]);
        });
    });

    router.post('/patient/update', requireLogin, async (req, res) => {
        const pid = req.session.user.pid;
        const { pname, paddress, ptel, password } = req.body;
        let sql = "UPDATE patient SET pname=?, paddress=?, ptel=? WHERE pid=?";
        let params = [pname, paddress, ptel, pid];
        if (password && password.length > 0) {
            const hashed = await bcrypt.hash(password, 10);
            sql = "UPDATE patient SET pname=?, paddress=?, ptel=?, ppassword=? WHERE pid=?";
            params = [pname, paddress, ptel, hashed, pid];
        }
        db.query(sql, params, (err) => {
            if (err) return res.status(500).json({ error: err.message });
            req.session.user.name = pname;
            res.json({ success: true });
        });
    });

    router.post('/patient/delete', requireLogin, (req, res) => {
        const pid   = req.session.user.pid;
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

    router.get('/health-record', requireLogin, (req, res) => {
        const user = req.session.user;
        const pid  = (user.usertype === 'd' && req.query.pid) ? req.query.pid : user.pid;

        Promise.all([
            new Promise((resolve, reject) =>
                db.query('SELECT * FROM patient WHERE pid = ?', [pid], (e, r) => e ? reject(e) : resolve(r[0]))
            ),
            new Promise((resolve, reject) =>
                db.query(
                    `SELECT a.appoid, a.appodate, a.status, d.docname, d.country, d.city, s.sname
                     FROM appointment a
                     JOIN doctor d ON a.scheduleid = d.docid
                     LEFT JOIN specialties s ON d.specialties = s.id
                     WHERE a.pid = ? ORDER BY a.appodate DESC`,
                    [pid], (e, r) => e ? reject(e) : resolve(r)
                )
            ),
            new Promise((resolve, reject) =>
                db.query(
                    `SELECT r.*, d.docname FROM lab_result r
                     LEFT JOIN doctor d ON r.docid = d.docid
                     WHERE r.pid = ? ORDER BY r.created_at DESC`,
                    [pid], (e, r) => e ? reject(e) : resolve(r)
                )
            )
        ])
        .then(([profile, appointments, labResults]) => res.json({ profile, appointments, labResults }))
        .catch(err => res.status(500).json({ error: err.message }));
    });

    router.get('/results', requireLogin, (req, res) => {
        db.query(
            `SELECT r.*, d.docname FROM lab_result r
             LEFT JOIN doctor d ON r.docid = d.docid
             WHERE r.pid = ? ORDER BY r.created_at DESC`,
            [req.session.user.pid], (err, results) => {
                if (err) return res.status(500).json({ error: err.message });
                res.json(results);
            }
        );
    });

    return router;
};
