import linked_list_node
import pytest


@pytest.fixture(scope="module")
def create_element_0():
    """
    fixture of creating element
    """
    element_0 = linked_list_node.LinkedListNode('value 0')
    return element_0


@pytest.fixture(scope="module")
def create_element_6():
    """
    fixture of creating element
    """
    element_6 = linked_list_node.LinkedListNode('value 6')
    return element_6


@pytest.fixture(scope="module")
def create_element_7():
    """
    fixture of creating element
    """
    element_7 = linked_list_node.LinkedListNode('value 7')
    return element_7


@pytest.fixture(scope="module")
def create_list():
    """
    fixture of creating linked list
    """
    element_1 = linked_list_node.LinkedListNode('value 1')
    element_2 = linked_list_node.LinkedListNode('value 2')
    element_3 = linked_list_node.LinkedListNode('value 3')
    element_4 = linked_list_node.LinkedListNode('value 4')
    element_5 = linked_list_node.LinkedListNode('value 5')

    list_1 = linked_list_node.LinkedList()
    list_1.append(element_1)
    list_1.append(element_2)
    list_1.append(element_3)
    list_1.append(element_4)
    list_1.append(element_5)

    return list_1
    # element_1, element_2, element_3, element_4, element_5


def test_str(create_list):
    """
    testing the function to display the first and last elements of a linked list
    """
    assert create_list.__str__() == "value 1 value 5"


def test_getitem(create_list):
    """
    testing the function of getting an element by index in linked list
    """
    getitem = create_list.__getitem__(2)
    assert getitem.content == "value 3"


@pytest.mark.parametrize("index", [-1, 10])
def test_getitem_return_none(create_list, index):
    """
    testing the function of getting an element by index in linked list
    """
    getitem = create_list.__getitem__(index)
    assert getitem is None


def test_iter_backward(create_list):
    """
    testing the reverse iteration function of a linked list
    """
    iter_back = []
    for x in create_list.iter_backward():
        element = x.content
        iter_back.append(element)
    assert iter_back == ["value 5", "value 4", "value 3", "value 2", "value 1"]


def test_iteration(create_list):
    """
    testing the iteration function of a linked list
    """
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 1", "value 2", "value 3", "value 4", "value 5"]


def test_pop(create_list):
    """
    testing the function of remove the last element from a linked list
    """
    create_list.pop()
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 1", "value 2", "value 3", "value 4"]


def test_pop_first(create_list):
    """
    testing the function of remove the first element from a linked list
    """
    create_list.pop_first()
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 2", "value 3", "value 4"]


def test_replace(create_list, create_element_6):
    """
    testing the function of replacing an element by index on a linked list
    """
    create_list.replace(create_element_6, 1)
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 2", "value 6", "value 4"]


@pytest.mark.parametrize("index", [-1, 10])
def test_replace_return_none(create_list, create_element_6, index):
    """
    testing the function of replacing an element by index on a linked list
    """
    assert create_list.replace(create_element_6, index) is None


def test_remove(create_list):
    """
    testing the function of removing an element by index on a linked list
    """
    create_list.remove(1)
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 2", "value 4"]


def test_put(create_list, create_element_6):
    """
    testing the function of inserting an element by index on a linked list
    """
    create_list.put(create_element_6, 1)
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 2", "value 6", "value 4"]


@pytest.mark.parametrize("index", [-1, 0, 10])
def test_put_is_none(create_list, create_element_6, index):
    """
    testing the function of inserting an element by index on a linked list
    if index is not actual
    """
    assert create_list.put(create_element_6, index) is None


def test_prepend(create_list, create_element_7):
    """
    testing the function of inserting the first element on a linked list
    """
    create_list.prepend(create_element_7)
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 7", "value 2", "value 6", "value 4"]


def test_append(create_list, create_element_0):
    """
    testing the function of inserting the last element on a linked list
    """
    create_list.append(create_element_0)
    iter_norm = []
    for x in create_list.__iter__():
        element = x.content
        iter_norm.append(element)
    assert iter_norm == ["value 7", "value 2", "value 6", "value 4", "value 0"]
