import types


def flat_generator(list_of_lists):
    copy_list = list_of_lists[:]
    flag = True
    while flag:
        new_list = []
        flag = False
        for i in copy_list:
            if isinstance(i, list):
                new_list.extend(i)
                flag = True
            else:
                new_list.append(i)
        copy_list = new_list
    yield from copy_list


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
