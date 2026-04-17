
USE hospital_management;
SET SQL_SAFE_UPDATES   = 0;
SET FOREIGN_KEY_CHECKS = 0;


SET @pid  = (SELECT pid   FROM patient WHERE pemail   = 'demo@hms.com'    LIMIT 1);
SET @doc1 = (SELECT docid FROM doctor  WHERE docemail = 'doctor1@hms.com' LIMIT 1);
SET @doc2 = (SELECT docid FROM doctor  WHERE docemail = 'doctor2@hms.com' LIMIT 1);


SELECT @pid AS demo_pid, @doc1 AS doc1_id, @doc2 AS doc2_id;


DELETE FROM lab_result  WHERE pid = @pid;
DELETE FROM appointment WHERE pid = @pid;


INSERT INTO appointment (pid, scheduleid, apponum, appodate, status) VALUES
(@pid, @doc1, 1, '2025-08-14', 'CHECKED_IN'),
(@pid, @doc1, 2, '2025-09-20', 'CHECKED_IN'),
(@pid, @doc2, 1, '2025-10-05', 'CHECKED_IN'),
(@pid, @doc1, 3, '2025-11-02', 'CHECKED_IN'),
(@pid, @doc1, 4, '2025-12-18', 'CHECKED_IN'),
(@pid, @doc1, 5, '2026-02-10', 'CHECKED_IN'),
(@pid, @doc1, 6, '2026-05-15', 'BOOKED');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc1, 'Blood Sugar (Glucose)',
 'Fasting: 198 mg/dL  |  Post-meal: 287 mg/dL',
 'High — CRITICALLY ELEVATED. Fasting glucose 198 (normal below 100). Post-meal 287 (normal below 140). Type 2 Diabetes Mellitus diagnosed. Metformin 500mg twice daily started.',
 '2025-08-14 09:30:00'),

(@pid, @doc1, 'Hemoglobin',
 'Hb: 11.2 g/dL',
 'Low — Mild anemia. Normal male range is 13.5 to 17.5 g/dL. Iron supplementation Ferrous Sulfate 200mg daily prescribed.',
 '2025-08-14 09:45:00'),

(@pid, @doc1, 'CBC - Complete Blood Count',
 'WBC: 10.8 K/uL  |  RBC: 4.1 M/uL  |  Platelets: 210 K/uL',
 'High — Borderline elevated WBC, normal is 4.5 to 11.0. May indicate low-grade infection. Repeat if symptoms worsen.',
 '2025-08-14 09:50:00'),

(@pid, @doc1, 'Thyroid Function (TSH)',
 'TSH: 3.8 mIU/L',
 'Normal — TSH within normal range 0.4 to 4.0 mIU/L. No thyroid disorder detected.',
 '2025-08-14 10:05:00');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc1, 'Cholesterol',
 'Total: 248 mg/dL  |  LDL: 162 mg/dL  |  HDL: 38 mg/dL  |  Triglycerides: 210 mg/dL',
 'High — Total cholesterol 248 (normal below 200). LDL 162 (optimal below 100). Cardiovascular risk elevated. Atorvastatin 20mg prescribed. Low-fat diet advised.',
 '2025-09-20 10:15:00'),

(@pid, @doc1, 'Blood Pressure Check',
 '148/94 mmHg',
 'High — Stage 1 Hypertension. Normal is below 120/80. Amlodipine 5mg once daily prescribed.',
 '2025-09-20 10:30:00'),

(@pid, @doc1, 'Vitamin D',
 '14 ng/mL',
 'Low — Vitamin D deficiency. Normal range is 20 to 50 ng/mL. Vitamin D3 5000 IU per day prescribed for 3 months.',
 '2025-09-20 10:45:00');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc2, 'Urinalysis - Complete',
 'Nitrites: POSITIVE  |  Leukocytes: 3+  |  Bacteria: Many  |  Glucose: +2',
 'Positive — UTI confirmed. Significant pyuria and bacteriuria. Ciprofloxacin 500mg twice daily for 7 days prescribed.',
 '2025-10-05 14:10:00'),

