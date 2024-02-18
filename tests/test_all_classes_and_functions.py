import pytest
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.vacancies_read_write_json import VacanciesReadWriteJson


@pytest.fixture
def test_job_api_init():
    return HeadHunterAPI({'name_vacancy': 'python', 'experience_vacancy': 5, 'top_n_vacancy': 10})


def test_get_headers(test_job_api_init):
    assert test_job_api_init.get_headers() == {'User-Agent': 'api-test-agent'}


@pytest.fixture
def test_vacancy1():
    return Vacancy({'id': '3214151', 'name': 'Backend-разработчик на Python', 'address': 'Не указан',
                    'salary': {'from': 150000, 'to': 200000, 'currency': 'RUR'}, 'experience': 'between3And6',
                    'url': 'https://hh.ru/vacancy/92935405'})


@pytest.fixture
def test_vacancy2():
    return Vacancy({'id': '3214151', 'name': 'Backend-разработчик на Python', 'address': 'Не указан',
                    'salary': {'from': 150000, 'to': 200000, 'currency': 'RUR'}, 'experience': 'between3And6',
                    'url': 'https://hh.ru/vacancy/92935405'})


def test_mean_salary(test_vacancy1, test_vacancy2):
    assert test_vacancy1.mean_salary(test_vacancy2) == ((150000 + 200000)/2, (150000 + 200000)/2)


@pytest.fixture
def test_vacancies_read_write_json():
    return VacanciesReadWriteJson([
    {
        "id": "92680997",
        "name": "Middle/Middle+ DevOps-инженер",
        "address": "Не указан",
        "salary": {
            "from": 220000,
            "to": 300000,
            "currency": "RUR"
        },
        "experience": "between1And3",
        "url": "https://hh.ru/vacancy/92680997"
    },
    {
        "id": "92683397",
        "name": "python man",
        "address": "Не указан",
        "salary": {
            "from": 12333,
            "to": 32111,
            "currency": "RUR"
        },
        "experience": "between1And3",
        "url": "https://hh.ru/vacancy/92680991"
    }
])


def test_read_write_json(test_vacancies_read_write_json):
    assert test_vacancies_read_write_json.unique_vacancies(test_vacancies_read_write_json.list_vacancies) == test_vacancies_read_write_json.list_vacancies
    assert test_vacancies_read_write_json.list_convert(None) is None
    assert test_vacancies_read_write_json.list_convert(test_vacancies_read_write_json.list_vacancies, reverse=True) == [
        {
            "id": "92680997",
            "name": "Middle/Middle+ DevOps-инженер",
            "address": "Не указан",
            "salary": {
                "from": 220000,
                "to": 300000,
                "currency": "RUR"
            },
            "experience": "between1And3",
            "url": "https://hh.ru/vacancy/92680997"
        },
        {
            "id": "92683397",
            "name": "python man",
            "address": "Не указан",
            "salary": {
                "from": 12333,
                "to": 32111,
                "currency": "RUR"
            },
            "experience": "between1And3",
            "url": "https://hh.ru/vacancy/92680991"
        }
    ]

