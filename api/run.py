import os
import sys
from application.app_logic import MainLogic
from application.utils import show_results


def run_money_box() -> None:
    """
    run application

    :return: None
    """
    try:
        amount = sys.argv[1]
    except IndexError:
        amount = int(input('PLease specify amount: '))

    MainLogic(amount).run()
    show_results()
