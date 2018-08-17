#!/usr/bin/env python3
# Code for Database Queries - Logs Analysis - Udacity Full Stack Nanodegree
# Alexandre D.

import psycopg2


def most_pop_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from top_three")
    articles = c.fetchall()
    list1 = [t[0] for t in articles]
    print ('The most popular three articles of all time:'
           + '\n'
           + '\n'.join(str(v) for v in list1)
           + '\n')
    db.close()


def most_pop_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from pop_authors")
    authors = c.fetchall()
    list1 = [t[0] for t in authors]
    print ('The most popular article authors of all time:'
           + '\n'
           + '\n'.join(str(v) for v in list1)
           + '\n')
    db.close()


def error_day():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from error_day")
    dates = c.fetchall()
    list1 = [t[0] for t in dates]
    print ("Days were more than 1% of requests lead to errors:"
           + '\n'
           + '\n'.join(str(v) for v in list1)
           + '\n')
    db.close()


most_pop_articles()
most_pop_authors()
error_day()
