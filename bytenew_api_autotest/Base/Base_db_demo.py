# -*- coding: UTF-8 -*-
import MySQLdb
import psycopg2
from typing import Optional, Union
import common.commons as commons

class DB:
    def __init__(self):
        self.logs = commons.Common.get_logs(self)
        self.connection: Optional[Union[MySQLdb.Connection, psycopg2.extensions.connection]] = None
        self.cursor: Optional[Union[MySQLdb.cursors.Cursor, psycopg2.extensions.cursor]] = None

    def connect(
        self,
        db_type: str = 'mysql',
        host: str = '101.126.55.217',
        user: str = 'nktest',
        password: str = 'BNuokeBE_IxIAjTesT',
        database: str = 'banniu_book',
        charset: str = 'utf8'
    ) -> None:
        """连接数据库"""
        try:
            if db_type == 'mysql':
                self.connection = MySQLdb.connect(
                    host=host,
                    user=user,
                    passwd=password,
                    db=database,
                    charset=charset
                )
            elif db_type == 'postgresql':
                self.connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            else:
                raise ValueError(f"不支持的数据库类型: {db_type}")

            self.cursor = self.connection.cursor()
            self.logs.info(f"成功连接 {db_type} 数据库: {database}")

        except Exception as e:
            self.logs.error(f"数据库连接失败: {str(e)}")
            raise

    def select(
        self,
        sql: str,
        parameters: Optional[tuple] = None,
        fetch_all: bool = False
    ) -> Union[tuple, list]:
        """执行查询语句"""
        if not self.connection or not self.cursor:
            raise ConnectionError("请先连接数据库")

        try:
            self.cursor.execute(sql, parameters)
            result = self.cursor.fetchall() if fetch_all else self.cursor.fetchone()
            self.logs.debug(f"执行SQL: {sql}\n参数: {parameters}\n结果: {result}")
            return result
        except Exception as e:
            self.logs.error(f"查询执行失败: {str(e)}")
            self.connection.rollback()
            raise

    def close(self) -> None:
        """关闭连接"""
        if self.cursor:
            self.cursor.close()
            self.logs.debug("数据库游标已关闭")
        if self.connection:
            self.connection.close()
            self.logs.info("数据库连接已关闭")