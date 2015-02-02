import sqlite3
from flask import Flask, render_template, abort, request, jsonify, g

DATABASE = 'C:/Users/Nitin Krishnan/Documents/RaleighOpenData/PoliceIncidents.sqlite'

app = Flask(__name__)

def get_db():
    db = None
    if db is None:
        db = connect_db()
    return db

def connect_db():
    return sqlite3.connect(DATABASE)


c = get_db().cursor()


def crimesThatDay(year,month,day):
    crimes = [];
    timebin =year +'-'
    timebin = timebin + month
    timebin = timebin + '-'
    timebin = timebin + day
    print timebin
    c = get_db().cursor()
    for row in c.execute('SELECT * FROM Police WHERE dates = ?',[timebin]):
        crimes.append({"date":row[10],"year":row[14],"month":row[13],"day":row[11],"latitude":row[7],"longitude":row[8],"type":row[20]})
        
    return crimes    
    
