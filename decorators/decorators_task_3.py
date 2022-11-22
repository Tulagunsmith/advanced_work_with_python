import os
import datetime
import types


def logger(old_function):
    def new_function(*args, **kwargs):
        with open('main.log', 'a') as log_file:
            now = datetime.datetime.now()
            log_file.write(
                f'Date and time: {now.strftime("%d.%m.%Y %H:%M:%S")}\n'
                f'Function name: {old_function.__name__}\n'
                f'Arquments: {args, kwargs}\n'
                f'Return: {old_function(*args, **kwargs)}\n\n'
            )
        return old_function(*args, **kwargs)

    return new_function


@logger
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
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

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
