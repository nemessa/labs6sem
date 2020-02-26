#!/bin/bash
PGPASSWORD=password
export PGPASSWORD
pg_dump -h 62.109.15.226 -U user_1 -Fc dima_lab5 > /tmp/db.dump
#send 'password'