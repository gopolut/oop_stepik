class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]  # будут взяты первые 4 элемента

    def count_mem(self):
        ram_list = []
        for i in self.mem_slots:
            ram_list.append(f'{i.name} - {i.volume}')
        return 'Память: ' + '; '.join(map(str, ram_list))

    def get_config(self):
        system = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            self.count_mem()
        ]

        print(system)


if __name__ == '__main__':
    mb = MotherBoard(
        'Gigabyte',
        CPU('INTEL Core i7', 3.7),
        Memory('Kingston', 8), Memory('Kingston_2', 8),
    )
    mb.get_config()
