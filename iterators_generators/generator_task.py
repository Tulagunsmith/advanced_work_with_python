import types


def flat_generator(list_of_lists):
    copy_list = list_of_lists[:]
    # print(copy_list)
    flag = True
    while flag:
        new_list = []
        flag = False
        for i in copy_list:
            # print(f' for {new_list}')
            if isinstance(i, list):
                new_list.extend(i)
                # print(f' instanse {new_list}')
                flag = True
            else:
                new_list.append(i)
        # print(new_list)
        copy_list = new_list

    yield copy_list


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
if __name__ == '__main__':
    a = flat_generator(list_of_lists_1)
    for item in a:
        print(item)
    # print(flat_generator(list_of_lists_1))
    # print(isinstance(flat_generator(list_of_lists_1), types.GeneratorType))
    test_2()
