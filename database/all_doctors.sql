-- =============================================
-- HMS Comprehensive Doctor Directory
-- 15 Countries | 30+ Cities | 50+ Hospitals | All 56 Specialties
-- =============================================
USE hospital_management;
SET NAMES utf8mb4;
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

-- Clear existing doctors and their webuser entries
DELETE FROM appointment;
DELETE FROM webuser WHERE usertype = 'd';
DELETE FROM doctor;
ALTER TABLE doctor AUTO_INCREMENT = 1;

INSERT INTO doctor (docname, docemail, docpassword, docnic, doctel, specialties, country, city, hospital_branch, hospital_type, consultation_fee, available, rating, review_count) VALUES

-- =============================================
-- TURKEY - Ankara
-- =============================================
('Dr. Ahmet Yılmaz',       'ahmet.yilmaz@hms.com',       '123', 'TR-ANK-001', '+90-312-3051000', 5,  'Turkey', 'Ankara', 'Hacettepe University Hospital',      'public',  60,  1, 4.8, 45),
('Dr. Fatma Kaya',         'fatma.kaya@hms.com',          '123', 'TR-ANK-002', '+90-312-3051001', 29, 'Turkey', 'Ankara', 'Hacettepe University Hospital',      'public',  60,  1, 4.7, 38),
('Dr. Mehmet Demir',       'mehmet.demir@hms.com',        '123', 'TR-ANK-003', '+90-312-5085000', 19, 'Turkey', 'Ankara', 'Ankara City Hospital',               'public',  50,  1, 4.6, 32),
('Dr. Ayşe Çelik',         'ayse.celik@hms.com',          '123', 'TR-ANK-004', '+90-312-5085001', 35, 'Turkey', 'Ankara', 'Ankara City Hospital',               'public',  50,  1, 4.5, 28),
('Dr. Mustafa Şahin',      'mustafa.sahin@hms.com',       '123', 'TR-ANK-005', '+90-312-4681000', 13, 'Turkey', 'Ankara', 'Güven Hospital',                     'private', 80,  1, 4.9, 60),
('Dr. Zeynep Arslan',      'zeynep.arslan@hms.com',       '123', 'TR-ANK-006', '+90-312-4681001', 14, 'Turkey', 'Ankara', 'Güven Hospital',                     'private', 80,  1, 4.7, 42),
('Dr. İbrahim Koç',        'ibrahim.koc@hms.com',         '123', 'TR-ANK-007', '+90-312-4283000', 32, 'Turkey', 'Ankara', 'Bayındır Kavaklıdere Hospital',       'private', 90,  1, 4.8, 55),
('Dr. Elif Yıldız',        'elif.yildiz@hms.com',         '123', 'TR-ANK-008', '+90-312-4283001', 38, 'Turkey', 'Ankara', 'Bayındır Kavaklıdere Hospital',       'private', 90,  1, 4.6, 35),

-- =============================================
-- TURKEY - Istanbul
-- =============================================
('Dr. Hasan Erdoğan',      'hasan.erdogan@hms.com',       '123', 'TR-IST-001', '+90-212-4140000', 27, 'Turkey', 'Istanbul', 'Istanbul University-Cerrahpaşa Hospital', 'public',  55,  1, 4.7, 48),
('Dr. Selin Öztürk',       'selin.ozturk@hms.com',        '123', 'TR-IST-002', '+90-212-4140001', 54, 'Turkey', 'Istanbul', 'Istanbul University-Cerrahpaşa Hospital', 'public',  55,  1, 4.5, 30),
('Dr. Burak Aydın',        'burak.aydin@hms.com',         '123', 'TR-IST-003', '+90-212-3040000', 42, 'Turkey', 'Istanbul', 'Acıbadem Maslak Hospital',               'private', 120, 1, 4.9, 72),
('Dr. Neslihan Doğan',     'neslihan.dogan@hms.com',      '123', 'TR-IST-004', '+90-212-3040001', 55, 'Turkey', 'Istanbul', 'Acıbadem Maslak Hospital',               'private', 120, 1, 4.8, 58),
('Dr. Tarık Yılmaz',       'tarik.yilmaz2@hms.com',       '123', 'TR-IST-005', '+90-212-2246000', 30, 'Turkey', 'Istanbul', 'Florence Nightingale Hospital',           'private', 110, 1, 4.7, 44),
('Dr. Canan Kaya',         'canan.kaya@hms.com',          '123', 'TR-IST-006', '+90-212-2246001', 28, 'Turkey', 'Istanbul', 'Florence Nightingale Hospital',           'private', 110, 1, 4.6, 36),
('Dr. Okan Çelik',         'okan.celik@hms.com',          '123', 'TR-IST-007', '+90-212-3114000', 2,  'Turkey', 'Istanbul', 'American Hospital Istanbul',              'private', 130, 1, 4.8, 50),
('Dr. Deniz Şahin',        'deniz.sahin@hms.com',         '123', 'TR-IST-008', '+90-212-3114001', 18, 'Turkey', 'Istanbul', 'American Hospital Istanbul',              'private', 130, 1, 4.9, 65),

-- =============================================
-- TURKEY - Izmir
-- =============================================
('Dr. Kemal Arslan',       'kemal.arslan@hms.com',        '123', 'TR-IZM-001', '+90-232-3901000', 22, 'Turkey', 'Izmir', 'Ege University Hospital', 'public',  45, 1, 4.6, 28),
('Dr. Pınar Koç',          'pinar.koc@hms.com',           '123', 'TR-IZM-002', '+90-232-3901001', 21, 'Turkey', 'Izmir', 'Ege University Hospital', 'public',  45, 1, 4.5, 22),
('Dr. Serkan Yıldız',      'serkan.yildiz@hms.com',       '123', 'TR-IZM-003', '+90-232-4840000', 3,  'Turkey', 'Izmir', 'Kent Hospital',           'private', 75, 1, 4.7, 40),
('Dr. Gül Erdoğan',        'gul.erdogan@hms.com',         '123', 'TR-IZM-004', '+90-232-4840001', 10, 'Turkey', 'Izmir', 'Kent Hospital',           'private', 75, 1, 4.8, 35),

