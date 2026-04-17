-- =============================================
-- HMS Book Appointment Features Migration
-- =============================================
USE hospital_management;
SET SQL_SAFE_UPDATES   = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- ─────────────────────────────────────────────
-- 1. ADD COLUMNS TO DOCTOR TABLE
--    Each line uses IF() + PREPARE so it never
--    errors — it simply skips if column exists
-- ─────────────────────────────────────────────

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='country');
SET @s = IF(@c=0, "ALTER TABLE doctor ADD COLUMN country VARCHAR(50) DEFAULT 'Turkey'", 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='city');
SET @s = IF(@c=0, "ALTER TABLE doctor ADD COLUMN city VARCHAR(50) DEFAULT 'Ankara'", 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='hospital_branch');
SET @s = IF(@c=0, "ALTER TABLE doctor ADD COLUMN hospital_branch VARCHAR(100) DEFAULT 'HMS Global'", 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='available');
SET @s = IF(@c=0, 'ALTER TABLE doctor ADD COLUMN available TINYINT(1) DEFAULT 1', 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='hospital_type');
SET @s = IF(@c=0, "ALTER TABLE doctor ADD COLUMN hospital_type VARCHAR(10) DEFAULT 'public'", 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='consultation_fee');
SET @s = IF(@c=0, 'ALTER TABLE doctor ADD COLUMN consultation_fee INT DEFAULT 50', 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='rating');
SET @s = IF(@c=0, 'ALTER TABLE doctor ADD COLUMN rating DECIMAL(2,1) DEFAULT 4.0', 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

SET @c = (SELECT COUNT(*) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='doctor' AND COLUMN_NAME='review_count');
SET @s = IF(@c=0, 'ALTER TABLE doctor ADD COLUMN review_count INT DEFAULT 0', 'SELECT 1'); PREPARE p FROM @s; EXECUTE p; DEALLOCATE PREPARE p;

-- ─────────────────────────────────────────────
-- 2. CREATE NEW TABLES (drop first to avoid 1050)
-- ─────────────────────────────────────────────

DROP TABLE IF EXISTS doctor_review;
CREATE TABLE doctor_review (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    pid         INT NOT NULL,
    docid       INT NOT NULL,
    rating      INT NOT NULL,
    review_text TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS health_sharing;
CREATE TABLE health_sharing (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    pid        INT NOT NULL,
    docid      INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_share (pid, docid)
);

-- ─────────────────────────────────────────────
-- 3. POPULATE DOCTOR DATA
-- ─────────────────────────────────────────────
UPDATE doctor SET country='Turkey', city='Ankara',   hospital_branch='HMS Ankara Central',  hospital_type='public',  consultation_fee=40,  available=1, rating=4.2, review_count=12;
UPDATE doctor SET country='Turkey', city='Istanbul', hospital_branch='HMS Istanbul Central', hospital_type='public',  consultation_fee=60,  available=1, rating=4.5, review_count=20 WHERE docid BETWEEN 4 AND 6;

SET SQL_SAFE_UPDATES   = 1;
SET FOREIGN_KEY_CHECKS = 1;

SELECT docid, docname, country, city, hospital_type, consultation_fee, rating FROM doctor LIMIT 10;
