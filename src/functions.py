from src.hh_api import HeadHunterAPI
from src.vacancies_read_write_json import VacanciesReadWriteJson


def input_from_user_for_load():
    """
    Метод запрашивающие с консоли название вакансии, и опыт работы.
    :return: желаемое имя вакансии, и опыт.
    """

    list_of_dict_input = [
        {'str_input': 'Введите название вакансии для поиска', 'type_input': 'Текст',
         'key_name_criteries': "name_vacancy"},
        {'str_input': 'Введите желаемый опыт работы в годах', 'type_input': 'Целое число',
         'key_name_criteries': "experience_vacancy"},
        # {'str_input': 'Введите сколько топовых вакансий вы хотите', 'type_input': 'Целое число', 'key_name_criteries': "top_n_vacancy"},
    ]

    dict_criteria = {}

    for dict_input in list_of_dict_input:
        input_value = input(f"{dict_input['str_input']} |{dict_input['type_input']}|")
        if input_value == "":
            dict_criteria[dict_input['key_name_criteries']] = None
        elif dict_input['type_input'] == 'Текст':
            dict_criteria[dict_input['key_name_criteries']] = input_value
        elif dict_input['type_input'] == 'Целое число':
            try:
                dict_criteria[dict_input['key_name_criteries']] = int(float(input_value))
            except ValueError("Невозможно преобразовать строку в натуральное число"):
                return None
    return dict_criteria


def load_data_from_network(dict_criteria):
    """
    Функция для загрузки вакансий с какого-либо портала по критериям пользователя.
    :param: dict_criteria Словарь параметров поиска.
    :return: Список Вакансий.
    """

    headhunterapi = HeadHunterAPI(dict_criteria)
    list_vacancies = headhunterapi.get_vacancies()
    return list_vacancies


def actions_with_vacancies(list_vacancies):
    """
    Функция для различных действий с вакансиями.
    """
    vacancies_read_write_json = VacanciesReadWriteJson(list_vacancies)
    while True:
        inp_1 = input(str(
            '\nКакие действия хотите с загруженными вакансиями.\n'
            '1 - Вывести в консоль.\n'
            '2 - Выбрать топ N вакансий\n'
            '3 - Добавить выбранные вакансии в файл.\n'
            '4 - если хотите завершить.\n'
            '-> '))
        if inp_1 == '1':
            vacancies_read_write_json.print_vacancies()
        elif inp_1 == '2':
            while True:
                n = input(str('\nВведите число N (топ вакансий по зп)\n->'))
                try:
                    n = int(float(n))
                    break
                except ValueError:
                    print('Ввели некорректное значение.')
            vacancies_read_write_json.get_top_n(n)
        elif inp_1 == '3':
            vacancies_read_write_json.add_new_vacancies()
        elif inp_1 == '4':
            print('Завершение программы.')
            break
        else:
            print('Вы ввели некорректные данные.')


def actions_with_vacancies_from_file():
    """
    Функция для различных действий с вакансиями из файла.
    """
    vacancies_read_write_json = VacanciesReadWriteJson()
    vacancies_from_file = vacancies_read_write_json.vacancies_read()
    vacancies_from_file = vacancies_read_write_json.list_convert(vacancies_from_file)
    vacancies_read_write_json.list_vacancies = vacancies_from_file
    while True:
        inp_1 = input(str(
            '\nКакие действия хотите сделать.\n'
            '1 - Вывести в консоль вакансии.\n'
            '2 - Выбрать топ N вакансий\n'
            '3 - Удалить выбранные вакансии из файла.\n'
            '4 - если хотите завершить.\n'
            '-> '))
        if inp_1 == '1':
            vacancies_read_write_json.print_vacancies()
        elif inp_1 == '2':
            while True:
                n = input(str('\nВведите число N (топ вакансий по зп)\n->'))
                try:
                    n = int(float(n))
                    break
                except ValueError:
                    print('Ввели некорректное значение.')
            vacancies_read_write_json.get_top_n(n)
        elif inp_1 == '3':
            vacancies_read_write_json.delete_vacancies()
        elif inp_1 == '4':
            print('Завершение программы.')
            break
        else:
            print('Вы ввели некорректные данные.')
    # vacancies_read_write_json = VacanciesReadWriteJson()

# print(input_from_user_for_load())