-- =============================================
-- UAE - Dubai
-- =============================================
('Dr. Mohammed Al-Rashid',  'mohammed.alrashid@hms.com',  '123', 'UAE-DXB-001', '+971-4-2194000', 1,  'UAE', 'Dubai', 'Dubai Hospital',             'public',  150, 1, 4.6, 42),
('Dr. Fatima Al-Mazrouei',  'fatima.almazrouei@hms.com',  '123', 'UAE-DXB-002', '+971-4-2194001', 37, 'UAE', 'Dubai', 'Dubai Hospital',             'public',  150, 1, 4.5, 35),
('Dr. David Williams',      'david.williams@hms.com',     '123', 'UAE-DXB-003', '+971-4-3364000', 5,  'UAE', 'Dubai', 'American Hospital Dubai',    'private', 280, 1, 4.9, 88),
('Dr. Sarah Thompson',      'sarah.thompson@hms.com',     '123', 'UAE-DXB-004', '+971-4-3364001', 42, 'UAE', 'Dubai', 'American Hospital Dubai',    'private', 280, 1, 4.8, 72),
('Dr. Rajiv Sharma',        'rajiv.sharma@hms.com',       '123', 'UAE-DXB-005', '+971-4-4354000', 29, 'UAE', 'Dubai', 'Mediclinic City Hospital',   'private', 250, 1, 4.7, 55),
('Dr. Priya Patel',         'priya.patel@hms.com',        '123', 'UAE-DXB-006', '+971-4-4354001', 35, 'UAE', 'Dubai', 'Mediclinic City Hospital',   'private', 250, 1, 4.8, 62),
('Dr. John Harrison',       'john.harrison@hms.com',      '123', 'UAE-DXB-007', '+971-4-3624000', 16, 'UAE', 'Dubai', 'Kings College Hospital Dubai','private', 300, 1, 4.9, 95),
('Dr. Aisha Al-Blooshi',    'aisha.alblooshi@hms.com',    '123', 'UAE-DXB-008', '+971-4-3624001', 27, 'UAE', 'Dubai', 'Kings College Hospital Dubai','private', 300, 1, 4.8, 78),
('Dr. Nadia Hassan',        'nadia.hassan@hms.com',       '123', 'UAE-DXB-009', '+971-4-3624002', 11, 'UAE', 'Dubai', 'Kings College Hospital Dubai','private', 300, 1, 4.7, 60),

-- =============================================
-- UAE - Abu Dhabi
-- =============================================
('Dr. Hamad Al-Mansoori',   'hamad.almansoori@hms.com',   '123', 'UAE-AUH-001', '+971-2-6191000', 49, 'UAE', 'Abu Dhabi', 'Sheikh Khalifa Medical City',   'public',  160, 1, 4.6, 44),
('Dr. Mariam Al-Zaabi',     'mariam.alzaabi@hms.com',     '123', 'UAE-AUH-002', '+971-2-6191001', 36, 'UAE', 'Abu Dhabi', 'Sheikh Khalifa Medical City',   'public',  160, 1, 4.5, 38),
('Dr. James Mitchell',      'james.mitchell@hms.com',     '123', 'UAE-AUH-003', '+971-2-5084000', 50, 'UAE', 'Abu Dhabi', 'Burjeel Hospital Abu Dhabi',     'private', 270, 1, 4.8, 68),
('Dr. Elena Petrova',       'elena.petrova@hms.com',      '123', 'UAE-AUH-004', '+971-2-5084001', 34, 'UAE', 'Abu Dhabi', 'Burjeel Hospital Abu Dhabi',     'private', 270, 1, 4.7, 52),
('Dr. Michael Chen',        'michael.chen@hms.com',       '123', 'UAE-AUH-005', '+971-2-6598000', 30, 'UAE', 'Abu Dhabi', 'Cleveland Clinic Abu Dhabi',     'private', 350, 1, 4.9, 110),
('Dr. Laura Anderson',      'laura.anderson@hms.com',     '123', 'UAE-AUH-006', '+971-2-6598001', 54, 'UAE', 'Abu Dhabi', 'Cleveland Clinic Abu Dhabi',     'private', 350, 1, 4.9, 98),

-- =============================================
-- UK - London
-- =============================================
('Dr. William Clarke',      'william.clarke@hms.com',     '123', 'UK-LON-001', '+44-20-32999000', 17, 'UK', 'London', 'Kings College Hospital',      'public',  120, 1, 4.8, 65),
('Dr. Emma Watson',         'emma.watson@hms.com',        '123', 'UK-LON-002', '+44-20-32999001', 5,  'UK', 'London', 'Kings College Hospital',      'public',  120, 1, 4.9, 82),
('Dr. Oliver Smith',        'oliver.smith@hms.com',       '123', 'UK-LON-003', '+44-20-71884000', 49, 'UK', 'London', 'St Thomas Hospital',          'public',  110, 1, 4.7, 55),
('Dr. Charlotte Brown',     'charlotte.brown@hms.com',    '123', 'UK-LON-004', '+44-20-71884001', 1,  'UK', 'London', 'St Thomas Hospital',          'public',  110, 1, 4.6, 44),
('Dr. George Taylor',       'george.taylor@hms.com',      '123', 'UK-LON-005', '+44-20-74073100', 35, 'UK', 'London', 'London Bridge Hospital',      'private', 200, 1, 4.9, 90),
('Dr. Isabella Wilson',     'isabella.wilson@hms.com',    '123', 'UK-LON-006', '+44-20-74073101', 41, 'UK', 'London', 'London Bridge Hospital',      'private', 200, 1, 4.8, 74),
('Dr. Henry Johnson',       'henry.johnson@hms.com',      '123', 'UK-LON-007', '+44-20-75800100', 32, 'UK', 'London', 'Portland Hospital London',    'private', 220, 1, 4.8, 68),
('Dr. Sophie Davies',       'sophie.davies@hms.com',      '123', 'UK-LON-008', '+44-20-75800101', 38, 'UK', 'London', 'Portland Hospital London',    'private', 220, 1, 4.9, 85),
('Dr. Arthur Bennett',      'arthur.bennett@hms.com',     '123', 'UK-LON-009', '+44-20-75800102', 44, 'UK', 'London', 'Portland Hospital London',    'private', 220, 1, 4.7, 50),
('Dr. Victoria Hughes',     'victoria.hughes@hms.com',    '123', 'UK-LON-010', '+44-20-32999002', 4,  'UK', 'London', 'Kings College Hospital',      'public',  120, 1, 4.7, 48),

