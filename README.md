# Dandelion Salon Application

A web application for managing salon appointments and services.

## Features

- Make appointments 
- Create user accounts with email
- View hair styles and services
- Online payment processing
- Admin dashboard for salon management

## Live Demo

Visit the live application at: https://madeleinecoiffure.herokuapp.com/

## Tech Stack

- Django 3.2.5
- Python 3.9
- PostgreSQL (via Heroku)
- HTML/CSS/JavaScript
- Heroku for deployment

## Setup

1. Clone the repository
```bash
git clone [repository-url]
```

2. Create and activate virtual environment
```bash
python -m venv env

# Activate it (Mac specific)
source env/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
python3 manage.py runserver
```

4. Set up environment variables
```bash
cp .env.example .env

# Edit .env with your configurations
```

=======
psql -v DB_ADMIN_EMAIL=your@email.com -v DB_ADMIN_PASSWORD=yourpassword -v DB_ADMIN_USERNAME=yourusername -f init.sql
# Edit .env with your configurations
```

## Database Setup

### PostgreSQL Schema
To set up the PostgreSQL database for the Madeleine Salon de Coiffure booking system:


# Create the database
brew list | grep postgresql
postgres --version
brew install postgresql@14
brew services start postgresql@14
createdb salon_app
createuser -s $(whoami)
createdb salon_app
psql -l
psql salon_app
touch schema.sql
code schema.sql
psql salon_app < schema.sql // After adding the below to the schema.sql file run this command

Add the following to the schema.sql file:

```sql
-- Create Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Services table
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration INTEGER NOT NULL, -- Duration in minutes
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Appointments table
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    service_id INTEGER REFERENCES services(id),
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telephone VARCHAR(20),
    appointment_time TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'scheduled', -- scheduled, completed, cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample services
INSERT INTO services (name, description, duration, price) VALUES
('Haircut', 'Basic haircut and styling', 60, 50.00),
('Color', 'Full hair coloring', 120, 120.00),
('Highlights', 'Partial or full highlights', 90, 100.00),
('Blowout', 'Wash and blowout styling', 45, 40.00),
('Treatment', 'Deep conditioning treatment', 30, 35.00);

-- Insert sample user
INSERT INTO users (username, email, password) VALUES
('madeleine', 'madeleinesalondecoiffure@gmail.com', 'hashed_password_here');

-- Insert sample appointments
INSERT INTO appointments (
    user_id,
    service_id,
    firstname,
    lastname,
    email,
    telephone,
    appointment_time
) VALUES
(1, 1, 'Jane', 'Doe', 'jane@example.com', '123-456-7890', '2024-03-20 10:00:00'),
(1, 2, 'Mary', 'Smith', 'mary@example.com', '123-456-7891', '2024-03-20 14:00:00');
```

### Database Setup Instructions

1. Create the database in PostgreSQL:
```bash
createdb salon_app
```

2. Apply the schema:
```bash
psql salon_app < schema.sql
```

3. Update your Django settings.py DATABASE configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'salon_app',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then apply the schema:
````
psql salon_app < schema.sql
```

This schema provides:
- A `users` table for authentication
- A `services` table for different salon services
- An `appointments` table that tracks all bookings

Key features:
- Foreign key relationships between tables
- Timestamp tracking for appointments
- Status tracking for appointment state
- Price and duration tracking for services
- Contact information for clients


# Project Structure

```
dandelionCoiffure/
├── .git/
├── deployment/
├── docs/
│   ├── static/
│   ├── users/
│   │   └── index.html
│   ├── .DS_Store
│   ├── about.html
│   ├── calendar.html
│   ├── clients.html
│   ├── contact.html
│   ├── index.html
│   ├── login.html
│   ├── payment.html
│   ├── profile.html
│   └── register.html
├── env/
├── salonapp/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   ├── __init__.py
│   ├── .DS_Store
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── salonproject/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── .DS_Store
│   ├── asgi.py
│   ├── settings.py
│   ├── temp.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
│   ├── admin/
│   │   ├── css/
│   │   │   ├── vendor/
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── responsive.css
│   │   │   ├── rtl.css
│   │   │   └── widgets.css
│   │   ├── fonts/
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img/
│   │   │   ├── gis/
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── calendar-icons.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   ├── js/
│   │   │   ├── admin/
│   │   │   │   ├── DateTimeShortcuts.js
│   │   │   │   └── RelatedObjectLookups.js
│   │   │   ├── vendor/
│   │   │   ├── actions.js
│   │   │   ├── autocomplete.js
│   │   │   ├── calendar.js
│   │   │   ├── cancel.js
│   │   │   ├── change_form.js
│   │   │   ├── collapse.js
│   │   │   ├── core.js
│   │   │   ├── inlines.js
│   │   │   ├── jquery.init.js
│   │   │   ├── nav_sidebar.js
│   │   │   ├── popup_response.js
│   │   │   ├── prepopulate_init.js
│   │   │   ├── prepopulate.js
│   │   │   ├── SelectBox.js
│   │   │   ├── SelectFilter2.js
│   │   │   └── urlify.js
│   │   └── .DS_Store
│   └── .DS_Store
├── templates/
│   ├── users/
│   │   └── index.html
│   ├── .DS_Store
│   ├── about.html
│   ├── calendar.html
│   ├── clients.html
│   ├── contact.html
│   ├── login.html
│   ├── payment.html
│   ├── profile.html
│   └── register.html
├── venv/
├── .DS_Store
├── .env
├── .env.example
├── .gitignore
├── app.json
├── app.py
├── db.sqlite3
├── init.sql
├── latest.dump
├── LICENSE.txt
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── schema.sql
```