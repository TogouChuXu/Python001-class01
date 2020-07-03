# -*- encoding: utf8 -*-

import pymysql


class PymysqlClient:
    """读取mysql数据库的客户端类"""

    def __init__(self, host, user, password, database):
        """构造函数"""
        self._conn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
        self._cur = self._conn.cursor()

    def execute(self, sql, args=()):
        try:
            """运行SQ语句"""
            if isinstance(args, list):  # 批量执行SQL语句，此时parameter是list，其元素是tuple
                self._cur.executemany(sql, args)
            else:  # 单次执行SQL语句，此时parameter是tuple或者None
                self._cur.execute(sql, args)
            if sql.split()[0].upper() != 'SELECT':  # 非select语句，则自动执行commit()
                self._conn.commit()
        except Exception as e:
            print (e)
            self._conn.rollback()
            return 0
        return self._cur.lastrowid

    def getlast(self):
        return self._cur.lastrowid

    def close(self):
        """关闭数据库连接"""
        self._cur.close()
        self._conn.close()
