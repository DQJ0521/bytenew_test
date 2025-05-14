# -*- coding: UTF-8 -*-
import MySQLdb
import psycopg2
from typing import Optional, Union, Tuple, Any
import common.commons as commons
from config.config_db import DB_CONFIGS

class DB:
    def __init__(self):
        self.logs = commons.Common.get_logs(self)
        self.connection: Optional[Any] = None
        self.cursor: Optional[Any] = None

    def connect(self, config_name: str = None, **kwargs) -> None:
        """
        连接数据库
        :param config_name: 配置文件中的配置名称 (优先使用)
        :param kwargs: 动态连接参数 (当config_name未指定时使用)
        """
        # 从配置文件加载配置
        if config_name:
            config = DB_CONFIGS.get(config_name)
            if not config:
                raise ValueError(f"数据库配置 '{config_name}' 不存在")
            kwargs.update(config)  # 合并配置参数

        db_type = kwargs.get('db_type', 'mysql')

        try:
            if db_type == 'mysql':
                self.connection = MySQLdb.connect(
                    host=kwargs.get('host', 'localhost'),
                    user=kwargs.get('user'),
                    passwd=kwargs.get('password'),
                    db=kwargs.get('database'),
                    port=kwargs.get('port', 3306),
                    charset=kwargs.get('charset', 'utf8')
                )
            elif db_type == 'postgresql':
                self.connection = psycopg2.connect(
                    host=kwargs.get('host', 'localhost'),
                    user=kwargs.get('user'),
                    password=kwargs.get('password'),
                    dbname=kwargs.get('database'),
                    port=kwargs.get('port', 5432)
                )
            else:
                raise ValueError(f"不支持的数据库类型: {db_type}")

            self.cursor = self.connection.cursor()
            self.logs.info(f"成功连接 {db_type} 数据库: {kwargs.get('database')}")

        except Exception as e:
            self.logs.error(f"连接失败: {str(e)}")
            raise

    def execute_query(self, sql: str, params: Optional[Tuple] = None, fetch_all: bool = False) -> Union[Tuple, list]:
        """执行查询语句
        :param sql: SQL语句 (建议使用WHERE column = %s参数化)
        :param params: 参数元组
        :param fetch_all: 是否获取全部结果
        :return: 查询结果 (单条元组或多条列表)
        """
        self._validate_connection()
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall() if fetch_all else self.cursor.fetchone()
        except Exception as e:
            self.logs.error(f"Query failed: {sql}\nError: {str(e)}")
            self.connection.rollback()
            raise

    def execute_update(self, sql: str, params: Optional[Tuple] = None, auto_commit: bool = True) -> int:
        """执行更新/插入语句
        :param sql: SQL语句 (INSERT/UPDATE/DELETE)
        :param params: 参数元组
        :param auto_commit: 是否自动提交事务
        :return: 受影响的行数
        """
        self._validate_connection()
        try:
            self.cursor.execute(sql, params)
            if auto_commit:
                self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.logs.error(f"Update failed: {sql}\nError: {str(e)}")
            self.connection.rollback()
            raise

    def insert(self, table: str, data: dict, auto_commit: bool = True) -> int:
        """快捷插入方法
        :param table: 表名
        :param data: 插入数据字典 {column: value}
        :param auto_commit: 是否自动提交
        :return: 插入的行数 (通常返回1)
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return self.execute_update(sql, tuple(data.values()), auto_commit)

    def update(self, table: str, set_data: dict, where_cond: str, where_params: Tuple = None, auto_commit: bool = True) -> int:
        """快捷更新方法
        :param table: 表名
        :param set_data: 更新数据 {column: new_value}
        :param where_cond: WHERE条件语句 (e.g. "id = %s")
        :param where_params: WHERE条件参数
        :param auto_commit: 是否自动提交
        :return: 受影响的行数
        """
        set_clause = ', '.join([f"{k} = %s" for k in set_data.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_cond}"
        params = tuple(set_data.values()) + (where_params if where_params else ())
        return self.execute_update(sql, params, auto_commit)

    def commit(self) -> None:
        """手动提交事务"""
        if self.connection:
            self.connection.commit()
            self.logs.debug("Transaction committed")

    def _validate_connection(self) -> None:
        """验证连接状态"""
        if not self.connection or not self.cursor:
            raise ConnectionError("Database not connected")

    def close(self) -> None:
        """关闭连接"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.logs.info("Connection closed")