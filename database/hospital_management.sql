-- ============================================================
-- HMS Base Data Reset
-- ============================================================
USE hospital_management;
SET SQL_SAFE_UPDATES   = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- Clear tables in correct order (child tables first)
DELETE FROM appointment;
DELETE FROM doctor;
DELETE FROM patient;
DELETE FROM webuser;

-- INSERT DOCTORS
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(1, 'Dr. Sara Ali',      'doctor1@hms.com', '123', '11111111', '0532000001', 1),
(2, 'Dr. John Smith',    'doctor2@hms.com', '123', '22222222', '0532000002', 2),
(3, 'Dr. Sarah Johnson', 'sarah@hms.com',   '123', '33333333', '0533000003', 3),
(4, 'Dr. Michael Brown', 'michael@hms.com', '123', '44444444', '0534000004', 4),
(5, 'Dr. Emily White',   'emily@hms.com',   '123', '55555555', '0535000005', 1),
(6, 'Dr. James Wilson',  'james@hms.com',   '123', '66666666', '0536000006', 2);

-- INSERT PATIENTS
INSERT INTO patient (pid, pname, pemail, ppassword, pnic, ptel, paddress, pdob) VALUES
(1, 'John Doe',         'john@example.com',   '123', '99999999', '0500111222', 'Main St 1',       '1990-01-01'),
(2, 'Mary Jane',        'mary@example.com',   '123', '88881111', '0500333444', 'Second St 5',     '1985-05-12'),
(3, 'Ali Hassan',       'ali@example.com',    '123', '77772222', '0500555666', 'Highway 10',      '1998-11-20'),
(4, 'Sarah Connor',     'sarahc@example.com', '123', '66663333', '0500777888', 'Industrial Ave',  '1975-03-30'),
(5, 'Ahmed Al-Rashidi', 'demo@hms.com',       '123', 'TR990AR',  '05324418820','14 Ataturk Blvd, Ankara', '1990-11-05');

-- INSERT WEBUSERS
INSERT INTO webuser (email, usertype) VALUES
('doctor1@hms.com',    'd'),
('doctor2@hms.com',    'd'),
('sarah@hms.com',      'd'),
('michael@hms.com',    'd'),
('emily@hms.com',      'd'),
('james@hms.com',      'd'),
('john@example.com',   'p'),
('mary@example.com',   'p'),
('ali@example.com',    'p'),
('sarahc@example.com', 'p'),
('demo@hms.com',       'p');

-- INSERT APPOINTMENTS
INSERT INTO appointment (pid, scheduleid, apponum, appodate, status) VALUES
(1, 1, 1, '2026-03-01', 'BOOKED'),
(2, 2, 1, '2026-03-01', 'BOOKED'),
(3, 3, 1, '2026-03-01', 'CHECKED_IN'),
(4, 4, 1, '2026-03-02', 'BOOKED'),
(1, 5, 2, '2026-03-02', 'BOOKED'),
(2, 6, 2, '2026-03-02', 'CANCELLED'),
(1, 1, 3, '2026-03-03', 'BOOKED');

SET SQL_SAFE_UPDATES   = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- Verify
SELECT COUNT(*) AS doctors      FROM doctor;
SELECT COUNT(*) AS patients     FROM patient;
SELECT COUNT(*) AS appointments FROM appointment;
