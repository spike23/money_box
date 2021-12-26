import os
import subprocess


def show_results():
    path = os.path.dirname(__file__).replace('application', 'template')
    file = os.path.join(path, 'money_calendar.xlsx')
    subprocess.call(['xdg-open', file])
