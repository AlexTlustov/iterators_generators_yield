
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.start = -1
        self.end = len(list_of_list)

    def __iter__(self):
        self.list_iterator = iter(self.list_of_list)
        self.list = []
        return self

    def __next__(self):
        self.start += 1
        if self.start != self.end:
            
            if next(self.list_iterator):
                self.list = next(self.list_iterator)



list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


for i in FlatIterator(list_of_lists_2):
    print(i)


# def test_3():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# if __name__ == '__main__':
#     test_3()