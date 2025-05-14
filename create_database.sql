-- create client database  
CREATE DATABASE ClientDB
    WITH
    OWNER = bank -- alternatively can be postgres
    ENCODING = 'UTF8' -- encoding system
    LC_COLLATE = 'C' -- collation order
    LC_CTYPE = 'C' -- character classification
    LOCALE_PROVIDER = 'libc' -- default collation
    TABLESPACE = pg_default -- default tablespace
    CONNECTION LIMIT = -1 -- unlmited concurrent connections
    IS_TEMPLATE = False -- database cannot be a template
;