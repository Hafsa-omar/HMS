# HMS — Hospital Management System

A full-stack web application for managing hospital appointments, patients, doctors, and lab results. Supports three user roles: **Patient**, **Doctor**, and **Admin**.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Node.js |
| Framework | Express.js |
| Database | MySQL (mysql2) |
| Auth | express-session |
| Frontend | Vanilla HTML / CSS / JavaScript |

---

## Project Structure

```
hospital-backend/
├── server.js               # Entry point — all routes & API
├── db.js                   # MySQL connection pool
├── .env                    # Environment variables
├── .env.example            # Env template
│
├── public/
│   ├── pages/              # HTML pages
│   ├── css/                # Stylesheets
│   ├── js/                 # Client-side scripts
│   └── assets/             # Images & media
│
└── database/               # SQL migration files
```

---

## Getting Started

### 1. Install dependencies

```bash
npm install
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=your_password
DB_NAME=hospital_management
```

### 3. Set up the database

Import the base schema first, then run migrations in order:

```bash
mysql -u root -p < database/hospital_management.sql
mysql -u root -p hospital_management < database/migrate_book_features.sql
mysql -u root -p hospital_management < database/add_doctors.sql
mysql -u root -p hospital_management < database/fix_lab_result_table.sql
mysql -u root -p hospital_management < database/demo_patient_record.sql
```

### 4. Start the server

```bash
node server.js
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## User Roles

### Patient
- Register and log in
- Browse and filter doctors by specialty, country, or city
- Book and cancel appointments
- View lab results
- View full health record
- Control health data sharing with doctors

### Doctor
- View assigned appointments and update their status
- View patient list
- Add lab results for patients
- Manage profile settings

### Admin
- View all patients and appointments system-wide
- Add or remove doctors
- Cancel any appointment
- Delete patient accounts

---

## API Overview

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Patient registration |
| POST | `/auth/login` | Login (all roles) |
| GET | `/logout` | Logout |
| GET | `/api/me` | Current user info |
| GET | `/api/doctors` | List available doctors |
| GET | `/api/specialties` | List specialties |
| POST | `/api/book` | Book an appointment |
| POST | `/api/appointments/cancel/:id` | Cancel appointment |
| GET | `/api/results` | Patient lab results |
| GET | `/api/health-record` | Full health record |
| POST | `/api/chat` | Chatbot |
| GET | `/api/admin/patients` | All patients (admin) |
| POST | `/api/admin/doctors/add` | Add doctor (admin) |

---

## Database Schema

| Table | Purpose |
|---|---|
| `patient` | Patient profiles |
| `doctor` | Doctor profiles & availability |
| `appointment` | Bookings |
| `webuser` | Unified login index (p/d/a) |
| `specialties` | Medical specialties |
| `lab_result` | Test results |
| `doctor_review` | Ratings & reviews |
| `health_sharing` | Patient-controlled data sharing |
| `admin` | Admin accounts |

---

## Chatbot

The built-in assistant supports natural language queries for:

- Viewing appointments
- Finding available doctors
- Checking lab results
- Navigation help (booking, cancelling, settings)

---

## Default Admin Accounts

| Email | Password |
|---|---|
| `admin@hms.com` | `123` |
| `admin@edoc.com` | `123` |

> Change these passwords after first login.