-- =============================================
-- UK - Manchester
-- =============================================
('Dr. Thomas Evans',        'thomas.evans@hms.com',       '123', 'UK-MAN-001', '+44-161-2762000', 29, 'UK', 'Manchester', 'Manchester Royal Infirmary',   'public',  115, 1, 4.6, 48),
('Dr. Lucy Roberts',        'lucy.roberts@hms.com',       '123', 'UK-MAN-002', '+44-161-2762001', 9,  'UK', 'Manchester', 'Manchester Royal Infirmary',   'public',  115, 1, 4.7, 40),
('Dr. Jack Phillips',       'jack.phillips@hms.com',      '123', 'UK-MAN-003', '+44-161-4478000', 42, 'UK', 'Manchester', 'Spire Manchester Hospital',    'private', 185, 1, 4.8, 58),
('Dr. Grace Turner',        'grace.turner@hms.com',       '123', 'UK-MAN-004', '+44-161-4478001', 13, 'UK', 'Manchester', 'Spire Manchester Hospital',    'private', 185, 1, 4.7, 45),

-- =============================================
-- UK - Birmingham
-- =============================================
('Dr. Samuel Morris',       'samuel.morris@hms.com',      '123', 'UK-BHM-001', '+44-121-6272000', 20, 'UK', 'Birmingham', 'Queen Elizabeth Hospital Birmingham', 'public',  110, 1, 4.7, 42),
('Dr. Hannah Cooper',       'hannah.cooper@hms.com',      '123', 'UK-BHM-002', '+44-121-4401000', 46, 'UK', 'Birmingham', 'Spire Birmingham Hospital',          'private', 180, 1, 4.8, 55),

-- =============================================
-- USA - New York
-- =============================================
('Dr. Robert Martinez',     'robert.martinez@hms.com',    '123', 'USA-NY-001', '+1-212-7463000', 5,  'USA', 'New York', 'NewYork-Presbyterian Hospital', 'public',  250, 1, 4.9, 120),
('Dr. Jennifer Garcia',     'jennifer.garcia@hms.com',    '123', 'USA-NY-002', '+1-212-7463001', 30, 'USA', 'New York', 'NewYork-Presbyterian Hospital', 'public',  250, 1, 4.8, 95),
('Dr. Christopher Lee',     'christopher.lee@hms.com',    '123', 'USA-NY-003', '+1-212-2418500', 16, 'USA', 'New York', 'Mount Sinai Hospital New York', 'private', 320, 1, 4.9, 140),
('Dr. Amanda White',        'amanda.white@hms.com',       '123', 'USA-NY-004', '+1-212-2418501', 14, 'USA', 'New York', 'Mount Sinai Hospital New York', 'private', 320, 1, 4.8, 108),
('Dr. Daniel Harris',       'daniel.harris@hms.com',      '123', 'USA-NY-005', '+1-212-4348000', 35, 'USA', 'New York', 'Lenox Hill Hospital',          'private', 300, 1, 4.8, 88),
('Dr. Jessica Lewis',       'jessica.lewis@hms.com',      '123', 'USA-NY-006', '+1-646-7548000', 45, 'USA', 'New York', 'NYU Langone Health',            'private', 340, 1, 4.9, 115),
('Dr. Brian Walker',        'brian.walker@hms.com',       '123', 'USA-NY-007', '+1-646-7548001', 6,  'USA', 'New York', 'NYU Langone Health',            'private', 340, 1, 4.8, 90),
('Dr. Monica Torres',       'monica.torres@hms.com',      '123', 'USA-NY-008', '+1-212-4348001', 43, 'USA', 'New York', 'Lenox Hill Hospital',          'private', 300, 1, 4.7, 65),

-- =============================================
-- USA - Los Angeles
-- =============================================
('Dr. Kevin Thompson',      'kevin.thompson@hms.com',     '123', 'USA-LA-001', '+1-310-8254321', 47, 'USA', 'Los Angeles', 'UCLA Medical Center',          'public',  280, 1, 4.8, 98),
('Dr. Michelle Robinson',   'michelle.robinson@hms.com',  '123', 'USA-LA-002', '+1-310-4230431', 29, 'USA', 'Los Angeles', 'Cedars-Sinai Medical Center',  'private', 380, 1, 4.9, 155),
('Dr. Steven Wright',       'steven.wright@hms.com',      '123', 'USA-LA-003', '+1-310-4230432', 13, 'USA', 'Los Angeles', 'Cedars-Sinai Medical Center',  'private', 380, 1, 4.8, 122),
('Dr. Nancy Adams',         'nancy.adams@hms.com',        '123', 'USA-LA-004', '+1-310-8254322', 48, 'USA', 'Los Angeles', 'UCLA Medical Center',          'public',  280, 1, 4.7, 78),

