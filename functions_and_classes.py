
class FlatIterator:

    def __init__(self, list_of_list):
        self.lol = list_of_list

    def __iter__(self):
        self.main = 0
        self.sub = -1

        return self

    def __next__(self):
        if self.sub < len(self.lol[self.main]) - 1:
            self.sub += 1
        else:
            self.main += 1
            self.sub = 0
        if self.main == len(self.lol):
            raise StopIteration
        item = self.lol[self.main][self.sub]
        return item


def flat_generator(list_of_lists):
    main_counter = 0
    sub_counter = 0
    while main_counter < len(list_of_lists):
        while sub_counter < len(list_of_lists[main_counter]):
            res = list_of_lists[main_counter][sub_counter]
            yield res
            sub_counter += 1
        sub_counter = 0
        main_counter += 1

