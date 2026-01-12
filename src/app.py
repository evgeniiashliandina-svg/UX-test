import subprocess
import pickle
import sqlite3

API_KEY = "TEST_HARDCODED_SECRET"

def search(name):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE name = '{name}'")  # SQL injection
    return cur.fetchall()

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)  # command injection

def load(data):
    return pickle.loads(data)  # insecure deserialization