-- =============================================
-- USA - Houston
-- =============================================
('Dr. Andrew Hall',         'andrew.hall@hms.com',        '123', 'USA-HOU-001', '+1-713-7904000', 5,  'USA', 'Houston', 'Houston Methodist Hospital', 'private', 350, 1, 4.9, 132),
('Dr. Patricia Young',      'patricia.young@hms.com',     '123', 'USA-HOU-002', '+1-713-7904001', 55, 'USA', 'Houston', 'Houston Methodist Hospital', 'private', 350, 1, 4.8, 105),
('Dr. Ryan Allen',          'ryan.allen@hms.com',         '123', 'USA-HOU-003', '+1-713-7044000', 1,  'USA', 'Houston', 'Memorial Hermann Hospital',  'public',  260, 1, 4.7, 78),
('Dr. Karen Nelson',        'karen.nelson@hms.com',       '123', 'USA-HOU-004', '+1-713-7904002', 15, 'USA', 'Houston', 'Houston Methodist Hospital', 'private', 350, 1, 4.8, 88),

-- =============================================
-- USA - Chicago
-- =============================================
('Dr. Lisa King',           'lisa.king@hms.com',          '123', 'USA-CHI-001', '+1-312-9262000', 18, 'USA', 'Chicago', 'Northwestern Memorial Hospital', 'public',  270, 1, 4.7, 88),
('Dr. Mark Scott',          'mark.scott@hms.com',         '123', 'USA-CHI-002', '+1-312-9426000', 50, 'USA', 'Chicago', 'Rush University Medical Center', 'private', 310, 1, 4.8, 96),
('Dr. Paul Carter',         'paul.carter@hms.com',        '123', 'USA-CHI-003', '+1-312-9426001', 39, 'USA', 'Chicago', 'Rush University Medical Center', 'private', 310, 1, 4.7, 72),

-- =============================================
-- GERMANY - Berlin
-- =============================================
('Dr. Hans Müller',         'hans.muller@hms.com',        '123', 'DE-BER-001', '+49-30-450500', 29, 'Germany', 'Berlin', 'Charité University Hospital',           'public',  90,  1, 4.8, 72),
('Dr. Petra Schmidt',       'petra.schmidt@hms.com',      '123', 'DE-BER-002', '+49-30-450501', 5,  'Germany', 'Berlin', 'Charité University Hospital',           'public',  90,  1, 4.9, 85),
('Dr. Klaus Weber',         'Klaus.weber@hms.com',        '123', 'DE-BER-003', '+49-30-8102000', 22, 'Germany', 'Berlin', 'Helios Klinikum Emil von Behring',     'private', 130, 1, 4.7, 48),
('Dr. Ingrid Fischer',      'ingrid.fischer@hms.com',     '123', 'DE-BER-004', '+49-30-8102001', 49, 'Germany', 'Berlin', 'Helios Klinikum Emil von Behring',     'private', 130, 1, 4.6, 38),
('Dr. Werner Braun',        'werner.braun@hms.com',       '123', 'DE-BER-005', '+49-30-450502', 8,  'Germany', 'Berlin', 'Charité University Hospital',           'public',  90,  1, 4.7, 55),

-- =============================================
-- GERMANY - Munich
-- =============================================
('Dr. Friedrich Wagner',    'friedrich.wagner@hms.com',   '123', 'DE-MUN-001', '+49-89-440001', 16, 'Germany', 'Munich', 'LMU Klinikum München',                'public',  95,  1, 4.8, 65),
('Dr. Katharina Bauer',     'katharina.bauer@hms.com',    '123', 'DE-MUN-002', '+49-89-440002', 14, 'Germany', 'Munich', 'LMU Klinikum München',                'public',  95,  1, 4.7, 52),
('Dr. Wolfgang Richter',    'wolfgang.richter@hms.com',   '123', 'DE-MUN-003', '+49-89-6809000', 35, 'Germany', 'Munich', 'Schön Klinik München Harlaching',     'private', 150, 1, 4.9, 88),
('Dr. Erika Hoffmann',      'erika.hoffmann@hms.com',     '123', 'DE-MUN-004', '+49-89-440003', 33, 'Germany', 'Munich', 'LMU Klinikum München',                'public',  95,  1, 4.6, 40),

-- =============================================
-- GERMANY - Hamburg
-- =============================================
('Dr. Gerhard Klein',       'gerhard.klein@hms.com',      '123', 'DE-HAM-001', '+49-40-741053000', 12, 'Germany', 'Hamburg', 'UKE Hamburg',            'public',  85,  1, 4.7, 44),
('Dr. Ursula Schulz',       'ursula.schulz@hms.com',      '123', 'DE-HAM-002', '+49-40-1818811000', 55, 'Germany', 'Hamburg', 'Asklepios Klinik Altona','private', 125, 1, 4.6, 36),
('Dr. Dieter Zimmermann',   'dieter.zimmermann@hms.com',  '123', 'DE-HAM-003', '+49-40-741053001', 56, 'Germany', 'Hamburg', 'UKE Hamburg',            'public',  85,  1, 4.5, 30),

