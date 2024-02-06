from pathlib import Path
import csv
import allure
from utils.months import MONTHS


def attach_csv_to_allure():
    file_csv = 'csv/result_transactions.csv'

    try:
        allure.attach.file(
            source=file_csv,
            name='result.csv',
            attachment_type=allure.attachment_type.CSV,
            extension='csv'
        )
    except Exception as error:
        print(f'Не удалось прикрепить файл к отчёту: {error}')


def add_transaction_to_csv_file(transaction):
    """Создание и прикрепление скриншота к Allure-отчёту"""

    csv_dir = Path('csv')
    csv_dir.mkdir(exist_ok=True)

    file_csv = Path('csv/result_transactions.csv')
    file_csv.touch(exist_ok=True)

    date = transaction.date.strftime('%d %B %Y')
    with open(file_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, transaction.amount, transaction.transaction_type])
        file.close()


def verify_transaction(actual_transaction, expected_transaction) -> bool:
    if actual_transaction['amount'] == expected_transaction.amount:
        if actual_transaction['type'] == expected_transaction.transaction_type:
            expected_date, actual_date = expected_transaction.date, actual_transaction['date']
            if str(expected_date.year) in actual_date:
                if MONTHS[str(expected_date.month)] in actual_date:
                    time = expected_transaction.date.strftime('%-H:%M:%S')
                    if time in actual_date:
                        add_transaction_to_csv_file(expected_transaction)
                        return True
