class Vacancy:
    """Класс для информации о вакансии и оперециями с вакансиями, сравнение и др. стандартные методы"""

    def __init__(self, dict_vacancy: dict) -> None:
        """
        Конструктор
        :param dict_vacancy - словарь с информацией о вакансии.
        """

        self.dict_vacancy = dict_vacancy
        self.id = dict_vacancy['id']
        self.name = self.dict_vacancy['name']
        self.address = self.dict_vacancy['address']
        self.salary_from = 0 if self.dict_vacancy['salary']['from'] is None else self.dict_vacancy['salary']['from']
        self.salary_to = 0 if self.dict_vacancy['salary']['to'] is None else self.dict_vacancy['salary']['to']
        self.salary_currency = (0 if self.dict_vacancy['salary']['currency'] is None
                                else self.dict_vacancy['salary']['currency'])
        self.experience = self.dict_vacancy['experience']
        self.url = self.dict_vacancy['url']

    def mean_salary(self, other: object) -> tuple[float, float]:
        other_salary_from = 0 if other.dict_vacancy['salary']['from'] is None else other.dict_vacancy['salary']['from']
        other_salary_to = 0 if other.dict_vacancy['salary']['to'] is None else other.dict_vacancy['salary']['to']
        other_salary_mean = (other_salary_from + other_salary_to) / 2
        self_salary_mean = (self.salary_from + self.salary_to) / 2
        return self_salary_mean, other_salary_mean

    def __str__(self) -> str:
        """Магический метод, строка информация о вакансии."""
        if all(map(lambda x: x == 0, [self.salary_from, self.salary_to, self.salary_currency])):
            return f'Вакансия: {self.name}, зарплата не указана. Опыт: {self.experience}. Ссылка на вакансию: {self.url}'
        else:
            return f'Вакансия: {self.name}, зарплата {self.salary_from}-{self.salary_to} {self.salary_currency} (средняя {(self.salary_from + self.salary_to) / 2}) Опыт: {self.experience}. Ссылка на вакансию: {self.url}'

    def __repr__(self) -> str:
        """Магический метод, строка информация о классе."""
        return f'Имя класса: {self.__class__.__name__}. Основные атрибуты класса: {self.id=}, {self.name=}, {self.address=}, {self.salary_from=}, {self.salary_to=}, {self.salary_currency=}, {self.experience=}, {self.url=},'

    def __gt__(self, other: object) -> bool:
        """Метод > """
        mean_self, mean_other = self.mean_salary(other)
        return mean_self > mean_other

    def __eq__(self, other: object) -> bool:
        """Метод == """

        mean_self, mean_other = self.mean_salary(other)
        return mean_self == mean_other

    # Methods classes
    def vacancy_to_dict(self) -> dict:
        """Метод, который возвращает вакансию dict."""
        dict_vacancy = {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'salary': {'from': self.salary_from, 'to': self.salary_to, 'currency': self.salary_currency},
            'experience': self.experience,
            'url': self.url,
        }
        return dict_vacancy


# v1 = Vacancy({'id': '3214151', 'name': 'Backend-разработчик на Python', 'address': 'Не указан', 'salary': {'from': 150000, 'to': 200000, 'currency': 'RUR'}, 'experience': 'between3And6', 'url': 'https://hh.ru/vacancy/92935405'})
# v2 = Vacancy({'name': 'Backend-разработчик на Python', 'address': 'Не указан', 'salary': {'from': 150000, 'to': 200000, 'currency': 'RUR'}, 'experience': 'between3And6', 'url': 'https://hh.ru/vacancy/92935405'})
# print(repr(v1))
#
# print(v1 == v2)