from abc import ABC, abstractmethod


class VacanciesReadWrite(ABC):
    """
    Абстрактный класс для работы добавления вакансий.
    Данный класс реализует запись и чтение вакансий из фалйа.
    """

    @abstractmethod
    def vacancies_write(self, vacancies) -> None:
        """Абстрактный метод для записи."""
        pass

    @abstractmethod
    def vacancies_read(self) -> None:
        """Абстрактный метод для чтения."""
        pass
