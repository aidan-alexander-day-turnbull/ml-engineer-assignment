-- initailize extensions
CREATE EXTENSION pgcrypto;

-- import first five columns of data from csv file into staging table (replace file path for your device)
\COPY dbo.client_credentials ("client_id", "clientname", "password", "email", "created_on") FROM '/Users/aidz/Desktop/RBC/client_data.csv' DELIMITER ',' CSV HEADER;

-- clean data
-- remove honorifics and degrees and unintended special characters from client names
UPDATE dbo.client_credentials SET clientname = regexp_replace(clientname, 'MD|\\|DDS|Mrs.|Dr.|Mr.|Ms.|DVM|PhD|Miss', '');

-- trim whitespaces
UPDATE dbo.client_credentials SET "clientname" = trim(BOTH ' ' FROM "clientname");
UPDATE dbo.client_credentials SET "password" = trim(BOTH ' ' FROM "password");
UPDATE dbo.client_credentials SET "email" = trim(BOTH ' ' FROM "email");

-- insert data into integration table
INSERT INTO dbo.client_credentials_final 
    SELECT 
    "client_id"::INT, 
    pgp_sym_encrypt("clientname", 'toronto'),
    pgp_sym_encrypt("password", 'toronto'),
    pgp_sym_encrypt("email", 'toronto'),
    "created_on"::TIMESTAMP
    FROM dbo.client_credentials;

-- delete staging table
DROP TABLE dbo.client_credentials;



