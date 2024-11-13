-- Drop existing tables if they exist
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

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
    duration INTEGER NOT NULL,
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
    status VARCHAR(20) DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample services
INSERT INTO services (name, description, duration, price) VALUES
('Haircut', 'Basic haircut and styling', 60, 50.00),
('Color', 'Full hair coloring', 120, 120.00),
('Highlights', 'Partial or full highlights', 90, 100.00),
('Blowout', 'Wash and blowout styling', 45, 40.00),
('Treatment', 'Deep conditioning treatment', 30, 35.00);

-- Insert sample user (Madeleine)
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

-- Select appointments with service names instead of IDs
SELECT 
    appointments.firstname,
    appointments.lastname,
    services.name as service,
    appointments.appointment_time,
    appointments.status
FROM appointments 
JOIN services ON appointments.service_id = services.id;

SELECT version();
