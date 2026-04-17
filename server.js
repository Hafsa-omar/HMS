require('dotenv').config();
const express = require('express');
const mysql   = require('mysql2');
const path    = require('path');
const session = require('express-session');
const app     = express();

// ── Middleware ────────────────────────────────────────────────────────────────
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(session({
    secret:            process.env.SESSION_SECRET,
    resave:            false,
    saveUninitialized: false,
    cookie:            { maxAge: 24 * 60 * 60 * 1000 }
}));

// ── Database ──────────────────────────────────────────────────────────────────
const db = mysql.createConnection({
    host:     process.env.DB_HOST,
    user:     process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
    port:     3306
});
db.connect((err) => {
    if (err) { console.error('DB Error: ' + err.message); return; }
    console.log('✅ Database connected!');
});

// ── Auth guard ────────────────────────────────────────────────────────────────
function requireLogin(req, res, next) {
    if (!req.session.user) return res.redirect('/login');
    next();
}

// ── Routes ────────────────────────────────────────────────────────────────────
app.use('/',          require('./routes/pages')(requireLogin));
app.use('/auth',      require('./routes/auth')(db));
app.use('/api',       require('./routes/patient')(db, requireLogin));
app.use('/api/doctor',require('./routes/doctor')(db, requireLogin));
app.use('/api/admin', require('./routes/admin')(db, requireLogin));
app.use('/api/chat',  require('./routes/chatbot')(db, requireLogin));

// ── Start ─────────────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`\n🏥 HMS running at: http://localhost:${PORT}\n`));
