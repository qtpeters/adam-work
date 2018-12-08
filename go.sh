#!/bin/bash
rm -f cvintl.db
sqlite3 cvintl.db < cvintl.sql
python mkdb.py