-- =============================================
-- FRANCE - Paris
-- =============================================
('Dr. Pierre Dupont',       'pierre.dupont@hms.com',      '123', 'FR-PAR-001', '+33-1-42161000', 29, 'France', 'Paris', 'Hôpital Pitié-Salpêtrière',         'public',  80,  1, 4.8, 60),
('Dr. Marie Laurent',       'marie.laurent@hms.com',      '123', 'FR-PAR-002', '+33-1-42161001', 45, 'France', 'Paris', 'Hôpital Pitié-Salpêtrière',         'public',  80,  1, 4.7, 48),
('Dr. Jean-François Moreau','jf.moreau@hms.com',          '123', 'FR-PAR-003', '+33-1-44494000', 38, 'France', 'Paris', 'Hôpital Necker',                    'public',  75,  1, 4.7, 52),
('Dr. Sophie Bernard',      'sophie.bernard@hms.com',     '123', 'FR-PAR-004', '+33-1-44494001', 21, 'France', 'Paris', 'Hôpital Necker',                    'public',  75,  1, 4.6, 40),
('Dr. Antoine Girard',      'antoine.girard@hms.com',     '123', 'FR-PAR-005', '+33-1-43290000', 42, 'France', 'Paris', 'Clinique Geoffroy Saint-Hilaire',   'private', 140, 1, 4.9, 75),
('Dr. Isabelle Rousseau',   'isabelle.rousseau@hms.com',  '123', 'FR-PAR-006', '+33-1-43290001', 7,  'France', 'Paris', 'Clinique Geoffroy Saint-Hilaire',   'private', 140, 1, 4.8, 62),
('Dr. Luc Fontaine',        'luc.fontaine@hms.com',       '123', 'FR-PAR-007', '+33-1-42161002', 51, 'France', 'Paris', 'Hôpital Pitié-Salpêtrière',         'public',  80,  1, 4.6, 42),

-- =============================================
-- SAUDI ARABIA - Riyadh
-- =============================================
('Dr. Abdullah Al-Otaibi',  'abdullah.alotaibi@hms.com',  '123', 'SA-RIY-001', '+966-11-4647272', 5,  'Saudi Arabia', 'Riyadh', 'King Faisal Specialist Hospital',    'public',  180, 1, 4.9, 95),
('Dr. Nora Al-Zahrani',     'nora.alzahrani@hms.com',     '123', 'SA-RIY-002', '+966-11-4647273', 19, 'Saudi Arabia', 'Riyadh', 'King Faisal Specialist Hospital',    'public',  180, 1, 4.8, 78),
('Dr. Khalid Al-Ghamdi',    'khalid.alghamdi@hms.com',    '123', 'SA-RIY-003', '+966-11-2900000', 18, 'Saudi Arabia', 'Riyadh', 'Dr. Sulaiman Al Habib Hospital',     'private', 220, 1, 4.8, 68),
('Dr. Reem Al-Shammari',    'reem.alshammari@hms.com',    '123', 'SA-RIY-004', '+966-11-2900001', 34, 'Saudi Arabia', 'Riyadh', 'Dr. Sulaiman Al Habib Hospital',     'private', 220, 1, 4.7, 55),
('Dr. Omar Al-Qahtani',     'omar.alqahtani@hms.com',     '123', 'SA-RIY-005', '+966-11-4600000', 25, 'Saudi Arabia', 'Riyadh', 'Saudi German Hospital Riyadh',       'private', 200, 1, 4.7, 48),
('Dr. Hessa Al-Mutairi',    'hessa.almutairi@hms.com',    '123', 'SA-RIY-006', '+966-11-4647274', 31, 'Saudi Arabia', 'Riyadh', 'King Faisal Specialist Hospital',    'public',  180, 1, 4.8, 62),

-- =============================================
-- SAUDI ARABIA - Jeddah
-- =============================================
('Dr. Faisal Al-Harbi',     'faisal.alharbi@hms.com',     '123', 'SA-JED-001', '+966-12-6408000', 27, 'Saudi Arabia', 'Jeddah', 'King Abdulaziz University Hospital', 'public',  160, 1, 4.7, 52),
('Dr. Hana Al-Dossari',     'hana.aldossari@hms.com',     '123', 'SA-JED-002', '+966-12-6408001', 14, 'Saudi Arabia', 'Jeddah', 'King Abdulaziz University Hospital', 'public',  160, 1, 4.6, 44),
('Dr. Youssef Al-Sayed',    'youssef.alsayed@hms.com',    '123', 'SA-JED-003', '+966-12-6653000', 54, 'Saudi Arabia', 'Jeddah', 'Dr. Soliman Fakeeh Hospital',        'private', 200, 1, 4.8, 62),

-- =============================================
-- JORDAN - Amman
-- =============================================
('Dr. Ziad Khalil',         'ziad.khalil@hms.com',        '123', 'JO-AMM-001', '+962-6-5351000', 5,  'Jordan', 'Amman', 'Jordan University Hospital', 'public',  70,  1, 4.7, 40),
('Dr. Lina Natour',         'lina.natour@hms.com',        '123', 'JO-AMM-002', '+962-6-5351001', 18, 'Jordan', 'Amman', 'Jordan University Hospital', 'public',  70,  1, 4.6, 32),
('Dr. Sami Al-Khatib',      'sami.alkhatib@hms.com',      '123', 'JO-AMM-003', '+962-6-4644281', 35, 'Jordan', 'Amman', 'Al-Khalidi Hospital',        'private', 100, 1, 4.8, 58),
('Dr. Rania Haddad',        'rania.haddad@hms.com',       '123', 'JO-AMM-004', '+962-6-4644282', 36, 'Jordan', 'Amman', 'Al-Khalidi Hospital',        'private', 100, 1, 4.7, 45),
('Dr. Basem Qasem',         'basem.qasem@hms.com',        '123', 'JO-AMM-005', '+962-6-5820000', 32, 'Jordan', 'Amman', 'Istishari Hospital',          'private', 90,  1, 4.8, 50),
('Dr. Dina Salameh',        'dina.salameh@hms.com',       '123', 'JO-AMM-006', '+962-6-5820001', 30, 'Jordan', 'Amman', 'Istishari Hospital',          'private', 90,  1, 4.7, 42),

