import Classes


computers = [
    Classes.Computer(1, 'Asus'),
    Classes.Computer(2, 'HP'),
    Classes.Computer(3, 'Mac'),
    Classes.Computer(4, 'Acer')
]

programs = [
    Classes.Program(1, 'Sims4', 6, 1),
    Classes.Program(2, 'Minecraft', 4, 1),
    Classes.Program(3, 'Overcooked2', 3, 2),
    Classes.Program(4, 'NFS Head', 50, 2),
    Classes.Program(5, 'GTA', 65, 2),
    Classes.Program(6, 'Diablo3', 25, 3),
    Classes.Program(7, 'Doom Eternal', 50, 3),
    Classes.Program(8, 'Outlast', 6, 4),
    Classes.Program(9, 'Resident Evil', 45, 4),
    Classes.Program(10, 'The Last of us2', 78, 4)
]


computer_program = [
    Classes.ProCom(1, 1),
    Classes.ProCom(1, 2),
    Classes.ProCom(1, 3),
    Classes.ProCom(1, 6),
    Classes.ProCom(2, 2),
    Classes.ProCom(2, 4),
    Classes.ProCom(2, 9),
    Classes.ProCom(2, 10),
    Classes.ProCom(3, 3),
    Classes.ProCom(3, 4),
    Classes.ProCom(3, 5),
    Classes.ProCom(3, 6),
    Classes.ProCom(4, 7),
    Classes.ProCom(4, 8),
    Classes.ProCom(4, 3),
    Classes.ProCom(4, 6)
]


def main():
    print('task1')
    task1_list = {comp.name: [prog.name for prog in programs if prog.com_id == comp.id] for comp in computers}
    for comp, prog in task1_list.items():
        print(f'{comp}: {prog}')

    print('\n\ntask2') 
    task2_list = dict(sorted(task1_list.items(), key=lambda x: len(x[1])))
    for comp, prog in task2_list.items():
        print(f'{comp}: {prog}')


    print('\n\ntask3')
    task3_list={}
    for prog in programs:
        if __name__ == '__main__':
            if prog.name[-1].isdigit:
                index_list = [comp.id_comp for comp in computer_program if comp.id_prog == prog.id]
        task3_list[prog.name] = [comp.name for comp in computers if comp.id in index_list]
    for prog, comp in task3_list.items():
        print(f'{prog}: {comp}')


if __name__ == '__main__':
    main()