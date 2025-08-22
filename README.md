Study Timer App
Author: John Karl B. Denisado, Mary Pauline Silvino, Michael M. Estorque, Raymond Eusoff Mendoza, Reynan Christian Dordas, Syrah C. Fundal
Date: August 21, 2025

Project Overview
The Study Timer App is a simple and effective tool that helps users manage their study sessions using focused time intervals and breaks. It improves concentration, reduces procrastination, and helps build better study habits for long-term productivity.

Built with Python, Tkinter(GUI), SQLite3 (Database), and following OOP Principles with SRP (Single Responsibility Principle).

Main Features
Set custom study duration
Start/Stop timer
Notify user when time is up
Track completed study sessions per user

Folder Structure
StudyTimerApp/
│
├── main.py                        # Entry point of the app
│
├── database/                      # Database layer (SQLite3)
│   ├── __init__.py
│   ├── connection.py               # Handles SQLite connection
│   └── user_repository.py          # CRUD for users and sessions
│
├── models/                        # Data models (OOP)
│   ├── __init__.py
│   ├── user.py
│   └── session.py
│
├── services/                      # Business logic
│   ├── __init__.py
│   ├── timer_service.py
│   ├── notification_service.py
│   └── session_service.py
│
├── interfaces/                    # Interfaces (ISP applied)
│   ├── __init__.py
│   ├── notifier_interface.py
│   └── timer_interface.py
│
├── gui/                           # Tkinter GUI components
│   ├── __init__.py
│   ├── main_window.py
│   ├── user_form.py
│   └── timer_view.py
│
└── utils/                         # Helper functions
    ├── __init__.py
    └── helpers.py


User Flow
1. User opens the app
2. App asks for user name and study duration
3. Users clicks Start
4. Timer runs and updates in real time 
5. App notifies when time is up
6. Session is saved to database and user can track completed sessions

Installation
1. Clone the repository

git clone https://github.com/yourusername/StudyTimerApp.git
cd StudyTimerApp

2. Make sure you have Python 3.10+ installled
3. Install required dependencies (Tkinter is usually bundled with python)
pip install -r requirements.txt

Running the App
python main.py

Database
Uses SQLite3 (study_timer.db)
Tables:
    users (id, name)
    sessions (id, user_id, duration, completed_at)

Principles Applied
OOP - User and Session models, encapsulated logic
SRP - Each module has a single responsibility (DB, models, GUI, Services)

Future Improvents
For individual feature to be implemented by our group.