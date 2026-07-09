# 🔐 Secure Web Application using Flask

A secure web application developed using **Python Flask** that demonstrates secure authentication, password protection, database security, and common web security practices.

This project was created as part of a cybersecurity project portfolio to understand and implement secure web development concepts.

---

# 📌 Project Objective

The objective of this project is to build a secure web application that protects user information by implementing:

- Secure user authentication
- Password hashing
- Input validation
- Database security
- Session management
- Protection against common web vulnerabilities

---

# 🚀 Features

## 1. User Registration

Users can create an account by providing:

- Username
- Email
- Password

Security implementation:

- Passwords are never stored in plain text
- Passwords are encrypted using **bcrypt hashing**
- User input is validated before storage

---

## 2. Secure Login System

The application provides:

- User authentication
- Password verification
- Secure session creation
- Logout functionality

Authentication flow:

```
User enters credentials

        ↓

Retrieve user from database

        ↓

Compare bcrypt password hash

        ↓

Create secure session

        ↓

Access dashboard
```

---

## 3. Protected Dashboard

The dashboard is accessible only to authenticated users.

Features:

- Displays user information
- Shows implemented security features
- Prevents unauthorized access

---

# 🔒 Security Features Implemented

## Password Hashing

Technology:

```
bcrypt
```

Benefits:

- Generates unique salts
- Protects stored passwords
- Prevents plain-text password exposure


Example stored password:

```
$2b$12$7x93kJ........
```

The original password is never stored.

---

## SQL Injection Prevention

Implemented using:

```
SQLAlchemy ORM
```

Instead of raw SQL queries:

```sql
SELECT * FROM users WHERE email='input'
```

the application uses ORM-based queries:

```python
User.query.filter_by(email=email).first()
```

This reduces SQL injection risks.

---

## Input Validation

The application validates:

- Username format
- Email format
- Password complexity

Password requirements:

- Minimum 8 characters
- Uppercase letter
- Lowercase letter
- Number
- Special character

---

## Session Security

Implemented using:

- Flask-Login
- Secure session handling
- Login-required routes

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| Flask-Login | Authentication management |
| Flask-SQLAlchemy | Database interaction |
| Flask-Bcrypt | Password hashing |
| SQLite | Database |
| HTML/CSS | Frontend design |

---

# 📂 Project Structure

```
secure-web-application-flask/

│
├── app.py
├── extensions.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── users.db
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── security/
│   ├── __init__.py
│   └── validation.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

# ⚙️ Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/secure-web-application-flask.git
```

---

## 2. Navigate to Project

```bash
cd secure-web-application-flask
```

---

## 3. Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start Flask server:

```bash
python app.py
```

Application will run at:

```
http://127.0.0.1:5000
```

---

# 🖥 Application Screens

## Home Page

Features:

- Project introduction
- Security information
- Navigation options


## Registration Page

Allows users to create secure accounts.


## Login Page

Authenticates users using bcrypt password verification.


## Dashboard

Displays protected user information after successful login.

---

# 🧪 Testing

## Registration Test

Example:

```
Username:
admin123

Email:
admin@gmail.com

Password:
Secure@123
```

Expected:

```
Account created successfully
```

---

## Login Test

Valid credentials:

```
Email:
admin@gmail.com

Password:
Secure@123
```

Result:

```
Dashboard access granted
```

---

# 📚 Cybersecurity Concepts Demonstrated

- Authentication security
- Password hashing
- Secure password storage
- Input validation
- Database protection
- Session management
- Secure coding practices
- OWASP security concepts

---

