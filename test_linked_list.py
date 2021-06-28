import linked_list_node
import pytest


# def test_pytest():
#     assert (1, 2, 3) == (1, 2, 3)


@pytest.fixture(scope="module")
def create_elements():
    element_1 = linked_list_node.LinkedListNode('value 1')
    element_2 = linked_list_node.LinkedListNode('value 2')
    element_3 = linked_list_node.LinkedListNode('value 3')
    element_4 = linked_list_node.LinkedListNode('value 4')
    element_5 = linked_list_node.LinkedListNode('value 5')
    # element_6 = linked_list_node.LinkedListNode('value 6')
    # element_7 = linked_list_node.LinkedListNode('value 7')

    list_1 = linked_list_node.LinkedList()
    list_1.append(element_1)
    list_1.append(element_2)
    list_1.append(element_3)
    list_1.append(element_4)
    list_1.append(element_5)

    return list_1
    # element_1, element_2, element_3, element_4, element_5, element_6, element_7


def test_str(create_elements):
    # print(create_elements)
    assert create_elements.__str__() == "value 1 value 5"
