# 🏪 Django Simple Store & Order Management System

A simple Django web application to display products, accept quantities, create orders, and show order history.  
This mini-project demonstrates Django models, views, templates, and form handling.

---

## 📂 Project Structure


django-mini-project/

1) simple_store/ __init__.py/ settings.py/ urls.py/ wsgi.py(Project Folder)

2) store/ migrations/ __init__.py/ admin.py/ apps.py/ models.py/ urls.py/ views.py (Django App)

3) frontend / migrations / templates / home.html / __init__.py/ (frontend)

.venv/
manage.py


---

## 🚀 Features

- Display list of products  
- User enters quantity and places an order  
- Automatically calculates total order amount  
- Shows order history with timestamps  
- Simple UI using Django Templates  
- Uses Django ORM for database operations  

---

## 🛠 Tech Stack

- Python  
- Django  
- SQL(MySQL)  
- HTML (Django Templates)

---

## 🧩 Main Files Explanation

### frontend/templates/home.html
- Renders the product list  
- Accepts quantity input  
- Displays order history  

### store/models.py
Contains:
- Product
- Order
- OrderItem

### store/views.py
Handles:
- Home page  
- Order creation  
- Order listing  

### store/urls.py
Defines routes for store actions.

---

## 🗄 Database Models

### Product
- name  
- price  

### Order
- created_at  
- total_amount  

### OrderItem
- order  
- product  
- quantity  
- total_price  