-- =============================================
-- EGYPT - Cairo
-- =============================================
('Dr. Tarek Hassan',        'tarek.hassan@hms.com',       '123', 'EG-CAI-001', '+20-2-23688000', 22, 'Egypt', 'Cairo', 'Cairo University Hospital Kasr Al-Ainy', 'public',  35, 1, 4.6, 38),
('Dr. Samira Mostafa',      'samira.mostafa@hms.com',     '123', 'EG-CAI-002', '+20-2-23688001', 53, 'Egypt', 'Cairo', 'Cairo University Hospital Kasr Al-Ainy', 'public',  35, 1, 4.5, 30),
('Dr. Amr Fathy',           'amr.fathy@hms.com',          '123', 'EG-CAI-003', '+20-2-24140000', 32, 'Egypt', 'Cairo', 'Cleopatra Hospital Cairo',               'private', 60, 1, 4.7, 48),
('Dr. Mona Ibrahim',        'mona.ibrahim@hms.com',       '123', 'EG-CAI-004', '+20-2-24140001', 13, 'Egypt', 'Cairo', 'Cleopatra Hospital Cairo',               'private', 60, 1, 4.6, 38),
('Dr. Hossam El-Din',       'hossam.eldin@hms.com',       '123', 'EG-CAI-005', '+20-2-25248000', 5,  'Egypt', 'Cairo', 'As-Salam International Hospital',        'private', 70, 1, 4.8, 55),
('Dr. Rasha Abdel-Fattah',  'rasha.abdelfattah@hms.com',  '123', 'EG-CAI-006', '+20-2-25248001', 26, 'Egypt', 'Cairo', 'As-Salam International Hospital',        'private', 70, 1, 4.7, 45),

-- =============================================
-- EGYPT - Alexandria
-- =============================================
('Dr. Adel Fahmy',          'adel.fahmy@hms.com',         '123', 'EG-ALX-001', '+20-3-4833000', 29, 'Egypt', 'Alexandria', 'Alexandria University Hospital',   'public',  30, 1, 4.5, 28),
('Dr. Nevine Soliman',      'nevine.soliman@hms.com',     '123', 'EG-ALX-002', '+20-3-5840000', 54, 'Egypt', 'Alexandria', 'Smouha International Hospital',    'private', 55, 1, 4.6, 36),
('Dr. Khaled Mansour',      'khaled.mansour@hms.com',     '123', 'EG-ALX-003', '+20-3-4833001', 23, 'Egypt', 'Alexandria', 'Alexandria University Hospital',   'public',  30, 1, 4.5, 25),

-- =============================================
-- INDIA - Mumbai
-- =============================================
('Dr. Vikram Mehta',        'vikram.mehta@hms.com',       '123', 'IN-MUM-001', '+91-22-24177000', 47, 'India', 'Mumbai', 'Tata Memorial Hospital',                  'public',  25, 1, 4.8, 78),
('Dr. Anjali Singh',        'anjali.singh@hms.com',       '123', 'IN-MUM-002', '+91-22-30999999', 5,  'India', 'Mumbai', 'Kokilaben Dhirubhai Ambani Hospital',      'private', 50, 1, 4.9, 92),
('Dr. Suresh Nair',         'suresh.nair@hms.com',        '123', 'IN-MUM-003', '+91-22-30999998', 29, 'India', 'Mumbai', 'Kokilaben Dhirubhai Ambani Hospital',      'private', 50, 1, 4.7, 64),
('Dr. Priyanka Joshi',      'priyanka.joshi@hms.com',     '123', 'IN-MUM-004', '+91-22-36555000', 32, 'India', 'Mumbai', 'Breach Candy Hospital Mumbai',             'private', 45, 1, 4.7, 55),
('Dr. Rohan Desai',         'rohan.desai@hms.com',        '123', 'IN-MUM-005', '+91-22-24177001', 48, 'India', 'Mumbai', 'Tata Memorial Hospital',                  'public',  25, 1, 4.8, 70),
('Dr. Sneha Patil',         'sneha.patil@hms.com',        '123', 'IN-MUM-006', '+91-22-30999997', 24, 'India', 'Mumbai', 'Kokilaben Dhirubhai Ambani Hospital',      'private', 50, 1, 4.6, 48),

-- =============================================
-- INDIA - New Delhi
-- =============================================
('Dr. Anil Kumar',          'anil.kumar@hms.com',         '123', 'IN-DEL-001', '+91-11-26588500', 29, 'India', 'New Delhi', 'AIIMS New Delhi',                       'public',  20, 1, 4.9, 110),
('Dr. Sunita Gupta',        'sunita.gupta@hms.com',       '123', 'IN-DEL-002', '+91-11-26588501', 27, 'India', 'New Delhi', 'AIIMS New Delhi',                       'public',  20, 1, 4.8, 95),
('Dr. Ramesh Kapoor',       'ramesh.kapoor@hms.com',      '123', 'IN-DEL-003', '+91-124-4921000', 35, 'India', 'New Delhi', 'Fortis Memorial Research Institute',    'private', 45, 1, 4.8, 72),
('Dr. Kavita Sharma',       'kavita.sharma@hms.com',      '123', 'IN-DEL-004', '+91-11-26512000', 18, 'India', 'New Delhi', 'Max Super Speciality Hospital Delhi',   'private', 40, 1, 4.7, 58),
('Dr. Vikas Bansal',        'vikas.bansal@hms.com',       '123', 'IN-DEL-005', '+91-11-26588502', 40, 'India', 'New Delhi', 'AIIMS New Delhi',                       'public',  20, 1, 4.7, 62),

-- =============================================
-- INDIA - Bangalore
-- =============================================
('Dr. Narayan Rao',         'narayan.rao@hms.com',        '123', 'IN-BLR-001', '+91-80-22112000', 47, 'India', 'Bangalore', 'Manipal Hospital Bangalore', 'private', 42, 1, 4.8, 68),
('Dr. Deepa Krishnamurthy', 'deepa.krishnamurthy@hms.com','123', 'IN-BLR-002', '+91-80-22112001', 30, 'India', 'Bangalore', 'Manipal Hospital Bangalore', 'private', 42, 1, 4.7, 52),

