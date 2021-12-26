import datetime
import os
import attr


class Logger:

    __slots__ = ['date', 'path', 'file_name', 'amount']

    def __init__(self, amount):
        self.date = datetime.datetime.now()
        self.path = os.path.dirname(__file__)
        self.amount = amount
        self.__post_init__()

    @property
    def curr_month(self) -> str:
        return self.date.strftime("%B")

    @property
    def file_path(self) -> str:
        return os.path.join(self.path, 'logs')

    def __post_init__(self) -> attr:
        setattr(Logger, 'file_name', os.path.join(self.file_path, f'{self.curr_month}.log'.lower()))

    def write(self) -> None:
        """
        write log files
        :return: None
        """
        os.makedirs(self.file_path, exist_ok=True)
        with open(self.file_name, 'a') as f:
            if self.amount is None:
                raise ValueError('Amount cannot be None.')
            f.write(f'{self.date} - {self.amount} UAH was added to money box.\n')
