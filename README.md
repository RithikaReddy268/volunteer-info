# Volunteer Information Management System

## Overview

The Volunteer Information Management System is a simple web application developed using Flask and SQLite to help NGOs and organizations manage volunteer records efficiently.

Instead of maintaining volunteer details in spreadsheets, this system allows administrators to securely store, view, and manage volunteer information through a user-friendly interface.

---

## Features

### Admin Authentication
- Secure admin login
- Session-based authentication
- Logout functionality

### Volunteer Management
- Add new volunteers
- View all volunteer records
- Delete volunteer records

### Duplicate Entry Prevention
- Prevents the same volunteer information from being entered multiple times
- Checks Name, Email, Phone, Skills, and City before saving

### Database Integration
- Uses SQLite database for data storage
- Stores volunteer information permanently

---

## Technology Stack

### Backend
- Python
- Flask

### Database
- SQLite

### Frontend
- HTML
- CSS

---

## Database Fields

The system stores the following volunteer details:

- Name
- Email
- Phone Number
- Skills
- City

---

## Project Structure

```text
Volunteer-Management-System/
│
├── app.py
│
├── volunteers.db
│
├── templates/
│   ├── login.html
│   ├── index.html
│   ├── add_volunteer.html
│   └── view_volunteers.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## How to Run the Project

### Step 1: Install Flask

```bash
pip install flask
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open in Browser

```text
http://127.0.0.1:5000
```

---

## Login Credentials

```text
Username: admin
Password: admin@pass
```

---

## NGO Use Case

This project can be used by NGOs and non-profit organizations to manage volunteer information in an organized and efficient manner.

Benefits include:

- Centralized volunteer records
- Easy volunteer management
- Reduced manual paperwork
- Quick access to volunteer information
- Better organization of volunteer activities

---

## Future Enhancements

- Volunteer search functionality
- Volunteer update/edit functionality
- REST API integration
- Role-based access control
- Email notifications
- Advanced admin dashboard

---

## Author

Rithika Reddy

Developed as part of a Backend Development Internship Assignment.
