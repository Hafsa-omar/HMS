USE hospital_management;
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS patient_documents (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    pid           INT NOT NULL,
    original_name VARCHAR(255) NOT NULL,
    stored_name   VARCHAR(255) NOT NULL,
    file_type     VARCHAR(50)  NOT NULL,
    file_size     INT          NOT NULL,
    uploaded_at   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pid) REFERENCES patient(pid) ON DELETE CASCADE
);

SET FOREIGN_KEY_CHECKS = 1;
