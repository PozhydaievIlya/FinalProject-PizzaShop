# Pizza Restaurant Web Application

Welcome to the Pizza Restaurant Web Application! This project is a web application developed using Django, designed to manage the operations of a pizza restaurant. The application provides features for menu management, order processing, customer management, and more.

## Table of Contents
* Features
* Installation
* Usage
* Technologies Used
* Contributing
* License


## Features
Menu Management: Add, update, and remove items from the menu.
Order Processing: Handle customer orders from ORDERS database table.
Customer Management: Manage customer information and order history.
Authentication: User registration and login functionality for customers and staff.
Blog: Create posts on blog to entertain clients.
Admin Interface: Django's built-in admin interface for managing the application.

## Installation
Prerequisites
Python 3.x,
Django 3.x or higher,
pip (Python package installer),
djmoney,
widget_tweaks,
pillow

## Setup
Clone the repository:
```
git clone https://github.com/your-username/pizza-restaurant.git
```
```
cd pizza-restaurant
```

Create a virtual environment:
```
python -m venv venv
```
```
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install dependencies:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Create a superuser:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser to see the application.


## Usage
Admin Interface
To access the admin interface, go to http://127.0.0.1:8000/admin and log in with the superuser credentials you created during setup. From here, you can manage the menu, orders, and customers.

Customer Interface
Customers can register, log in, and browse the menu. They can place orders and view their order history.

Staff Interface
Staff can log in to manage orders and update their status.

    
## Technologies Used

* Backend: Django

* Frontend: HTML, CSS, JavaScript, Bootstrap

* Database: SQLite

## Contributing
Contributions are welcome! Please follow these steps to contribute:

## Fork the repository.
1. Create a new branch
```
git checkout -b feature-branch
```
2. Commit your changes 
```
git commit -am 'Add new feature'
```
3. Push to the branch 
```
git push origin feature-branch
```
4. Create a new Pull Request.
