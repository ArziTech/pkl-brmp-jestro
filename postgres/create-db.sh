!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE TABLE rainfall_data (
  id SERIAL PRIMARY KEY,
  tippingCount NUMERIC(6,2) NOT NULL,
	sessionRain NUMERIC(6,2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW() 
  );
CREATE TABLE humidity (
  id SERIAL PRIMARY KEY,
  temp NUMERIC(6,2) NOT NULL,
	rh NUMERIC(6,2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW() 
  );
CREATE TABLE soil_moisture (
  id SERIAL PRIMARY KEY,
  moisture NUMERIC(6,2) NOT NULL,
	status TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW() 
  );
EOSQL
