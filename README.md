# HRMS Lite – Full Stack Application

## Frontend Repository
https://github.com/pradeeppathak1996/hrms-lite-frontend

## Backend Repository
https://github.com/pradeeppathak1996/hrms-lite-backend

---

## Live Application (Production)

**Frontend (Vercel):**  
https://hrms-lite-frontend-j4rc.vercel.app

**Backend API (Render):**  
https://hrms-lite-backend-1-qd60.onrender.com

> Note: The backend is an API-only Django application.  
> The root URL (`/`) does not serve a webpage and may show **Not Found**.  
> All functionality is exposed via API endpoints under `/api/`.

---

## Project Overview

**HRMS Lite** is a lightweight Human Resource Management System built to manage employees and their attendance with a strong focus on **data correctness, validation, and production stability**.

The project demonstrates a complete **end-to-end full-stack workflow**, covering frontend UI, REST APIs, and database persistence.

### Key Capabilities
- Employee management (Add, View, Delete)
- Daily attendance tracking
- Employee-wise attendance history
- Attendance summaries and analytics
- Central dashboard with key HR metrics

---

## Tech Stack

### Frontend
- React
- React Router
- Axios
- Custom CSS

### Backend
- Python
- Django
- Django REST Framework

### Database
- Postgresql (used for assignment and demo scope)

### Deployment
- Frontend: Vercel
- Backend: Render

---

## Features Implemented

### Employee Management
- Add new employees
- View employee list
- Delete employees

#### Employee Data Requirements
To add an employee, the following data is required:
- **Employee ID**: Must contain both letters and numbers (e.g. `EMP001`)
- **Full Name**: Alphabetic characters only
- **Email**: Must be a valid email format
- **Department**: Alphabetic characters only

Validations are enforced on both frontend and backend to ensure data consistency.

---

### Attendance Management
- Mark attendance for employees
- Attendance status: **Present / Absent**
- Attendance allowed only for the **current local date**
- Future or invalid dates are restricted
- View all attendance records
- View attendance history per employee

---

### Dashboard Summary
- Total employees
- Total attendance records
- Total present count
- Total absent count
- Clean, card-based dashboard UI

---

## Data Validation & Error Handling

### Backend Validations
- Required field validation
- Email format validation
- Duplicate employee prevention
- Attendance date validation
- Proper HTTP status codes with meaningful error messages

### Timezone Handling
- Frontend uses browser local time
- Backend uses Django 'timezone.localdate()'
- Prevents UTC vs IST date mismatch issues in production

---

## API Endpoints (Production)

- Employees API:  
  `https://hrms-lite-backend-1-qd60.onrender.com/api/employees/`

- Attendance API:  
  `https://hrms-lite-backend-1-qd60.onrender.com/api/attendance/`

---

## Running the Project Locally (Optional)

> Local setup is optional and intended only for development or testing.

### Backend (Local)

```bash
cd hrms-lite-backend

python -m venv venv
source venv/bin/activate   

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver