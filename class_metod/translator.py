from collections import defaultdict


class Translator:
    eng_rus = {}

    def add(self, eng, rus):
        # self.eng_rus.setdefault(eng, []).append(rus)
        self.eng_rus.setdefault(eng, [])
        if rus not in self.eng_rus[eng]:
            self.eng_rus[eng].append(rus)


    def remove(self, eng):
        self.eng_rus.pop(eng)

    def translate(self, eng):
        result = [word for word in self.eng_rus[eng]]
        return result


if __name__ == '__main__':
    tr = Translator()
    tr.add("tree", "дерево")
    tr.add("car", "машина")
    tr.add("car", "автомобиль")
    tr.add("leaf", "лист")
    tr.add("river", "река")
    tr.add("go", "идти")
    tr.add("go", "ехать")
    tr.add("go", "ходить")
    tr.add("milk", "молоко")
    tr.remove("car")
    print(*tr.translate("go"))
