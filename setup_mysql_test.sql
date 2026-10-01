-- Create the test database if it does not exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user if it does not exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Set the required password.
ALTER USER 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Remove any existing privileges from the user.
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'hbnb_test'@'localhost';

-- Grant all privileges only on the test database.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant only SELECT on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
