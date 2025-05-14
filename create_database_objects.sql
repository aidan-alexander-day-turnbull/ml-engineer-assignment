-- create distinct schema
CREATE SCHEMA IF NOT EXISTS dbo 
    AUTHORIZATION bank
;

-- create staging table [datatypes are set to varchar(100) to accomedate imperfections in source file]
CREATE TABLE IF NOT EXISTS dbo.client_credentials
(
    "client_id" varchar(100) PRIMARY KEY,
    "clientname" varchar(100) NULL,
    "password" varchar(100) NULL,
    "email" varchar(100) NULL,
    "created_on" varchar(100) NULL
)
TABLESPACE pg_default
;

-- create integrated table
CREATE TABLE IF NOT EXISTS dbo.client_credentials_final
(
    "client_id" INTEGER PRIMARY KEY,
    "encrypted_clientname" bytea NOT NULL,
    "encrypted_password" bytea NOT NULL,
    "encrypted_email" bytea NOT NULL,
    "created_on" timestamp NOT NULL
)
TABLESPACE pg_default
;
