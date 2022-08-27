import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for i in range(len(fields)):
            setattr(self, fields[i], lst_values[i])
        #     self.__dict__.update(zip(fields, lst_values))
        return True

    # 2 вариант ===============================
    # def create(self, fields, lst_values):
    #     if len(fields) != len(lst_values):
    #         return False
    #
    #     for i, key in enumerate(fields):
    #         setattr(self, key, lst_values[i])
    #         # 0: id
    #         # 1: fields
    #         # 2: jopa
    #     return  True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__)
