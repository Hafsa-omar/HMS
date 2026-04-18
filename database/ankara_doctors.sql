-- =============================================
-- Ankara doctors — one per specialty (all 56)
-- Fills in every specialty missing from Ankara
-- Run AFTER all_doctors.sql and fix_specialties.sql
-- =============================================
USE hospital_management;
SET NAMES utf8mb4;
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

INSERT INTO doctor (docname, docemail, docpassword, docnic, doctel, specialties, country, city, hospital_branch, hospital_type, consultation_fee, available, rating, review_count) VALUES

-- Specialty 1: Anaesthesiology
('Dr. Ali Kara',            'ali.kara@hms.com',             '123', 'TR-ANK-A01', '+90-312-3051100', 1,  'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   55,  1, 4.5, 20),
-- Specialty 2: Cardiology
('Dr. Seda Polat',          'seda.polat@hms.com',           '123', 'TR-ANK-A02', '+90-312-3051101', 2,  'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   60,  1, 4.7, 34),
-- Specialty 3: Cardiothoracic Surgery
('Dr. Bulent Yilmaz',       'bulent.yilmaz@hms.com',        '123', 'TR-ANK-A03', '+90-312-5085100', 3,  'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   70,  1, 4.6, 28),
-- Specialty 4: Vascular Surgery
('Dr. Nur Ozdemir',         'nur.ozdemir@hms.com',          '123', 'TR-ANK-A04', '+90-312-4681100', 4,  'Turkey', 'Ankara', 'Guven Hospital',                   'private',  85,  1, 4.8, 42),
-- Specialty 6: Child Psychiatry
('Dr. Leyla Akgun',         'leyla.akgun@hms.com',          '123', 'TR-ANK-A06', '+90-312-4283100', 6,  'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  90,  1, 4.7, 30),
-- Specialty 7: Clinical Biology
('Dr. Emre Toprak',         'emre.toprak@hms.com',          '123', 'TR-ANK-A07', '+90-312-3051102', 7,  'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   50,  1, 4.4, 15),
-- Specialty 8: Clinical Chemistry
('Dr. Aylin Celik',         'aylin.celik@hms.com',          '123', 'TR-ANK-A08', '+90-312-3051103', 8,  'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   50,  1, 4.3, 12),
-- Specialty 9: Clinical Neurophysiology
('Dr. Orhan Yildiz',        'orhan.yildiz@hms.com',         '123', 'TR-ANK-A09', '+90-312-5085101', 9,  'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   55,  1, 4.5, 18),
-- Specialty 10: Clinical Pharmacology
('Dr. Fatma Arslan',        'fatma.arslan@hms.com',         '123', 'TR-ANK-A10', '+90-312-4681101', 10, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  80,  1, 4.6, 22),
-- Specialty 11: Dental & Oral Surgery
('Dr. Hakan Sahin',         'hakan.sahin@hms.com',          '123', 'TR-ANK-A11', '+90-312-4283101', 11, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  95,  1, 4.8, 48),
-- Specialty 12: Emergency Medicine
('Dr. Zehra Koc',           'zehra.koc@hms.com',            '123', 'TR-ANK-A12', '+90-312-3051104', 12, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   45,  1, 4.5, 35),
-- Specialty 15: Gastro-Enterologic Surgery
('Dr. Serhat Demirci',      'serhat.demirci@hms.com',       '123', 'TR-ANK-A15', '+90-312-5085102', 15, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   65,  1, 4.6, 26),
-- Specialty 16: General Medicine
('Dr. Nilufer Yilmaz',      'nilufer.yilmaz@hms.com',       '123', 'TR-ANK-A16', '+90-312-4681102', 16, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  80,  1, 4.7, 38),
-- Specialty 17: General Hematology
('Dr. Tayfun Aksoy',        'tayfun.aksoy@hms.com',         '123', 'TR-ANK-A17', '+90-312-3051105', 17, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   60,  1, 4.8, 45),
-- Specialty 18: General Surgery
('Dr. Gulsen Kaya',         'gulsen.kaya@hms.com',          '123', 'TR-ANK-A18', '+90-312-5085103', 18, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   55,  1, 4.5, 22),
-- Specialty 20: Gynaecology & Obstetrics
('Dr. Arzu Polat',          'arzu.polat@hms.com',           '123', 'TR-ANK-A20', '+90-312-4283102', 20, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  90,  1, 4.9, 62),
-- Specialty 21: Hand Surgery
('Dr. Cengiz Aydın',        'cengiz.aydin@hms.com',         '123', 'TR-ANK-A21', '+90-312-4681103', 21, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  85,  1, 4.6, 28),
-- Specialty 22: Haematology-Oncology
('Dr. Sibel Ozturk',        'sibel.ozturk@hms.com',         '123', 'TR-ANK-A22', '+90-312-3051106', 22, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   65,  1, 4.7, 40),
-- Specialty 23: Internal Medicine
('Dr. Kadir Yildirim',      'kadir.yildirim@hms.com',       '123', 'TR-ANK-A23', '+90-312-5085104', 23, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   50,  1, 4.5, 30),
-- Specialty 24: Laboratory Medicine
('Dr. Pelin Kara',          'pelin.kara@hms.com',           '123', 'TR-ANK-A24', '+90-312-4283103', 24, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  80,  1, 4.4, 18),
-- Specialty 25: Maxillo-Facial Surgery
('Dr. Volkan Demir',        'volkan.demir@hms.com',         '123', 'TR-ANK-A25', '+90-312-4681104', 25, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  95,  1, 4.7, 32),
-- Specialty 26: Microbiology
('Dr. Elif Arslan',         'elif.arslan@hms.com',           '123', 'TR-ANK-A26', '+90-312-3051107', 26, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   50,  1, 4.3, 14),
-- Specialty 27: Nephrology
('Dr. Omer Sahin',          'omer.sahin@hms.com',           '123', 'TR-ANK-A27', '+90-312-5085105', 27, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   60,  1, 4.6, 36),
-- Specialty 28: Neuro-Psychiatry
('Dr. Irem Yilmaz',         'irem.yilmaz@hms.com',          '123', 'TR-ANK-A28', '+90-312-4283104', 28, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  90,  1, 4.8, 50),
-- Specialty 30: Neurosurgery
('Dr. Murat Ozkan',         'murat.ozkan@hms.com',          '123', 'TR-ANK-A30', '+90-312-4681105', 30, 'Turkey', 'Ankara', 'Guven Hospital',                   'private', 110,  1, 4.9, 58),
-- Specialty 31: Nuclear Medicine
('Dr. Tuba Celik',          'tuba.celik@hms.com',           '123', 'TR-ANK-A31', '+90-312-3051108', 31, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   60,  1, 4.5, 20),
-- Specialty 33: Occupational Medicine
('Dr. Selim Koc',           'selim.koc@hms.com',            '123', 'TR-ANK-A33', '+90-312-5085106', 33, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   45,  1, 4.4, 16),
-- Specialty 34: Oncology
('Dr. Bahar Demir',         'bahar.demir@hms.com',          '123', 'TR-ANK-A34', '+90-312-3051109', 34, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   70,  1, 4.8, 55),
-- Specialty 36: Oral Surgery
('Dr. Kerem Arslan',        'kerem.arslan@hms.com',         '123', 'TR-ANK-A36', '+90-312-4283105', 36, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  85,  1, 4.6, 25),
-- Specialty 37: Orthopaedics
('Dr. Fikret Yildirim',     'fikret.yildirim@hms.com',      '123', 'TR-ANK-A37', '+90-312-4681106', 37, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  90,  1, 4.7, 44),
-- Specialty 39: Pathology
('Dr. Gokhan Ozturk',       'gokhan.ozturk@hms.com',        '123', 'TR-ANK-A39', '+90-312-3051110', 39, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   55,  1, 4.5, 18),
-- Specialty 40: Pharmacology
('Dr. Cemre Yilmaz',        'cemre.yilmaz@hms.com',         '123', 'TR-ANK-A40', '+90-312-5085107', 40, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   50,  1, 4.4, 14),
-- Specialty 41: Paediatrics
('Dr. Hatice Kara',         'hatice.kara@hms.com',          '123', 'TR-ANK-A41', '+90-312-4283106', 41, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  80,  1, 4.8, 52),
-- Specialty 42: Physical Medicine & Rehabilitation
('Dr. Umut Sahin',          'umut.sahin@hms.com',           '123', 'TR-ANK-A42', '+90-312-4681107', 42, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  85,  1, 4.6, 30),
-- Specialty 43: Podiatric Medicine
('Dr. Nazli Celik',         'nazli.celik@hms.com',          '123', 'TR-ANK-A43', '+90-312-3051111', 43, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   50,  1, 4.3, 12),
-- Specialty 44: Podiatric Surgery
('Dr. Enes Demir',          'enes.demir@hms.com',           '123', 'TR-ANK-A44', '+90-312-5085108', 44, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   55,  1, 4.4, 16),
-- Specialty 45: Psychiatry
('Dr. Sinem Yilmaz',        'sinem.yilmaz@hms.com',         '123', 'TR-ANK-A45', '+90-312-4283107', 45, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  90,  1, 4.7, 38),
-- Specialty 46: Public Health & Preventive Medicine
('Dr. Bora Koc',            'bora.koc@hms.com',             '123', 'TR-ANK-A46', '+90-312-3051112', 46, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   45,  1, 4.4, 15),
-- Specialty 47: Pulmonology
('Dr. Meltem Arslan',       'meltem.arslan@hms.com',        '123', 'TR-ANK-A47', '+90-312-5085109', 47, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   60,  1, 4.6, 28),
-- Specialty 48: Radiotherapy
('Dr. Recep Ozkan',         'recep.ozkan@hms.com',          '123', 'TR-ANK-A48', '+90-312-3051113', 48, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   65,  1, 4.7, 35),
-- Specialty 49: Radiology
('Dr. Dilek Yildirim',      'dilek.yildirim@hms.com',       '123', 'TR-ANK-A49', '+90-312-4681108', 49, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  80,  1, 4.6, 27),
-- Specialty 50: Rheumatology
('Dr. Caner Kaya',          'caner.kaya@hms.com',           '123', 'TR-ANK-A50', '+90-312-4283108', 50, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  85,  1, 4.7, 33),
-- Specialty 51: Stomatology
('Dr. Ipek Sahin',          'ipek.sahin@hms.com',           '123', 'TR-ANK-A51', '+90-312-5085110', 51, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   55,  1, 4.5, 20),
-- Specialty 52: Thoracic Surgery
('Dr. Tolga Celik',         'tolga.celik@hms.com',          '123', 'TR-ANK-A52', '+90-312-3051114', 52, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   70,  1, 4.7, 40),
-- Specialty 53: Toxicology
('Dr. Merve Demir',         'merve.demir@hms.com',          '123', 'TR-ANK-A53', '+90-312-4681109', 53, 'Turkey', 'Ankara', 'Guven Hospital',                   'private',  80,  1, 4.5, 18),
-- Specialty 54: Tropical Medicine
('Dr. Sercan Arslan',       'sercan.arslan@hms.com',        '123', 'TR-ANK-A54', '+90-312-5085111', 54, 'Turkey', 'Ankara', 'Ankara City Hospital',             'public',   55,  1, 4.4, 14),
-- Specialty 55: Urology
('Dr. Yusuf Kara',          'yusuf.kara@hms.com',           '123', 'TR-ANK-A55', '+90-312-4283109', 55, 'Turkey', 'Ankara', 'Bayindir Kavaklidere Hospital',    'private',  90,  1, 4.8, 46),
-- Specialty 56: Venereology
('Dr. Asli Yilmaz',         'asli.yilmaz@hms.com',          '123', 'TR-ANK-A56', '+90-312-3051115', 56, 'Turkey', 'Ankara', 'Hacettepe University Hospital',    'public',   50,  1, 4.3, 10);

-- Add webuser entries for new doctors
INSERT IGNORE INTO webuser (email, usertype)
SELECT docemail, 'd' FROM doctor
WHERE city = 'Ankara' AND docemail LIKE '%@hms.com%'
  AND docemail NOT IN (SELECT email FROM webuser);

SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;

SELECT COUNT(*) AS ankara_doctors FROM doctor WHERE city = 'Ankara';
