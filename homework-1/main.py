"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv
import os


def get_data_from_csv(filename: str) -> list[list]:
    with open(os.path.join('north_data', filename), 'r') as csvfile:
        customers = csv.reader(csvfile)
        next(customers)

        return [tuple(row) for row in customers]


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1q2w3e'
)
try:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', get_data_from_csv('customers_data.csv'))
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                        get_data_from_csv('employees_data.csv'))
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', get_data_from_csv('orders_data.csv'))

        conn.commit()
finally:
    conn.close()
