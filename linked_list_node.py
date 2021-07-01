from typing import Optional


class LinkedListNode:
    """
    Класс создания элементов
    """
    def __init__(self, content, link_previous=None, link_next=None):
        self.content = content  # задать содержимое элемента
        self.link_previous = link_previous  # задать ссылка на предыдущий элемент
        self.link_next = link_next  # задать ссылка на следующий элемент


class LinkedList:
    """
    Класс создания двунаправленого связного списка
    """
    def __init__(self):
        """
        Создание списка
        При первой инициализации списка в нём нет элементов и его длина равна 0
        """
        self.first_element: Optional[LinkedListNode] = None  # задать первый элемент списка
        self.last_element: Optional[LinkedListNode] = None  # задать последний элемент списка
        self.length: int = 0  # задать длину списка

    def append(self, element: LinkedListNode):
        """
        Добавление элемента в конец списка

        :param element: принимает в качестве параметра элемент класса LinkedListNode для добавления
        :return: в конец списка добавлен элемент и длина списка увеличена на 1
        """
        if self.first_element is None:  # если список пуст
            self.first_element = element  # назначить новый элемент на первую позицию списка
            self.last_element = element  # назначить новый элемент на последнюю позицию списка
        else:
            self.last_element.link_next = element  # прилинковыть новый элемент в качесте следующего к последнему элементу списка
            element.link_previous = self.last_element  # прилинковать последний элемент списка в качестве предыдущего к новому элементу
            self.last_element = element  # назначить новый элемент на последнюю позицию списка
        self.length += 1  # увеличить длину списка

    def prepend(self, element: LinkedListNode):
        """
        Добавление элемента в начало

        :param element: принимает в качестве параметра элемент класса LinkedListNode для добавления
        :return: в начало списка добавлен элемент и длина списка увеличена на 1
        """
        if self.first_element is None:  # если список пуст
            self.first_element = element  # назначить новый элемент на первую позицию списка
            self.last_element = element  # назначить новый элемент на последнюю позицию списка
        else:
            self.first_element.link_previous = element  # прилинковыть новый элемент в качесте предыдущего к первому элементу списка
            element.link_next = self.first_element  # прилинковать первый элемент списка в качестве следующего к новому элементу
            self.first_element = element  # назначить новый элемент на первую позицию списка
        self.length += 1  # увеличить длину списка

    def put(self, element: LinkedListNode, index: int):
        """
        Добавление элемента на позицию по индексу
        Новый элемент встаёт на нужный индекс сдвигая к концу последующие элементы

        :param element: принимает в качестве параметра элемент класса LinkedListNode для добавления
        :param index: принимает в качестве параметра натуральное число
        :return: на требуемую позицию добавлен элемент и длина списка увеличена на 1
        """
        try:
            index_element = self[index]  # вызов элемента из списка по требуемому индексу
            previous_element = index_element.link_previous  # вызов предыдущего элемента
            previous_element.link_next = element  # прилинковать новый элемент в качестве следующего к предыдущему элементу списка
            index_element.link_previous = element  # прилинковать новый элемент в качестве предыдущего к элементу на требуемом индексе
            element.link_previous = previous_element  # прилинковать предыдущий элемент списка в качестве предыдущего к новому элементу
            element.link_next = index_element  # прилинковать элемент на требуемом индексе в качестве следующего к новому элементу
            self.length += 1  # увеличение длины списка
        except AttributeError:
            return None

    def replace(self, element: LinkedListNode, index: int):
        """
        Замена элемента на требуемой позиции
        Новый элемент встаёт на нужный индекс, заменяя имеющийся на заданной позиции элемент

        :param element: принимает в качестве параметра элемент класса LinkedListNode для добавления
        :param index: принимает в качестве параметра натуральное число
        :return: на требуемую позицию установлен элемент
        """
        try:
            index_element = self[index]  # вызов элемента из списка по требуемому индексу
            previous_element = index_element.link_previous  # вызов предыдущего элемента
            next_element = index_element.link_next  # вызов следующего элемента
            previous_element.link_next = element  # прилинковать новый элемент в качестве следующего к предыдущему элементу списка
            next_element.link_prev = element  # прилинковать новый элемент в качестве предыдущего к следующему элементу списка
            element.link_previous = previous_element  # прилинковать предыдущий элемент списка в качестве предыдущего к новому элементу
            element.link_next = next_element  # прилинковать следующий элемент в качестве следующего к новому элементу списка
        except AttributeError:
            return None

    def remove(self, index: int):
        """
        Удаление элемента с требуемой позиции

        :param index: принимает в качестве параметра натуральное число
        :return: удалён элемент с требуемой позиуии и длина списка уменьшена на 1
        """
        try:
            element = self.__getitem__(index)  # вызов элемента стребующегося индекса
            previous_element = element.link_previous  # вызов предыдущего элемента
            next_element = element.link_next  # вызов следующего элемента
            previous_element.link_next = next_element  # прилинковать следующий элемент в качестве следующего к предыдущему элементу
            next_element.link_previous = previous_element  # прилинковать предыдущий элемент в качестве предыдущего к следующему элементу
            self.length -= 1  # уменьшить длину списка
        except AttributeError:
            return None

    def pop_first(self):
        """
        Удаление первого элемента

        :return: удалён элемент из начала списка и уменьшина длина списка на 1
        """
        if self.length == 0:  # проверка длины списка
            return

        self.first_element = self.first_element.link_next  # назначение элемента, следующего за первым элементом, на первую позицию в списке
        self.first_element.link_previous = None  # удаление у первого элемента списка ссылки на предыдущий элемент
        self.length -= 1  # уменьшение длины списка

    def pop(self):
        """
        Удаление последнего элемента

        :return: удалён элемент из конца списка и уменьшина длина списка на 1
        """
        if self.length == 0:  # проверка длины списка
            return

        self.last_element = self.last_element.link_previous  # назначение элемента, предшествующего последнему элементу, на последнюю позицию списка
        self.last_element.link_next = None  # удаление у последнего элемента списка ссылки на следующий элемент
        self.length -= 1  # уменьшение длины списка

    def __iter__(self):
        """
        Итерация списка от первого элемента к последнему
        """
        element = self.first_element  # вызов первого элемента списка
        while element is not None:  # выполнение цикла пока существует вызываемый элемент
            yield element  # возвратить элемент
            element = element.link_next  # вызвать следующий элемент

    def iter_backward(self):
        """
        Итерация списка от последнего элемента к первому
        """
        element = self.last_element  # вызов последнего элемента списка
        while element is not None:  # выполнение цикла пока существует вызываемый элемент
            yield element  # возвратить элемент
            element = element.link_previous  # вызвать предыдущий элемент

    def __str__(self):
        """
        Вывести начало и конец списка
        """
        # вернуть строку с содержимым первого и последнего элемента списка
        return self.first_element.content + " " + self.last_element.content

    def __getitem__(self, index: int):
        """
        Поиск элемента по индексу

        :param index: принимает в качестве параметра натуральное число
        :return: возвращает требуемый элемент по ндексу
        """
        try:
            element_in_index = self.first_element  # получить первый элемент списка в качестве начального
            counter_index = 0  # счётчик количества элементов

            while counter_index != index:  # цикл выполняется пока счётчик не равен необходимому элементу
                element_in_index = element_in_index.link_next  # получить следующий элемент
                counter_index += 1  # увеличение счётчика
            return element_in_index  # вернуть найденый элемент
        except AttributeError:
            return None

# что будет если менять местами уже имеющиеся в списке элементы или дублировать их?

# element_1 = LinkedListNode('value 1')
# element_2 = LinkedListNode('value 2')
# element_3 = LinkedListNode('value 3')
# element_4 = LinkedListNode('value 4')
# element_5 = LinkedListNode('value 5')
# element_6 = LinkedListNode('value 6')
# element_7 = LinkedListNode('value 7')
# element_0 = LinkedListNode('value 0')
#
# list_1 = LinkedList()
# list_1.append(element_1)
# list_1.append(element_2)
# list_1.append(element_3)
# list_1.append(element_4)
# list_1.append(element_5)
