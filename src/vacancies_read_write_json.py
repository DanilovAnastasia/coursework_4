import os
from pathlib import Path
from src.vacancies_read_write import VacanciesReadWrite
from src.vacancy import Vacancy
import json


class VacanciesReadWriteJson(VacanciesReadWrite):
    """
    Дочерний класс для работы с файлом json. А также отвечающий за фильтрацию, и другой функционал с вакансиями.
    Данный класс реализует запись и чтение вакансий из файла.
    """
    out_root_path = Path(__file__).parent.parent

    def __init__(self, list_vacancies=None):
        """
        Конструктор класса, с одним атрибутом
        file_path: путь к файлу.
        """
        self.file_path = os.path.join(self.out_root_path, 'data', "vacancies.json")
        if list_vacancies is None:
            list_vacancies = []
        self.list_vacancies = self.list_convert(list_vacancies)

    def vacancies_write(self, vacancies) -> None:
        """Абстрактный метод для записи."""
        with open(self.file_path, 'w', encoding='UTF-8') as file:
            json.dump([*vacancies], file, indent=4, ensure_ascii=False)

    def vacancies_read(self) -> list:
        """Абстрактный метод для чтения."""
        try:
            with open(self.file_path, 'r', encoding='UTF-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print('file_not_found')
            return []
        except json.decoder.JSONDecodeError:
            return []

    @staticmethod
    def list_convert(list_vacancies, reverse=False) -> list or None:
        """
        Метод конвертирующий список вакансий из словарей в экземпляры класса вакансий или обратно
        """
        if list_vacancies is None:
            return None
        if reverse:
            list_vacancies = [vacancy.vacancy_to_dict() for vacancy in list_vacancies]
        else:
            list_vacancies = [Vacancy(dic_vacancy) for dic_vacancy in list_vacancies]
        return list_vacancies

    def print_vacancies(self) -> None:
        """
        Метод для печати вакансий.
        """
        for vacancy in self.list_vacancies:
            print(vacancy)

    def get_top_n(self, n) -> None:
        """
        Метод для получения топ n вакансий.
        """
        self.list_vacancies.sort(reverse=True)
        self.list_vacancies = self.list_vacancies[:min(n, len(self.list_vacancies) - 1)]
        self.print_vacancies()

    @staticmethod
    def unique_vacancies(vacancies_all) -> list:
        ids_vacancies = [vacancy.id for vacancy in vacancies_all]
        ids_vacancies_unique = list(set(ids_vacancies))
        vacancy_unique = []
        for vacancy in vacancies_all:
            if vacancy.id in ids_vacancies_unique:
                vacancy_unique.append(vacancy)
                ids_vacancies_unique.remove(vacancy.id)
        return vacancy_unique

    def add_new_vacancies(self) -> None:
        """
        Метод для добавления вакансий в файл.
        """
        vacancies_from_file = self.vacancies_read()
        vacancies_from_file = self.list_convert(vacancies_from_file)
        vacancies_all = self.list_vacancies + vacancies_from_file
        vacancies_unique = self.unique_vacancies(vacancies_all)
        vacancies_unique = self.list_convert(vacancies_unique, reverse=True)
        self.vacancies_write(vacancies_unique)

    def delete_vacancies(self) -> None:
        vacancies_from_file = self.vacancies_read()
        vacancies_from_file = self.list_convert(vacancies_from_file)
        vacancies_unique = self.unique_vacancies(vacancies_from_file)
        ids_vacancies = [vacancy.id for vacancy in self.list_vacancies]
        ids_vacancies_unique = list(set(ids_vacancies))

        list_after_delete_vacancies = []
        for vacancy in vacancies_unique:
            if vacancy.id not in ids_vacancies_unique:
                list_after_delete_vacancies.append(vacancy)
        list_after_delete_vacancies = self.list_convert(list_after_delete_vacancies, reverse=True)
        self.vacancies_write(list_after_delete_vacancies)
