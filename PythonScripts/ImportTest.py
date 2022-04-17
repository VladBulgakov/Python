# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:27:16 2022

@author: Владислав
"""

import webbrowser

importedval = 'Строка из импортированного модуля'
print('Эта команда выполняется при импорте и запуске модуля')
print(f'Этот модуль имеет имя {__name__}')


def OpenWebsite(url):
    # webbrowser.register('Opera', None, webbrowser.BackgroundBrowser(r'C:\Users\Владислав\AppData\Local\Programs\Opera\launcher.exe'))
    webbrowser.open(url, new=2)


if __name__ == '__main__':
    print('Этот код выполнится, если мы непосредственно запускаем модуль')
    pass  # Команда ничего не делает
    print('После pass выполнение продолжается')
    assert len(importedval) == 33, 'importedval имеет длину не 33 символа!'