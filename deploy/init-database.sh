#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER todolist;
	ALTER ROLE todolist WITH PASSWORD 'todolist';
	CREATE DATABASE todolist;
	GRANT ALL PRIVILEGES ON DATABASE todolist TO todolist;
EOSQL