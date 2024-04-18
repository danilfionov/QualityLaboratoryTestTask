import os

from faker import Faker

fake = Faker()
path_to_clients_csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "test", "python", "configuration", "csv", "clients.csv"))
path_to_env_csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "test", "python", "configuration", "csv", "env.csv"))


class CSV(object):
    """Класс для взаимодействия с .csv файлами."""

    @staticmethod
    def get_env():
        """Метод для получения значения окружения из .csv файла."""
        with open(path_to_env_csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                return row[0]