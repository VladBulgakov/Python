# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:54:04 2022

@author: Владислав
"""
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial


import logging
import mymodlog


def main():
    # Тест logging
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S',
                        filename='log_example.txt', encoding='utf-8',
                        level=logging.DEBUG, filemode='w')
    logging.debug('Это сообщение gebug')
    logging.info('Это сообщение info')
    logging.warning('Это сообщение warning')
    logging.error('Это сообщение error')
    logging.critical('Это сообщение critical')
    mymodlog.myfun('Hello!')

if __name__ == '__main__':
    main()
