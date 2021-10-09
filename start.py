#!/usr/bin/env python3
import os
from subprocess import run

os.environ["DB_NAME"] = "TaxCalculator"
run("./setup_database.sh")
