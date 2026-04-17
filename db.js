const mysql = require('mysql2');



const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',      
  password: '',     
  database: 'hospital_management',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

pool.getConnection((err, connection) => {
  if (err) {
    console.error('CRITICAL: Database connection failed!');
    console.error('Error details: ' + err.message);
    return;
  }
  console.log('--- HMS DATABASE STATUS: ONLINE ---');
  console.log('Connected to thread ID: ' + connection.threadId);
  connection.release(); 
});

module.exports = pool.promise();