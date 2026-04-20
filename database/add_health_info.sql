-- =============================================
-- Patient self-reported health information
-- Run once to add the table
-- =============================================
USE hospital_management;
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS patient_health_info (
    id                      INT AUTO_INCREMENT PRIMARY KEY,
    pid                     INT NOT NULL UNIQUE,
    blood_type              VARCHAR(5)   DEFAULT NULL,
    allergies               TEXT         DEFAULT NULL,
    chronic_conditions      TEXT         DEFAULT NULL,
    current_medications     TEXT         DEFAULT NULL,
    emergency_contact_name  VARCHAR(100) DEFAULT NULL,
    emergency_contact_phone VARCHAR(30)  DEFAULT NULL,
    notes                   TEXT         DEFAULT NULL,
    updated_at              TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (pid) REFERENCES patient(pid) ON DELETE CASCADE
);
SET FOREIGN_KEY_CHECKS = 1;
