class FlatIterator:

    def __init__(self, list_of_list):
        self.complex_list = self.flat_list(list_of_list)
        self.count = 0
        self.item = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.complex_list):
            raise StopIteration
        else:
            self.item = self.complex_list[self.count]
            self.count += 1
        return self.item

    def flat_list(self, complex_list):
        flag = True
        copy_list = complex_list[:]
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
        return copy_list


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test()
    test_3()
