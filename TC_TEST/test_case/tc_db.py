#!/usr/bin/env python
# encoding: utf-8
__author__ = "Caohp"
import MySQLdb


class MySQLHelper:
    def __init__(self, host, user, password, db, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db)
            self.conn.set_character_set(self.charset)
            self.cur = self.conn.cursor()
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self, sql):
        try:
            n = self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

    def query_row(self, sql):
        self.query(sql)
        result = self.cur.fetchone()
        return result

    def query_all(self, sql):
        self.query(sql)
        result = self.cur.fetchall()
        desc = self.cur.description
        d = []
        for inv in result:
            _d = {}
            for i in range(0, len(inv)):
                _d[desc[i][0]] = str(inv[i])
            d.append(_d)
        return d

    def insert(self, p_table_name, p_data):
        for key in p_data:
            p_data[key] = "'""'" + str(p_data[key]) + "'"
        key = ','.join(p_data.keys())
        value = ','.join(p_data.values())
        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value + ")"
        return self.query(real_sql)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = MySQLHelper(host='10.2.0.202', user='xingdb_read', password='abc.1234%', db='che100')
    sql = "SELECT phone FROM che100.`tc_apply` WHERE name = '张三' ORDER BY id DESC;"
    result = db.query_all(sql)
    print result[0]['phone']
    db.close()
