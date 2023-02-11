# from datetime import datetime as dt

#
# def universal_logger(data, data_description):
#     time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
#     with open('log.csv', 'a', encoding='utf-8') as file:
#         file.write(f'{time}; {data_description}; {data}\n')

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_log.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)


