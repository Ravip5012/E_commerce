🛍️ E-commerce WebShopi

E-commerce WebShopi is a full-featured Python Django e-commerce web application.
It allows users to browse over 200+ products, manage a cart, make secure payments using UPI, and get automated billing with GST.
It has separate apps for core e-commerce functionality, authentication, and payment processing.

🚀 Features

User Authentication: Register, login, logout, and manage profiles.

Product Catalog: 200+ products organized into multiple categories.

Admin Panel: Easily add, update, or delete products and categories.

Cart System: Add items to cart, update quantity, remove items.

Order Management: Place, track, and view order history.

Payment Integration: UPI, Google Pay, Paytm, Net Banking support.

GST Billing: Automatic GST calculation based on product category.

Email Notifications: Confirmation emails on successful orders.

Responsive UI: Works across all devices.

🧰 Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite3

Payment Gateway: UPI / Razorpay Integration (demo/test)

Environment: Python 3.x

📁 Project Structure
E-commerce-WebShopi/
│
├── webshopi/                       # Main Django project folder
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI entry point
│   ├── asgi.py                     # ASGI entry point (optional)
│
├── shop/                           # Core e-commerce logic
│   ├── models.py                   # Product, Order, Category models
│   ├── views.py                    # Handles product and order views
│   ├── urls.py                     # Shop app routes
│   ├── templates/shop/             # HTML templates for shop
│   ├── static/shop/                # CSS, JS, images for shop
│
├── authentication/                 # User login/signup/profile management
│   ├── models.py                   # User profile model (if extended)
│   ├── views.py                    # Auth views (login, signup, logout)
│   ├── forms.py                    # Django forms for auth
│   ├── urls.py                     # Auth app routes
│   ├── templates/authentication/   # Login/Signup/Profile templates
│
├── paymentgateway/                 # Payment handling
│   ├── views.py                    # Payment processing logic
│   ├── urls.py                     # Payment app routes
│   ├── templates/paymentgateway/   # Payment templates
│
├── webshopiapp/                    # Shared static files
│   ├── static/                     # CSS, JS, images shared across apps
│
├── db.sqlite3                      # Default database
├── manage.py                       # Django project runner
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/Sandipy47/E-commerce-WebShopi.git
cd E-commerce-WebShopi


Create a virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create an admin user

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open in browser

http://127.0.0.1:8000/

💳 Payment Integration

Handled by paymentgateway app.

Integrated UPI-based payment (Razorpay/demo).

Supports multiple payment modes: Google Pay, Paytm, Net Banking, Cash On Delivery.

Payment status automatically updates in the order record.

Configure Razorpay/UPI keys in settings.py for testing or real payments.

🔐 Authentication

Separate authentication app manages all user-related operations.

Features:

Register new accounts

Secure login/logout

Profile management

Order history

Passwords securely hashed using Django authentication system.

🚀 Deployment

Deploy on platforms like Render, Railway, or PythonAnywhere.

Steps:

Push the project to GitHub.

Configure environment variables (SECRET_KEY, DEBUG, RAZORPAY_KEY, etc.).

Run migrations and collect static files:

python manage.py migrate
python manage.py collectstatic


Start the server with Gunicorn:

web: gunicorn webshopi.wsgi

🧩 Customization

Add products and categories via Django admin.

Modify payment options in paymentgateway/views.py.

Extend user profile in authentication/models.py.

Update shared static files in webshopiapp/static/.

Modify front-end templates in templates/ directories for each app.

🧑‍💻 Author

Sandip Yadav (Sany)
📧 sany.luminip@gmail.com

🌐 GitHub Profile