-- =============================================
-- PAKISTAN - Karachi
-- =============================================
('Dr. Imran Ahmed',         'imran.ahmed@hms.com',        '123', 'PK-KHI-001', '+92-21-111911911', 5,  'Pakistan', 'Karachi', 'Aga Khan University Hospital', 'private', 30, 1, 4.8, 65),
('Dr. Zara Hussain',        'zara.hussain@hms.com',       '123', 'PK-KHI-002', '+92-21-111911912', 29, 'Pakistan', 'Karachi', 'Aga Khan University Hospital', 'private', 30, 1, 4.7, 52),
('Dr. Muhammad Tariq',      'muhammad.tariq@hms.com',     '123', 'PK-KHI-003', '+92-21-99215000',  19, 'Pakistan', 'Karachi', 'Civil Hospital Karachi',       'public',  15, 1, 4.4, 35),
('Dr. Fatima Malik',        'fatima.malik@hms.com',       '123', 'PK-KHI-004', '+92-21-35148000',  54, 'Pakistan', 'Karachi', 'Liaquat National Hospital',    'private', 25, 1, 4.6, 44),

-- =============================================
-- PAKISTAN - Lahore
-- =============================================
('Dr. Asif Khan',           'asif.khan@hms.com',          '123', 'PK-LAH-001', '+92-42-111556000', 47, 'Pakistan', 'Lahore', 'Shaukat Khanum Cancer Hospital', 'private', 28, 1, 4.9, 80),
('Dr. Nadia Siddiqui',      'nadia.siddiqui@hms.com',     '123', 'PK-LAH-002', '+92-42-99203000',  18, 'Pakistan', 'Lahore', 'Services Hospital Lahore',       'public',  12, 1, 4.5, 38),
('Dr. Hassan Raza',         'hassan.raza@hms.com',        '123', 'PK-LAH-003', '+92-42-35761000',  5,  'Pakistan', 'Lahore', 'Ittefaq Hospital Lahore',        'private', 22, 1, 4.7, 55),

-- =============================================
-- CANADA - Toronto
-- =============================================
('Dr. Nathan Brooks',       'nathan.brooks@hms.com',      '123', 'CA-TOR-001', '+1-416-3404800', 52, 'Canada', 'Toronto', 'Toronto General Hospital',       'public',  150, 1, 4.8, 68),
('Dr. Rachel Green',        'rachel.green@hms.com',       '123', 'CA-TOR-002', '+1-416-5865800', 32, 'Canada', 'Toronto', 'Mount Sinai Hospital Toronto',   'private', 200, 1, 4.8, 74),
('Dr. Cameron Price',       'cameron.price@hms.com',      '123', 'CA-TOR-003', '+1-416-3604000', 1,  'Canada', 'Toronto', 'St. Michaels Hospital Toronto',  'public',  160, 1, 4.7, 55),
('Dr. Olivia Martin',       'olivia.martin@hms.com',      '123', 'CA-TOR-004', '+1-416-3404801', 49, 'Canada', 'Toronto', 'Toronto General Hospital',       'public',  150, 1, 4.7, 60),

-- =============================================
-- CANADA - Vancouver
-- =============================================
('Dr. Emily Foster',        'emily.foster@hms.com',       '123', 'CA-VAN-001', '+1-604-8754111', 5,  'Canada', 'Vancouver', 'Vancouver General Hospital', 'public', 145, 1, 4.8, 62),
('Dr. Lucas Chen',          'lucas.chen@hms.com',         '123', 'CA-VAN-002', '+1-604-8754112', 19, 'Canada', 'Vancouver', 'Vancouver General Hospital', 'public', 145, 1, 4.7, 50),

-- =============================================
-- AUSTRALIA - Sydney
-- =============================================
('Dr. Thomas Hughes',       'thomas.hughes@hms.com',      '123', 'AU-SYD-001', '+61-2-95156111', 5,  'Australia', 'Sydney', 'Royal Prince Alfred Hospital', 'public',  130, 1, 4.8, 72),
('Dr. Megan OBrien',        'megan.obrien@hms.com',       '123', 'AU-SYD-002', '+61-2-83824000', 22, 'Australia', 'Sydney', 'St Vincents Hospital Sydney',  'public',  125, 1, 4.7, 58),
('Dr. James Cooper',        'james.cooper@hms.com',       '123', 'AU-SYD-003', '+61-2-92872900', 42, 'Australia', 'Sydney', 'Sydney Private Hospital',      'private', 200, 1, 4.8, 65),

-- =============================================
-- AUSTRALIA - Melbourne
-- =============================================
('Dr. Sarah McDonald',      'sarah.mcdonald@hms.com',     '123', 'AU-MEL-001', '+61-3-93427000', 29, 'Australia', 'Melbourne', 'Royal Melbourne Hospital', 'public',  125, 1, 4.8, 68),
('Dr. Patrick Kelly',       'patrick.kelly@hms.com',      '123', 'AU-MEL-002', '+61-3-94262000', 35, 'Australia', 'Melbourne', 'Epworth Hospital',         'private', 195, 1, 4.9, 85),
('Dr. Catherine Walsh',     'catherine.walsh@hms.com',    '123', 'AU-MEL-003', '+61-3-94262001', 16, 'Australia', 'Melbourne', 'Epworth Hospital',         'private', 195, 1, 4.7, 62),
('Dr. Daniel Murphy',       'daniel.murphy@hms.com',      '123', 'AU-MEL-004', '+61-3-93427001', 20, 'Australia', 'Melbourne', 'Royal Melbourne Hospital', 'public',  125, 1, 4.7, 50),

