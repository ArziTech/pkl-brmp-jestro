#!/bin/bash

# Muat .env ke shell
export $(grep -v '^#' .env | xargs)

# Jalankan psql di container
docker exec -it postgres-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
