# Smart Task Analyzer


# Project Overview:

The Smart Task Analyzer is a full-stack web application that helps users manage, organize, and prioritize their tasks efficiently. The backend is powered by Django, handling task storage, retrieval, and CRUD operations, while the frontend uses HTML, CSS, and JavaScript for a responsive and interactive user interface.

It is designed to help users focus on high-priority tasks, track deadlines, and improve productivity.

# Features:
Add tasks with title, due date, estimated hours, and importance.
Update or delete tasks easily.
Analyze tasks based on importance and urgency (earliest due date first).
Persistent storage using Django ORM and SQLite/PostgreSQL database.
Interactive frontend with real-time updates using JavaScript.
RESTful API integration for seamless frontend-backend communication.

# Working:
Users fill in the task details via a form.
Frontend sends the task to Django backend using a POST API.
Backend stores the task in the database.
Frontend fetches all tasks using a GET API and displays them dynamically.
Clicking Analyze Tasks sorts tasks by importance and urgency using JavaScript.
Users can update or delete tasks, which triggers PUT/DELETE APIs.
Tasks remain persistent in the database for future use.

# Technologies Used:
Backend: Django, Python, SQLite/PostgreSQL
Frontend: HTML, CSS, JavaScript
APIs: Django REST framework
Logic: Custom JavaScript algorithm for task prioritization