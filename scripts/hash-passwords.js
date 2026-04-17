// One-time script — hashes all existing plain-text passwords in the database
// Run once with: node scripts/hash-passwords.js
require('dotenv').config();
const mysql = require('mysql2');
const bcrypt = require('bcrypt');

const db = mysql.createConnection({
    host:     process.env.DB_HOST,
    user:     process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
    port:     3306
});

async function hashColumn(table, idCol, passCol) {
    return new Promise((resolve, reject) => {
        db.query(`SELECT ${idCol}, ${passCol} FROM ${table}`, async (err, rows) => {
            if (err) return reject(err);
            let updated = 0;
            for (const row of rows) {
                const plain = row[passCol];
                // Skip already-hashed values (bcrypt hashes start with $2b$)
                if (!plain || plain.startsWith('$2b$')) continue;
                const hashed = await bcrypt.hash(plain, 10);
                await new Promise((res, rej) => {
                    db.query(`UPDATE ${table} SET ${passCol} = ? WHERE ${idCol} = ?`,
                        [hashed, row[idCol]], (e) => e ? rej(e) : res());
                });
                updated++;
            }
            console.log(`✅ ${table}: ${updated} passwords hashed`);
            resolve();
        });
    });
}

(async () => {
    try {
        await hashColumn('patient', 'pid',   'ppassword');
        await hashColumn('doctor',  'docid', 'docpassword');
        await hashColumn('admin',   'aemail','apassword');
        console.log('\n✅ All passwords hashed successfully.');
    } catch (e) {
        console.error('Error:', e.message);
    } finally {
        db.end();
    }
})();
