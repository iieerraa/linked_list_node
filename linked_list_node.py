from typing import Optional


class LinkedListNode:  # класс элементов списка
    def __init__(self, content, link_previous=None, link_next=None):
        self.content = content  # содержимое элемента
        self.link_previous = link_previous  # ссылка на предыдущий элемент
        self.link_next = link_next  # ссылка на следуЮщий элемент


class LinkedList:  # класс списков
    def __init__(self):
        self.first_element: Optional[LinkedListNode] = None
        self.last_element: Optional[LinkedListNode] = None
        self.length: int = 0

    def append(self, element: LinkedListNode):
        """
        Dobavlenie elimenta v konec spiska
        """
        if self.first_element is None:  # усли список пуст
            self.first_element = element  # назначить элемент на первую позицию
            self.last_element = element  # назначить элемент на последнюю позицию
        else:
            self.last_element.link_next = element  # ссылка на следующий элемент
            element.link_previous = self.last_element  # ссылка на предыдущий элемент
            self.last_element = element  # определение элемента на последнюю позицию
        self.length += 1  # увеличение длины списка

    def prepend(self, element: LinkedListNode):
        """
        Dobavlenie pervogo elementa
        """
        if self.first_element is None:  # если список пуст
            self.first_element = element  # назначить элемент на первую позицию
            self.last_element = element  # назначить элемент на последнюю позицию
        else:
            self.first_element.link_previous = element  # ссылка на предыдущий элемент
            element.link_next = self.first_element  # ссылка на следующтй элемент
            self.first_element = element  # назначение первого элемента
        self.length += 1  # увеличение длины списка

    def put(self, element, position):
        """
        Dobavlenie na kakuju-to poziciju
        """
        if position > self.length or self.length == 0:  # проверка наличия требуемой позиции
            return None

        position_element = self[position]  # получение элемента на требуемой позиции
        previous_element = position_element.link_previous  # получение предыдущего элемента
        previous_element.link_next = element  # ссылка на следующий элемент
        position_element.link_previous = element  # ссылка на предыдущий элемент
        element.link_previous = previous_element  # ссылка на предыдущий элемент
        element.link_next = position_element  # ссылка на следующий элемент
        self.length += 1  # увеличение длины списка

    def replace(self, element, position):
        """
        Замена элемента на требуемой позиции
        """
        if position > self.length or self.length == 0:  # проверка наличия требуемой позиции
            return None

        position_element = self[position]  # получение элемента на требуемой позиции
        previous_element = position_element.link_previous  # получение предыдущего элемента
        next_element = position_element.link_next  # получение следующего элемента
        previous_element.link_next = element  # ссылка на следующий элемент
        next_element.link_prev = element  # ссылка на предыдущий элемент
        element.link_previous = previous_element  # ссылка на прудыдущий элемент
        element.link_next = next_element  # ссылка на следующтй элемент

    def remove(self, position):
        """
        Удаление элемента с позиции
        """
        if position > self.length or self.length == 0:  # проверка наличия требуемой позиции
            return None

        element = self.__getitem__(position)  # получение элемента на требуемой позиции
        previous_element = element.link_previous  # получение предыдущего элемента
        next_element = element.link_next  # получение следующего элемента
        previous_element.link_next = next_element  # ссылка на следующий элемент
        next_element.link_previous = previous_element  # ссылка на поредыдущий элемент
        self.length -= 1  # уменьшегние длины списка

    def pop_first(self):
        """
        Удаление первого элемента
        """
        if self.length == 0:  # проверка длины списка
            return

        self.first_element = self.first_element.link_next  # назначение первого элемента
        self.first_element.link_previous = None  # ссылка на предыдущий элемент
        self.length -= 1  # уменьшение длины списка

    def pop(self):
        """
        Удаление последнего элемента
        """
        if self.length == 0:  # проверка длины списка
            return

        self.last_element = self.last_element.link_previous  # назначение последнего элемента
        self.last_element.link_next = None  # ссылка на последний элемент
        self.length -= 1  # уменьшение длины списка

    def __iter__(self):
        """
        Итерация списка от первого элемента к последнему
        """
        element = self.first_element  # получение элемента
        while element is not None:  # если элемент существует
            yield element  # вернуть элемент
            element = element.link_next  # получение следующего элемента для итерации

    def iter_backward(self):
        """
        Итерация от последнего элемента к первому
        """
        element = self.last_element  # получение элемента
        while element is not None:  # если элемент существует
            yield element  # вернуть элемент
            element = element.link_previous  # получение предыдущего элемента для итерации

    def __str__(self):
        """
        Вывести начало и конец списка
        :return:
        """
        return self.first_element.content + " " + self.last_element.content

    def __getitem__(self, index):
        """
        Поиск элемента по индексу
        :param index:
        :return:
        """
        counter_index = 1  # счётчик количества элементов
        element_in_index = self.first_element  # получение индексируемого элемента
        if index > self.length or self.length == 0:  # проверка наличия требуемой позиции
            return None

        while counter_index != index:  # пока счётчик не равен неоБходимому элементу
            element_in_index = element_in_index.link_next  # получение следующего элемента
            counter_index += 1  # увеличение счётчика
        return element_in_index  # вернуть найденый элемент


# element_1 = LinkedListNode('value 1')
# element_2 = LinkedListNode('value 2')
# element_3 = LinkedListNode('value 3')
# element_4 = LinkedListNode('value 4')
# element_5 = LinkedListNode('value 5')
# element_6 = LinkedListNode('value 6')
# element_7 = LinkedListNode('value 7')
#
# list_1 = LinkedList()
# list_1.append(element_1)
# list_1.append(element_2)
# list_1.append(element_3)
# list_1.append(element_4)
# list_1.append(element_5)
#
# print('вывод первого и последнего элементов списка')
# print(list_1)  # вывод первого и последнего элементов списка

# print('вывод обратной итерации списка')
# for x in list_1.iter_backward():  # вывод итерации списка
#     print(x.content)

# print('вывод итерации списка')
# for x in list_1:  # вывод итерации списка
#     print(x.content)

# print('вывод элемента по индексу')
# print(list_1[6])  # вывод элемента по индексу
# print(list_1[3].content)

# print('put')
# list_1.put(element_6, 3)
# print('вывод первого и последнего элементов списка')
# print(list_1)
# print('вывод итерации списка')
# for x in list_1:
#     print(x)

# создать итерацию списка по срезу с шагом
# for x in list_1[1:3:-1]:
#     print(x)
