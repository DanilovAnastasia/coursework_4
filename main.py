from src.functions import input_from_user_for_load, load_data_from_network, actions_with_vacancies, actions_with_vacancies_from_file


if __name__ == '__main__':
    while True:
        inp = input(str(
            '\nПривет, вы используете программу для работы с вакансиями с HH.\n'
            'Введите:Загрузить вакансии с сайта HH.\n'
            '1 - если хотите загрузить новые вакансии, по условию.\n'
            '2 - если хотите посмотреть/поработать с вакансиями из файла.\n'
            '3 - если хотите завершить.\n'
            '-> '))
        if inp == '1':
            dict_criteria = input_from_user_for_load()
            list_vacancies = load_data_from_network(dict_criteria)
            actions_with_vacancies(list_vacancies)
        elif inp == '2':
            actions_with_vacancies_from_file()
        elif inp == '3':
            print('Завершение программы.')
            break
        else:
            print('Вы ввели некорректные данные.')