-- =============================================
-- JAPAN - Tokyo
-- =============================================
('Dr. Hiroshi Tanaka',      'hiroshi.tanaka@hms.com',     '123', 'JP-TKY-001', '+81-3-58008000', 47, 'Japan', 'Tokyo', 'The University of Tokyo Hospital', 'public',  100, 1, 4.8, 70),
('Dr. Yuki Yamamoto',       'yuki.yamamoto@hms.com',      '123', 'JP-TKY-002', '+81-3-35417151', 18, 'Japan', 'Tokyo', 'St. Lukes International Hospital', 'private', 150, 1, 4.9, 88),
('Dr. Kenji Suzuki',        'kenji.suzuki@hms.com',       '123', 'JP-TKY-003', '+81-3-33531211', 5,  'Japan', 'Tokyo', 'Keio University Hospital',         'private', 140, 1, 4.8, 75),
('Dr. Akiko Watanabe',      'akiko.watanabe@hms.com',     '123', 'JP-TKY-004', '+81-3-33531212', 34, 'Japan', 'Tokyo', 'Keio University Hospital',         'private', 140, 1, 4.7, 62),

-- =============================================
-- SOUTH KOREA - Seoul
-- =============================================
('Dr. Ji-Young Park',       'jiyoung.park@hms.com',       '123', 'KR-SEO-001', '+82-2-20722114', 5,  'South Korea', 'Seoul', 'Seoul National University Hospital', 'public',  90,  1, 4.9, 95),
('Dr. Sung-Min Kim',        'sungmin.kim@hms.com',        '123', 'KR-SEO-002', '+82-2-34100200', 30, 'South Korea', 'Seoul', 'Samsung Medical Center',             'private', 160, 1, 4.9, 110),
('Dr. Min-Joo Lee',         'minjoo.lee@hms.com',         '123', 'KR-SEO-003', '+82-2-30101114', 16, 'South Korea', 'Seoul', 'Asan Medical Center',                'private', 155, 1, 4.8, 88),
('Dr. Hyun-Ji Choi',        'hyunji.choi@hms.com',        '123', 'KR-SEO-004', '+82-2-30101115', 14, 'South Korea', 'Seoul', 'Asan Medical Center',                'private', 155, 1, 4.8, 75),

-- =============================================
-- REMAINING SPECIALTIES COVERAGE
-- (one doctor per specialty not yet assigned)
-- =============================================

-- Specialty 17: General hematology — already covered (UK Kings)
-- Specialty 23: Internal medicine
('Dr. Carlos Vega',         'carlos.vega@hms.com',        '123', 'MX-MEX-001', '+52-55-50620000', 23, 'Mexico', 'Mexico City', 'Hospital General de Mexico',          'public',  40,  1, 4.6, 44),
-- Specialty 24: Laboratory medicine
('Dr. Amelia Stone',        'amelia.stone@hms.com',       '123', 'AU-SYD-004', '+61-2-95156112', 24, 'Australia', 'Sydney', 'Royal Prince Alfred Hospital',          'public',  130, 1, 4.6, 35),
-- Specialty 26: Microbiology — already covered (Egypt Cairo)
-- Specialty 31: Nuclear medicine
('Dr. Yeon-Soo Jung',       'yeonsoo.jung@hms.com',       '123', 'KR-SEO-005', '+82-2-34100201', 31, 'South Korea', 'Seoul', 'Samsung Medical Center',                'private', 160, 1, 4.8, 62),
-- Specialty 39: Pathology — already covered (USA Chicago Rush)
-- Specialty 40: Pharmacology — already covered (India Delhi AIIMS)
-- Specialty 43: Podiatric Medicine — already covered (USA NY Lenox Hill)
-- Specialty 44: Podiatric Surgery — already covered (UK London Portland)
-- Specialty 46: Public health — already covered (UK Birmingham)
-- Specialty 48: Radiotherapy — covered India Mumbai Tata
-- Specialty 51: Stomatology — already covered (France Paris)
-- Specialty 56: Venereology — already covered (Germany Hamburg)

-- Extra coverage for specialties needing a second location:
-- Specialty 6: Child psychiatry
('Dr. Amina Al-Rashidi',    'amina.alrashidi@hms.com',    '123', 'SA-RIY-007', '+966-11-2900002', 6,  'Saudi Arabia', 'Riyadh', 'Dr. Sulaiman Al Habib Hospital',     'private', 220, 1, 4.8, 45),
-- Specialty 7: Clinical biology — already covered (France Paris)
-- Specialty 8: Clinical chemistry — already covered (Germany Berlin Charité)
-- Specialty 9: Clinical neurophysiology — already covered (UK Manchester)
-- Specialty 11: Dental oral maxillo-facial surgery — already covered (UAE Dubai)
-- Specialty 15: Gastro-enterologic surgery — already covered (USA Houston)
-- Specialty 25: Maxillo-facial surgery
('Dr. Layla Al-Farsi',      'layla.alfarsi@hms.com',      '123', 'UAE-DXB-010', '+971-4-2194002', 25, 'UAE', 'Dubai', 'Dubai Hospital',                             'public',  150, 1, 4.7, 38),
-- Specialty 28: Neuro-psychiatry — already covered (Turkey Istanbul Florence)
-- Specialty 33: Occupational medicine — already covered (Germany Munich)

-- Specialty 40: Pharmacology (extra)
('Dr. Yuki Nakamura',       'yuki.nakamura@hms.com',      '123', 'JP-TKY-005', '+81-3-33531213', 40, 'Japan', 'Tokyo', 'Keio University Hospital',                   'private', 140, 1, 4.7, 50);

-- =============================================
-- WEBUSER ENTRIES FOR ALL DOCTORS
-- =============================================
INSERT INTO webuser (email, usertype)
SELECT docemail, 'd' FROM doctor;

SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- =============================================
-- SUMMARY
-- =============================================
SELECT COUNT(*) AS total_doctors FROM doctor;
SELECT country, COUNT(*) AS doctors FROM doctor GROUP BY country ORDER BY doctors DESC;
SELECT s.sname, COUNT(d.docid) AS doctors FROM specialties s LEFT JOIN doctor d ON s.id = d.specialties GROUP BY s.id, s.sname ORDER BY doctors DESC;
