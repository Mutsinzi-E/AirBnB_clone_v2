-- Create the development database if it does not exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the development user if it does not exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Set the required password.
ALTER USER 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Remove any existing privileges from the user.
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'hbnb_dev'@'localhost';

-- Grant all privileges only on the development database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant only SELECT on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
