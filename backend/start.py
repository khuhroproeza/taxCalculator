#!/usr/bin/env python3
import os
from subprocess import run

os.environ["DB_NAME"] = "TaxCalculator"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_USER"] = "root"
os.environ["DB_PASS"] = ""
#run("chmod +x setup_database.sh")


