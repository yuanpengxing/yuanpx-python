# -*- coding: UTF-8 -*-
# author: yuanpx
import pymysql as pymysql


class MysqlClient:
    def __init__(self):
        config = {
            'host':'192.168.31.35',
            'port':3306,
            'user':'root',
            'password':'123456',
            'db':'mysql',
            'charset':'utf8mb4',
            'cursorclass':pymysql.cursors.DictCursor
        }
        self.conn = pymysql.connect(**config)

    def insert(self, sql, tuple):
        """
        :param sql:
            sql = 'INSERT INTO employees (name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s)' ，对应的tuple
            tuple = ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14))

        :param tuple: tuple的大小和顺序，严格按照占位符来确定
        :return:
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, tuple)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()


    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()