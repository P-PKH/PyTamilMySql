"""
# -*- coding: utf-8 -*-

Created on Sun Feb 26 10:15:53 2017

@author: 116749
"""
import sys
import pymysql.cursors

def byte_to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes): #check if its in bytes
        print(bytes_or_str.decode('utf-8'))
    else:
        print("Object not of byte type")

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='root', db='wccdb', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
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
            #print (str(result).encode('utf-8'))
            #print (str(result).encode('raw-unicode-escape').decode('utf-8'))
            #print (chr(result))
            #print(len(u'கி'))
            #print(unicode(0x0b85))
            #   mystring = [u'\u0bb5', u'\u0ba3' u'\u0b95' u'\u0bcd' u'\u0b95' u'\u0bae' u'\u0bcd']
            # result1 = u'സന്തോഷ്  हिन्दी'
            # for ch in result1:
                # if (ch.isalpha()):
                    # print (ch)
            print (str(result[0][u'data']).encode('utf-8')).decode('utf-8')
            print ("sys.stdout.encoding: ", sys.stdout.encoding)     #cp437
            print ("sys.getdefaultencoding(): ", sys.getdefaultencoding())        #utf-8
            print ("str(result).encode('utf-8'): ", str(result).encode('utf-8'))
            print ("type(result): ", type(result))
            #b"[{'eng_data': 'India Is My Country', 'id': 1, 'data': '\xe0\xae\x87\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xbf\xe0\xae\xaf\xe0\xae\xbe \xe0\xae\xa8\xe0\xae\xbe\xe0\xae\x9f\xe0\xaf\x8d\xe0\xae\x9f\xe0\xae\xbf\xe0\xae\xa9\xe0\xaf\x8d \xe0\xae\xaa\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\x99\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d'}]"
            #print (b'\xe0\xae\x87\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xbf\xe0\xae\xaf\xe0\xae\xbe \xe0\xae\xa8\xe0\xae\xbe\xe0\xae\x9f\xe0\xaf\x8d\xe0\xae\x9f\xe0\xae\xbf\xe0\xae\xa9\xe0\xaf\x8d \xe0\xae\xaa\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\x99\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d'.decode('utf-8'))
            #print (result[0][u'data'])
            f = open('D:\MyFiles\Pers\Project\wcc\output.txt', 'w')
            y = str(result[0][u'data']).decode('utf-8')
            f.write(y)
            f.close()
finally:
    connection.close()
