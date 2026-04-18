-- =============================================
-- Fix specialties table: insert all 56 specialties
-- matching the numbering used in all_doctors.sql
-- Run once after all_doctors.sql
-- =============================================
USE hospital_management;
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- Replace all existing specialties with the full 56-entry list
DELETE FROM specialties;

INSERT INTO specialties (id, sname) VALUES
(1,  'Anaesthesiology'),
(2,  'Cardiology'),
(3,  'Cardiothoracic Surgery'),
(4,  'Vascular Surgery'),
(5,  'Dermatology'),
(6,  'Child Psychiatry'),
(7,  'Clinical Biology'),
(8,  'Clinical Chemistry'),
(9,  'Clinical Neurophysiology'),
(10, 'Clinical Pharmacology'),
(11, 'Dental & Oral Surgery'),
(12, 'Emergency Medicine'),
(13, 'Endocrinology'),
(14, 'Gastroenterology'),
(15, 'Gastro-Enterologic Surgery'),
(16, 'General Medicine'),
(17, 'General Hematology'),
(18, 'General Surgery'),
(19, 'Geriatrics'),
(20, 'Gynaecology & Obstetrics'),
(21, 'Hand Surgery'),
(22, 'Haematology-Oncology'),
(23, 'Internal Medicine'),
(24, 'Laboratory Medicine'),
(25, 'Maxillo-Facial Surgery'),
(26, 'Microbiology'),
(27, 'Nephrology'),
(28, 'Neuro-Psychiatry'),
(29, 'Neurology'),
(30, 'Neurosurgery'),
(31, 'Nuclear Medicine'),
(32, 'Obstetrics & Gynaecology'),
(33, 'Occupational Medicine'),
(34, 'Oncology'),
(35, 'Ophthalmology'),
(36, 'Oral Surgery'),
(37, 'Orthopaedics'),
(38, 'Otolaryngology (ENT)'),
(39, 'Pathology'),
(40, 'Pharmacology'),
(41, 'Paediatrics'),
(42, 'Physical Medicine & Rehabilitation'),
(43, 'Podiatric Medicine'),
(44, 'Podiatric Surgery'),
(45, 'Psychiatry'),
(46, 'Public Health & Preventive Medicine'),
(47, 'Pulmonology'),
(48, 'Radiotherapy'),
(49, 'Radiology'),
(50, 'Rheumatology'),
(51, 'Stomatology'),
(52, 'Thoracic Surgery'),
(53, 'Toxicology'),
(54, 'Tropical Medicine'),
(55, 'Urology'),
(56, 'Venereology');

SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- Verify
SELECT id, sname FROM specialties ORDER BY id;
SELECT COUNT(*) AS total_specialties FROM specialties;
SELECT s.sname, COUNT(d.docid) AS doctor_count
FROM specialties s
LEFT JOIN doctor d ON s.id = d.specialties
GROUP BY s.id, s.sname
ORDER BY doctor_count DESC
LIMIT 20;
