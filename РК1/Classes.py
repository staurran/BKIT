class Computer:
    """
        класс Компьютер
        id: id компьютера
        name: название модели
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Program:
    """
        класс Программа
        id: id программы
        name: название программы
        size: размер
        com_id: id компьютера, на котором установлена программа
    """
    def __init__(self, id, name, size, com_id):
        self.id = id
        self.name = name
        self.size = size
        self.com_id = com_id


class ProCom:
    """
    Класс программы-коспьютеры
    id_com: id компьютера
    id_prog: id программы
    """
    def __init__(self, id_com, id_prog):
        self.id_comp = id_com
        self.id_prog = id_prog
