__author__ = 'robert'
import psycopg2
import sqlite3
import datetime

load_conn = psycopg2.connect(host='172.26.26.200', database='locationdata', user='postgres', password='197210')
lcursor = load_conn.cursor()

dump_conn = sqlite3.connect("../db")
dcursor = dump_conn.cursor()

def load_employees():
    lcursor.execute("select name, card_id, duty, mine_id, birthday from config_person")
    total = lcursor.fetchall()
    for t in total:
        age = 2012 - t[4].year
        SQL = "insert into app_employee values (\"%s\", \"%s\", \"%s\", \"%s\", %d, 1)" % (t[0], t[1], t[2], t[3], age)
        #print SQL
        dcursor.execute(SQL)
    dump_conn.commit()

def load_areas():
    lcursor.execute("select area_id, mine_id, area_num, area_name, area_type from config_area")
    total = lcursor.fetchall()
    for t in total:
        SQL = "insert into app_area values (\"%s\", \"%s\", %d, \"%s\", \"%s\")" % (t[0], t[1], t[2], t[3], t[4])
        print SQL
        dcursor.execute(SQL)
    dump_conn.commit()

def load_points():
    lcursor.execute("select point_id, mine_id, point_name from config_points")
    total = lcursor.fetchall()
    for t in total:
        SQL = "insert into app_point values (\"%s\", \"%s\", \"%s\")" % (t[0], t[1], t[2])
        print SQL
        dcursor.execute(SQL)
    dump_conn.commit()



if __name__ == '__main__':
    #load_employees()
    #load_areas()
    load_points()
