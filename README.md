## Project Overview

The HRMS Lite system allows an admin to:

- Manage employee records (Add, View, Delete)
- Mark and track daily attendance
- View attendance history per employee
- See attendance analytics and summaries
- Access a dashboard with key HR metrics

The focus of this project is **stability, correctness, and real-world usability**, not unnecessary features.

---

## Tech Stack

### Frontend
- React (Create React App)
- React Router
- Axios
- CSS (Custom styling)

### Backend
- Python
- Django
- Django REST Framework

### Database
- SQLite (Local & Assignment Scope)

### Deployment
- **Frontend:** Vercel
- **Backend:** Render

---

## ✨ Features Implemented

### 👨‍💼 Employee Management
- Add new employees
- View employee list
- Delete employees
- Server-side validations:
  - Required fields
  - Valid email format
  - Duplicate employee handling
  - Name & department character validation

---

### 🕒 Attendance Management
- Mark attendance for employees
- Attendance status: **Present / Absent**
- Attendance restricted to **current local date only**
- Prevention of invalid date selection (timezone-safe)
- View all attendance records
- View attendance records **per employee**

---

### 📊 Dashboard Summary
- Total Employees
- Total Attendance Records
- Total Present
- Total Absent
- Clean card-based UI

---

## 🎁 Bonus Features (Implemented)

✅ Filter attendance records by date  
✅ Display total present days per employee  
✅ Attendance analytics per employee  
✅ Dashboard summary with counts  

---

##  Data Validation & Error Handling

### Backend Validations
- Required field validation
- Email format validation
- Duplicate employee prevention
- Attendance date validation using timezone-aware logic
- Meaningful error messages with proper HTTP status codes

### Timezone Handling
- Frontend uses browser local time (IST safe)
- Backend uses Django `timezone.localdate()`
- Prevents UTC vs IST midnight bugs permanently


## How to Run

### Backend Setup

```bash
cd backend

python -m venv venv
source venv/bin/activate  

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend will run on:

http://127.0.0.1:8000/

Frontend Setup

cd frontend
npm install
npm start

http://localhost:3000/# hrms-lite-backend
