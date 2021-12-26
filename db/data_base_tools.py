import os
import sqlite3
import attr
from typing import ClassVar


class DataBaseTools:

    __slots__ = ['conn', 'amount', 'cursor']

    __all_done_query: ClassVar = """select days from money_box where state = 'd'"""

    __update_done_query: ClassVar = """update money_box set state = 'd' where days = {}"""

    def __init__(self, amount):
        self.amount = amount
        self.__post_init__()

    def __post_init__(self) -> attr:
        setattr(DataBaseTools, 'conn', sqlite3.connect(self.db_path))
        setattr(DataBaseTools, 'cursor', self.conn.cursor())

    @property
    def db_path(self) -> str:
        path = os.path.dirname(__file__).replace('db', '')
        return os.path.join(path, 'db_storage')

    def get_all_done(self) -> list:
        """
        get all paid days
        :return: paid days
        """
        self.cursor.execute(self.__all_done_query)
        res = self.cursor.fetchall()
        return [i[0] for i in res]

    def update_done(self) -> None:
        """
        update paid days
        :return: None
        """
        self.cursor.execute(self.__update_done_query.format(self.amount))
        self.conn.commit()
        print(f'{self.cursor.rowcount} rows were updated.')

    def close(self) -> None:
        """
        close conn and cursor
        :return: None
        """
        self.cursor.close()
        self.conn.close()
