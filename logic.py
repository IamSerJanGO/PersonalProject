import pickle
from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class NewValue(Field):
    def __init__(self, value):
        if not value:
            raise ValueError('нет входных данных')
        super().__init__(value)


class GenerateDays:
    def generate(self):
        today = datetime.now().date()
        next_10_days = [today + timedelta(days=i) for i in range(10)]
        result = {}

        for day in next_10_days[3:]:
            result[day.strftime('%Y-%m-%d')] = {'time': {'10:00': None, '11:00': None}}

        return result

    def __str__(self):
        return str(self.result)


class CustomRecordBook:
    """
    Класс реализующий доп-функции чтобы не загромождать код
    """

    def get_days_value(self, data):
        days_list = list(data.keys())
        return days_list

    def get_time_value(self, data, day):
        time_list = []
        for key, value in data[day]['time'].items():
            if value is None:
                time_list.append(key)
        return time_list

    def del_finish_day(self, data: dict):
        today = str(datetime.now().date())
        days_to_remove = []

        for day, _ in data.items():
            if day < today:
                days_to_remove.append(day)

        for day in days_to_remove:
            del data[day]



class RecordBook(UserDict):
    def __init__(self):
        super().__init__()
        self.custom_functions = CustomRecordBook()

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}

    def add_days(self, value):
        """
        Функция расширяющая словарь дней для записи
        :param value: Словрь записи на неделю вперед
        :return:
        """
        if isinstance(value, NewValue):
            self.data.update(value.value)
        else:
            raise TypeError('Неверный тип объекта. Ожидается NewValue.')

    def add_record(self, day, time, user_id):

        """
        Позволяет юзеру записаться на прием
        :param day: день записи
        :param time: время записи
        :param user_id: его ID-пользователя
        :return:
        """

        if day in self.data:
            if time in self.data[day]['time']:
                self.data[day]['time'][time] = user_id
            else:
                raise ValueError('Время записи недоступно')
        else:
            raise ValueError('День для записи недоступен')

    def del_record(self, day, time):
        """
        Позволяет пользователю отменить запись
        :param day: день на который он записан
        :param time: Время его записи
        :return:
        """
        if day in self.data:
            if time in self.data[day]['time']:
                self.data[day]['time'][time] = None
            else:
                raise ValueError('Время записи недоступно')
        else:
            raise ValueError('День для записи недоступен')

    def del_day(self, day):
        """
        Удаляет день из рабочей недели
        :param day: День которій необходимо удалить из рабочей недели
        :return:
        """
        if day in self.data:
            del self.data[day]
        else:
            raise ValueError('Даты для записи не существует')

    def del_time_record(self, day, time):
        """
        Удаляет запись из из дня
        :param day: день  из которого нужно удалить щапись
        :param time: время записи которое нужно удалить
        :return:
        """
        if day in self.data:
            if time in self.data[day]['time']:
                del self.data[day]['time'][time]
            else:
                raise ValueError('Время записи недоступно')
        else:
            raise ValueError('День для записи недоступен')

    def del_finish_day(self):
        self.custom_functions.del_finish_day(self.data)


    def get_day_value(self):
        """
        Функция создания кнопок для выбора дня записи
        :return:  Спасиок возможных дней для записи
        """
        result = self.custom_functions.get_days_value(self.data)
        return result

    def get_time_value(self, day):
        result = self.custom_functions.get_time_value(self.data, day)
        return result

    def __str__(self):
        return str(self.data)


book = RecordBook()
a = GenerateDays()
result = a.generate()
b = NewValue(result)
book.add_days(b)
book.add_record('2023-11-02', '11:00', 123445)
book.add_record('2023-11-01', '11:00', 44444)
book.del_time_record('2023-11-01', '10:00')
print(book)
book.del_record('2023-11-01', '11:00')
book.del_day('2023-11-04')
result3 = book.get_time_value('2023-11-05')
result2 = book.get_day_value()
print(result2)
print(book)
print(result3)
