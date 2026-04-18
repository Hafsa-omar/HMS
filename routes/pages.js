const express = require('express');
const path    = require('path');
const router  = express.Router();

const P = (file) => path.join(__dirname, '..', 'public', 'pages', file);

module.exports = (requireLogin) => {

    router.get('/', (req, res) => {
        if (req.session.user) {
            const t = req.session.user.usertype;
            if (t === 'd') return res.redirect('/doctor');
            if (t === 'a') return res.redirect('/admin');
            return res.redirect('/dashboard');
        }
        res.sendFile(P('index.html'));
    });

    router.get('/login',    (req, res) => res.sendFile(P('login.html')));
    router.get('/register', (req, res) => res.sendFile(P('register.html')));

    // Patient pages
    router.get('/dashboard',   requireLogin, (req, res) => res.sendFile(P('dashboard.html')));
    router.get('/book',        requireLogin, (req, res) => res.sendFile(P('book.html')));
    router.get('/doctors',     requireLogin, (req, res) => res.sendFile(P('doctors.html')));
    router.get('/mybookings',  requireLogin, (req, res) => res.sendFile(P('mybookings.html')));
    router.get('/results',     requireLogin, (req, res) => res.sendFile(P('results.html')));
    router.get('/healthrecord',requireLogin, (req, res) => res.sendFile(P('healthrecord.html')));
    router.get('/settings',    requireLogin, (req, res) => res.sendFile(P('settings.html')));

    // Doctor pages
    router.get('/doctor',         requireLogin, (req, res) => res.sendFile(P('doctor.html')));
    router.get('/mypatients',     requireLogin, (req, res) => res.sendFile(P('mypatients.html')));
    router.get('/addresult',      requireLogin, (req, res) => res.sendFile(P('addresult.html')));
    router.get('/doctorsettings', requireLogin, (req, res) => res.sendFile(P('doctorsettings.html')));

    // Admin page
    router.get('/admin', requireLogin, (req, res) => res.sendFile(P('admin.html')));

    // Logout
    router.get('/logout', (req, res) => {
        req.session.destroy();
        res.redirect('/');
    });

    return router;
};
