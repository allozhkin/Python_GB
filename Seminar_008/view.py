import model


def input_class():
    return input('Какой класс нужен?: ').upper()


def input_subject():
    return input('Какой предмет?: ').lower()


def who_answer():
    return input('Кого к доске?: ')


def what_mark():
    return input('Какую ставить оценку?: ')


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')
