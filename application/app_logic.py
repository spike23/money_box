from db.data_base_tools import DataBaseTools
from excel.excel_writer import ExcelWriter
from logger.logger import Logger


class MainLogic:

    __slots__ = ['amount', '__logger', '__xlsx_writer', '__db_tool']

    def __init__(self, amount):
        self.amount = amount
        self.__logger = Logger(self.amount)
        self.__db_tool = DataBaseTools(self.amount)
        self.__xlsx_writer = ExcelWriter(self.__db_tool)

    def run(self) -> None:
        """
        run application steps

        :return: None
        """
        self.__logger.write()
        self.__db_tool.update_done()
        self.__xlsx_writer.write()
        self.__db_tool.close()
