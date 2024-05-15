-- app user
CREATE ROLE pms_app LOGIN PASSWORD 'pms_app';

-- db owned by
CREATE DATABASE pms_db OWNER = pms_app;

-- revoke rights
REVOKE ALL ON DATABASE pms_db FROM PUBLIC;

--connect and change ownership
\connect pms_db
ALTER SCHEMA public OWNER TO pms_app;