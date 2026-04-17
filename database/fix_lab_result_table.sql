-- ============================================================
-- FIX: Recreate lab_result table with correct column names
-- Run this ONCE in MySQL Workbench
-- ============================================================
USE hospital_management;
SET FOREIGN_KEY_CHECKS = 0;

-- Drop the old table (wrong schema)
DROP TABLE IF EXISTS lab_result;

-- Create with the correct columns that match the server code
CREATE TABLE lab_result (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    pid        INT NOT NULL,
    docid      INT NOT NULL,
    test_name  VARCHAR(200) NOT NULL,
    result     VARCHAR(500) NOT NULL,
    notes      TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SET FOREIGN_KEY_CHECKS = 1;

-- Confirm new structure
DESCRIBE lab_result;
