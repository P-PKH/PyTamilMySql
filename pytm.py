# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:15:53 2017

@author: 116749
"""
import sys
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='root', db='wccdb', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * from tamil"
            # WHERE `email`=%s"
            # cursor.execute(sql, ('webmaster@python.org',))
            cursor.execute(sql)
            result = cursor.fetchall()

            # print (str(result).encode('utf-8'))
            # print (str(result).encode('raw-unicode-escape').decode('utf-8'))

            #print(result[0][u'data'])
            #print(type(result))

            print ("Record: ", result)
            print ("Record[2]: ", result[0]['data'])

            f = open('D:\MyFiles\Pers\Project\wcc\output2.txt', 'w', encoding='utf-8')
            f.write(str(result))
            f.close()

            #   mystring = [u'\u0bb5', u'\u0ba3' u'\u0b95' u'\u0bcd' u'\u0b95' u'\u0bae' u'\u0bcd']
finally:
    connection.close()