const express = require('express');
const router  = express.Router();

module.exports = (db, requireLogin) => {

    router.post('/', requireLogin, (req, res) => {
        const { message } = req.body;
        const user = req.session.user;
        const pid  = user.pid;
        const msg  = (message || '').toLowerCase().trim();

        if (/^(hi|hello|hey|good morning|good afternoon|good evening|howdy|greetings)/.test(msg)) {
            return res.json({ reply: `Hello ${user.name}! 👋 How can I help you today?\n\nYou can ask me about:\n• Your appointments\n• Available doctors\n• Your lab results\n• How to book or cancel an appointment` });
        }

        if (/appointment|booking|schedule|booked/.test(msg)) {
            db.query(
                `SELECT a.appoid, a.appodate, a.status, d.docname, s.sname AS specialty
                 FROM appointment a
                 JOIN doctor d ON a.scheduleid = d.docid
                 LEFT JOIN specialties s ON d.specialties = s.id
                 WHERE a.pid = ? ORDER BY a.appodate DESC LIMIT 5`,
                [pid], (err, rows) => {
                    if (err || !rows.length) return res.json({ reply: 'You have no appointments yet. Visit the Book page to schedule one!' });
                    let reply = `📅 Your recent appointments:\n\n`;
                    rows.forEach(r => {
                        reply += `• ${r.appodate?.toString().slice(0,10)} — Dr. ${r.docname} (${r.specialty || 'General'})\n  Status: ${r.status}\n\n`;
                    });
                    reply += 'To book a new appointment, go to the Book page. To cancel, visit My Bookings.';
                    res.json({ reply });
                }
            );
            return;
        }

        if (/doctor|specialist|physician|find.*doc|available doc/.test(msg)) {
            db.query(
                `SELECT d.docname, d.country, d.city, d.consultation_fee, d.rating, s.sname AS specialty
                 FROM doctor d LEFT JOIN specialties s ON d.specialties = s.id
                 WHERE d.available = 1 ORDER BY d.rating DESC LIMIT 6`,
                (err, rows) => {
                    if (err || !rows.length) return res.json({ reply: 'No doctors available at the moment.' });
                    let reply = `👨‍⚕️ Top available doctors:\n\n`;
                    rows.forEach(r => {
                        reply += `• Dr. ${r.docname} — ${r.specialty || 'General'}\n  ${r.city}, ${r.country} | ⭐ ${r.rating} | $${r.consultation_fee}\n\n`;
                    });
                    reply += 'Visit the Doctors page to see all available doctors and book an appointment.';
                    res.json({ reply });
                }
            );
            return;
        }

        if (/lab|result|test|blood|report/.test(msg)) {
            db.query(
                `SELECT r.test_name, r.result, r.created_at, d.docname
                 FROM lab_result r LEFT JOIN doctor d ON r.docid = d.docid
                 WHERE r.pid = ? ORDER BY r.created_at DESC LIMIT 5`,
                [pid], (err, rows) => {
                    if (err || !rows.length) return res.json({ reply: 'No lab results found on your record yet.' });
                    let reply = `🧪 Your recent lab results:\n\n`;
                    rows.forEach(r => {
                        reply += `• ${r.test_name}: ${r.result}\n  Added by Dr. ${r.docname} on ${r.created_at?.toString().slice(0,10)}\n\n`;
                    });
                    reply += 'Visit the Results page for full details and notes.';
                    res.json({ reply });
                }
            );
            return;
        }

        if (/how.*book|book.*how|make.*appointment|create.*appointment/.test(msg)) {
            return res.json({ reply: `To book an appointment:\n\n1. Click "Book Appointment" in the menu\n2. Choose a medical specialty\n3. Select a doctor\n4. Pick a date\n5. Confirm your booking\n\nYou can also view and manage your bookings under "My Bookings".` });
        }

        if (/cancel/.test(msg)) {
            return res.json({ reply: `To cancel an appointment:\n\n1. Go to "My Bookings" in the menu\n2. Find the appointment you want to cancel\n3. Click the Cancel button next to it\n\nOnly BOOKED appointments can be cancelled.` });
        }

        if (/health record|medical record|my record|health history/.test(msg)) {
            return res.json({ reply: `Your health record is available under the "Health Record" section in the menu. It includes:\n\n• All past and upcoming appointments\n• Lab test results\n• Doctor notes` });
        }

        if (/setting|profile|update|password|phone|address/.test(msg)) {
            return res.json({ reply: `You can update your profile under the Settings page:\n\n• Change your name\n• Update phone number\n• Update address\n• Change password` });
        }

        if (/emergency|urgent|critical|911|ambulance/.test(msg)) {
            return res.json({ reply: `🚨 For emergencies, please call your local emergency number immediately. Do not use this chat for medical emergencies.` });
        }

        if (/thank|thanks|thank you|appreciate/.test(msg)) {
            return res.json({ reply: `You're welcome, ${user.name}! 😊 Feel free to ask if you need anything else.` });
        }

        res.json({ reply: `I can help you with:\n\n• 📅 Appointments — view, book, or cancel\n• 👨‍⚕️ Doctors — find available doctors\n• 🧪 Lab Results — view your test results\n• 📋 Health Record — your full medical history\n• ⚙️ Settings — update your profile` });
    });

    return router;
};