(@pid, @doc2, 'Urine Culture',
 'E. coli  |  Colony Count: over 100000 CFU/mL  |  Ciprofloxacin: SENSITIVE',
 'Positive — E. coli UTI confirmed. Organism sensitive to prescribed antibiotic. Complete full course.',
 '2025-10-07 11:00:00');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc1, 'COVID-19 PCR Test',
 'NEGATIVE',
 'Negative — No SARS-CoV-2 detected. Patient cleared for travel.',
 '2025-11-02 08:30:00');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc1, 'Blood Sugar (Glucose)',
 'Fasting: 126 mg/dL  |  Post-meal: 168 mg/dL  |  HbA1c: 7.2%',
 'High — IMPROVING. Down from initial 198/287. Metformin increased to 1000mg twice daily. Patient commended for diet and exercise compliance.',
 '2025-12-18 10:00:00'),

(@pid, @doc1, 'Cholesterol',
 'Total: 196 mg/dL  |  LDL: 112 mg/dL  |  HDL: 44 mg/dL  |  Triglycerides: 154 mg/dL',
 'Normal — EXCELLENT IMPROVEMENT from 248 mg/dL. Continue Atorvastatin 20mg. Next lipid panel in 6 months.',
 '2025-12-18 10:15:00'),

(@pid, @doc1, 'Blood Pressure Check',
 '128/82 mmHg',
 'Normal — Improved from 148/94. Continue Amlodipine 5mg. Monthly home BP monitoring advised.',
 '2025-12-18 10:20:00'),

(@pid, @doc1, 'Hemoglobin',
 'Hb: 13.1 g/dL',
 'Normal — Anemia fully resolved from 11.2 g/dL. Discontinue iron supplements. Maintain iron-rich diet.',
 '2025-12-18 10:30:00');


INSERT INTO lab_result (pid, docid, test_name, result, notes, created_at) VALUES
(@pid, @doc1, 'CBC - Complete Blood Count',
 'WBC: 6.2 K/uL  |  RBC: 4.9 M/uL  |  Platelets: 245 K/uL',
 'Normal — All blood count values within normal range. No signs of infection. Patient in stable condition.',
 '2026-02-10 09:00:00'),

(@pid, @doc1, 'Vitamin D',
 '34 ng/mL',
 'Normal — Corrected from 14 to 34 ng/mL. Reduce to maintenance dose 2000 IU per day.',
 '2026-02-10 09:10:00'),

(@pid, @doc1, 'Kidney Function Test',
 'Creatinine: 0.9 mg/dL  |  BUN: 14 mg/dL  |  eGFR: 92 mL/min',
 'Normal — Kidney function excellent. eGFR 92 is normal. Annual monitoring recommended.',
 '2026-02-10 09:20:00'),

(@pid, @doc1, 'Liver Function Test',
 'ALT: 28 U/L  |  AST: 24 U/L  |  ALP: 76 U/L  |  Albumin: 4.2 g/dL',
 'Normal — Liver function normal. No side effects from long-term Atorvastatin or Metformin.',
 '2026-02-10 09:30:00'),

(@pid, @doc1, 'Iron Level',
 'Serum Iron: 88 mcg/dL  |  Ferritin: 62 ng/mL  |  TIBC: 310 mcg/dL',
 'Normal — Iron stores fully replenished. No supplementation required.',
 '2026-02-10 09:40:00');

SET SQL_SAFE_UPDATES   = 1;
SET FOREIGN_KEY_CHECKS = 1;


SELECT pid, pname, pemail, pdob, ptel FROM patient WHERE pemail = 'demo@hms.com';

SELECT a.appodate, a.status, d.docname
FROM appointment a JOIN doctor d ON a.scheduleid = d.docid
WHERE a.pid = @pid ORDER BY a.appodate;

SELECT COUNT(*) AS total_lab_results FROM lab_result WHERE pid = @pid;
