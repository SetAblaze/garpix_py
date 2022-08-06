class ListWorker:
    def __init__(self, *args):
        self.args = args

    def get_str_list(self):
        out_list = []
        for i in self.args:
            if isinstance(i, str):
                out_list.append(i)
        return out_list

    def get_int_list(self):
        out_list = []
        for i in self.args:
            if isinstance(i, int):
                out_list.append(i)
        return out_list

    def get_oth_list(self):
        out_list = []
        for i in self.args:
            if not isinstance(i, int) and not isinstance(i, str):
                out_list.append(i)
        return out_list

test_list = ListWorker('1', 5, 3, 2, ' hello', None)

for i in test_list.get_str_list():
    print(i)

for i in test_list.get_int_list():
    print(i)

for i in test_list.get_oth_list():
    print(i)