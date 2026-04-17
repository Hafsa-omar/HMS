-- ============================================================
-- HMS — Add More Doctors (Turkey + UAE focus)
-- Run this ONCE in MySQL Workbench
-- ============================================================
USE hospital_management;
SET SQL_SAFE_UPDATES   = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- ─────────────────────────────────────────────
-- 1. MAKE SURE SPECIALTIES TABLE EXISTS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS specialties (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    sname VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO specialties (id, sname) VALUES
(1,  'Cardiology'),
(2,  'Neurology'),
(3,  'Orthopedics'),
(4,  'Pediatrics'),
(5,  'Dermatology'),
(6,  'Oncology'),
(7,  'Gynecology'),
(8,  'Ophthalmology'),
(9,  'ENT'),
(10, 'General Medicine'),
(11, 'Psychiatry'),
(12, 'Urology'),
(13, 'Endocrinology'),
(14, 'Gastroenterology'),
(15, 'Pulmonology');

-- ─────────────────────────────────────────────
-- 2. UPDATE EXISTING 6 DOCTORS — SET TURKEY
-- ─────────────────────────────────────────────
UPDATE doctor SET country='Turkey', city='Ankara', hospital_branch='HMS Ankara Central',
    hospital_type='public', consultation_fee=40, available=1, rating=4.5, review_count=18
WHERE docid = 1;

UPDATE doctor SET country='Turkey', city='Ankara', hospital_branch='HMS Ankara Central',
    hospital_type='public', consultation_fee=40, available=1, rating=4.3, review_count=12
WHERE docid = 2;

UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Medical Center',
    hospital_type='public', consultation_fee=55, available=1, rating=4.6, review_count=24
WHERE docid = 3;

UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Private',
    hospital_type='private', consultation_fee=120, available=1, rating=4.7, review_count=31
WHERE docid = 4;

UPDATE doctor SET country='Turkey', city='Ankara', hospital_branch='HMS Ankara Central',
    hospital_type='public', consultation_fee=40, available=1, rating=4.4, review_count=15
WHERE docid = 5;

UPDATE doctor SET country='Turkey', city='Izmir', hospital_branch='HMS Izmir Clinic',
    hospital_type='public', consultation_fee=35, available=1, rating=4.2, review_count=9
WHERE docid = 6;

-- ─────────────────────────────────────────────
-- 3. NEW TURKEY DOCTORS (docid 7–14)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(7,  'Dr. Ayse Kaya',       'ayse.kaya@hms.com',      '123', '10001001', '0530001007', 5),
(8,  'Dr. Mehmet Yilmaz',   'mehmet.yilmaz@hms.com',  '123', '10001002', '0530001008', 7),
(9,  'Dr. Fatma Demir',     'fatma.demir@hms.com',    '123', '10001003', '0530001009', 10),
(10, 'Dr. Emre Arslan',     'emre.arslan@hms.com',    '123', '10001004', '0530001010', 13),
(11, 'Dr. Zeynep Celik',    'zeynep.celik@hms.com',   '123', '10001005', '0530001011', 6),
(12, 'Dr. Burak Sahin',     'burak.sahin@hms.com',    '123', '10001006', '0530001012', 14),
(13, 'Dr. Selin Ozturk',    'selin.ozturk@hms.com',   '123', '10001007', '0530001013', 11),
(14, 'Dr. Tarık Yıldız',    'tarik.yildiz@hms.com',   '123', '10001008', '0530001014', 15);

UPDATE doctor SET country='Turkey', city='Ankara',   hospital_branch='HMS Ankara Central',       hospital_type='public',  consultation_fee=45,  available=1, rating=4.6, review_count=22 WHERE docid = 7;
UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Medical Center',hospital_type='public',  consultation_fee=55,  available=1, rating=4.4, review_count=17 WHERE docid = 8;
UPDATE doctor SET country='Turkey', city='Ankara',   hospital_branch='HMS Ankara Central',       hospital_type='public',  consultation_fee=40,  available=1, rating=4.8, review_count=35 WHERE docid = 9;
UPDATE doctor SET country='Turkey', city='Izmir',    hospital_branch='HMS Izmir Clinic',         hospital_type='public',  consultation_fee=35,  available=1, rating=4.3, review_count=11 WHERE docid = 10;
UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Private',     hospital_type='private', consultation_fee=130, available=1, rating=4.9, review_count=48 WHERE docid = 11;
UPDATE doctor SET country='Turkey', city='Ankara',   hospital_branch='HMS Ankara Central',       hospital_type='public',  consultation_fee=40,  available=1, rating=4.5, review_count=19 WHERE docid = 12;
UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Private',     hospital_type='private', consultation_fee=120, available=1, rating=4.7, review_count=29 WHERE docid = 13;
UPDATE doctor SET country='Turkey', city='Izmir',    hospital_branch='HMS Izmir Clinic',         hospital_type='public',  consultation_fee=35,  available=1, rating=4.1, review_count=8  WHERE docid = 14;

-- ─────────────────────────────────────────────
-- 4. NEW UAE DOCTORS (docid 15–22)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(15, 'Dr. Khalid Al-Mansoori', 'khalid.mansoori@hms.com', '123', '20001001', '0501001015', 1),
(16, 'Dr. Layla Al-Hashimi',   'layla.hashimi@hms.com',   '123', '20001002', '0501001016', 2),
(17, 'Dr. Omar Al-Rashidi',    'omar.rashidi@hms.com',    '123', '20001003', '0501001017', 3),
(18, 'Dr. Noura Al-Maktoum',   'noura.maktoum@hms.com',   '123', '20001004', '0501001018', 4),
(19, 'Dr. Faisal Al-Zaabi',    'faisal.zaabi@hms.com',    '123', '20001005', '0501001019', 6),
(20, 'Dr. Mariam Al-Suwaidi',  'mariam.suwaidi@hms.com',  '123', '20001006', '0501001020', 7),
(21, 'Dr. Ahmed Al-Nuaimi',    'ahmed.nuaimi@hms.com',    '123', '20001007', '0501001021', 8),
(22, 'Dr. Sara Al-Qubaisi',    'sara.qubaisi@hms.com',    '123', '20001008', '0501001022', 9);

UPDATE doctor SET country='UAE', city='Dubai',     hospital_branch='HMS Dubai Premium',    hospital_type='private', consultation_fee=200, available=1, rating=4.8, review_count=52 WHERE docid = 15;
UPDATE doctor SET country='UAE', city='Dubai',     hospital_branch='HMS Dubai Premium',    hospital_type='private', consultation_fee=200, available=1, rating=4.7, review_count=44 WHERE docid = 16;
UPDATE doctor SET country='UAE', city='Abu Dhabi', hospital_branch='HMS Abu Dhabi Public', hospital_type='public',  consultation_fee=60,  available=1, rating=4.5, review_count=28 WHERE docid = 17;
UPDATE doctor SET country='UAE', city='Abu Dhabi', hospital_branch='HMS Abu Dhabi Public', hospital_type='public',  consultation_fee=60,  available=1, rating=4.6, review_count=33 WHERE docid = 18;
UPDATE doctor SET country='UAE', city='Dubai',     hospital_branch='HMS Dubai Premium',    hospital_type='private', consultation_fee=220, available=1, rating=4.9, review_count=67 WHERE docid = 19;
UPDATE doctor SET country='UAE', city='Abu Dhabi', hospital_branch='HMS Abu Dhabi Public', hospital_type='public',  consultation_fee=65,  available=1, rating=4.4, review_count=21 WHERE docid = 20;
UPDATE doctor SET country='UAE', city='Dubai',     hospital_branch='HMS Dubai Medical City',hospital_type='private', consultation_fee=180, available=1, rating=4.6, review_count=38 WHERE docid = 21;
UPDATE doctor SET country='UAE', city='Abu Dhabi', hospital_branch='HMS Abu Dhabi Public', hospital_type='public',  consultation_fee=60,  available=1, rating=4.3, review_count=16 WHERE docid = 22;

-- ─────────────────────────────────────────────
-- 5. UK DOCTORS (docid 23–25)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(23, 'Dr. Oliver Bennett',  'oliver.bennett@hms.com',  '123', '30001001', '07700001023', 1),
(24, 'Dr. Charlotte Evans', 'charlotte.evans@hms.com', '123', '30001002', '07700001024', 3),
(25, 'Dr. William Harris',  'william.harris@hms.com',  '123', '30001003', '07700001025', 10);

UPDATE doctor SET country='UK', city='London', hospital_branch='HMS London NHS',     hospital_type='public',  consultation_fee=0,   available=1, rating=4.5, review_count=71 WHERE docid = 23;
UPDATE doctor SET country='UK', city='London', hospital_branch='HMS London NHS',     hospital_type='public',  consultation_fee=0,   available=1, rating=4.3, review_count=55 WHERE docid = 24;
UPDATE doctor SET country='UK', city='London', hospital_branch='HMS London Private', hospital_type='private', consultation_fee=180, available=1, rating=4.8, review_count=89 WHERE docid = 25;

-- ─────────────────────────────────────────────
-- 6. GERMANY DOCTORS (docid 26–28)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(26, 'Dr. Hans Mueller',    'hans.mueller@hms.com',    '123', '40001001', '01700001026', 2),
(27, 'Dr. Anna Schmidt',    'anna.schmidt@hms.com',    '123', '40001002', '01700001027', 5),
(28, 'Dr. Klaus Wagner',    'klaus.wagner@hms.com',    '123', '40001003', '01700001028', 12);

UPDATE doctor SET country='Germany', city='Berlin', hospital_branch='HMS Berlin Klinik',   hospital_type='public',  consultation_fee=20,  available=1, rating=4.5, review_count=38 WHERE docid = 26;
UPDATE doctor SET country='Germany', city='Berlin', hospital_branch='HMS Berlin Klinik',   hospital_type='public',  consultation_fee=20,  available=1, rating=4.4, review_count=29 WHERE docid = 27;
UPDATE doctor SET country='Germany', city='Berlin', hospital_branch='HMS Berlin Private',  hospital_type='private', consultation_fee=150, available=1, rating=4.7, review_count=44 WHERE docid = 28;

-- ─────────────────────────────────────────────
-- 7. USA DOCTORS (docid 29–31)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(29, 'Dr. James Carter',    'james.carter@hms.com',    '123', '50001001', '12120001029', 1),
(30, 'Dr. Emily Davis',     'emily.davis@hms.com',     '123', '50001002', '12120001030', 6),
(31, 'Dr. Robert Wilson',   'robert.wilson@hms.com',   '123', '50001003', '12120001031', 11);

UPDATE doctor SET country='USA', city='New York', hospital_branch='HMS NYC Hospital', hospital_type='public',  consultation_fee=100, available=1, rating=4.2, review_count=15 WHERE docid = 29;
UPDATE doctor SET country='USA', city='New York', hospital_branch='HMS NYC Premium',  hospital_type='private', consultation_fee=300, available=1, rating=4.9, review_count=108 WHERE docid = 30;
UPDATE doctor SET country='USA', city='New York', hospital_branch='HMS NYC Hospital', hospital_type='public',  consultation_fee=100, available=1, rating=4.4, review_count=27 WHERE docid = 31;

-- ─────────────────────────────────────────────
-- 8. FRANCE DOCTORS (docid 32–33)
-- ─────────────────────────────────────────────
INSERT INTO doctor (docid, docname, docemail, docpassword, docnic, doctel, specialties) VALUES
(32, 'Dr. Pierre Dubois',   'pierre.dubois@hms.com',   '123', '60001001', '0600001032', 8),
(33, 'Dr. Marie Leclerc',   'marie.leclerc@hms.com',   '123', '60001002', '0600001033', 7);

UPDATE doctor SET country='France', city='Paris', hospital_branch='HMS Paris Clinic',   hospital_type='public',  consultation_fee=30,  available=1, rating=4.4, review_count=23 WHERE docid = 32;
UPDATE doctor SET country='France', city='Paris', hospital_branch='HMS Paris Premium',  hospital_type='private', consultation_fee=160, available=1, rating=4.7, review_count=41 WHERE docid = 33;

-- ─────────────────────────────────────────────
-- 9. ADD ALL NEW DOCTORS TO WEBUSER TABLE
-- ─────────────────────────────────────────────
INSERT IGNORE INTO webuser (email, usertype) VALUES
('ayse.kaya@hms.com',      'd'),
('mehmet.yilmaz@hms.com',  'd'),
('fatma.demir@hms.com',    'd'),
('emre.arslan@hms.com',    'd'),
('zeynep.celik@hms.com',   'd'),
('burak.sahin@hms.com',    'd'),
('selin.ozturk@hms.com',   'd'),
('tarik.yildiz@hms.com',   'd'),
('khalid.mansoori@hms.com','d'),
('layla.hashimi@hms.com',  'd'),
('omar.rashidi@hms.com',   'd'),
('noura.maktoum@hms.com',  'd'),
('faisal.zaabi@hms.com',   'd'),
('mariam.suwaidi@hms.com', 'd'),
('ahmed.nuaimi@hms.com',   'd'),
('sara.qubaisi@hms.com',   'd'),
('oliver.bennett@hms.com', 'd'),
('charlotte.evans@hms.com','d'),
('william.harris@hms.com', 'd'),
('hans.mueller@hms.com',   'd'),
('anna.schmidt@hms.com',   'd'),
('klaus.wagner@hms.com',   'd'),
('james.carter@hms.com',   'd'),
('emily.davis@hms.com',    'd'),
('robert.wilson@hms.com',  'd'),
('pierre.dubois@hms.com',  'd'),
('marie.leclerc@hms.com',  'd');

SET SQL_SAFE_UPDATES   = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- ─────────────────────────────────────────────
-- VERIFY
-- ─────────────────────────────────────────────
SELECT country, COUNT(*) AS total_doctors FROM doctor GROUP BY country ORDER BY total_doctors DESC;
SELECT docid, docname, country, city, hospital_branch FROM doctor ORDER BY country, city;
