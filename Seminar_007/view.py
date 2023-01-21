def main_menu() -> int:
    print("-"*5 + "Главное меню" + "-"*5)
    menu_list = ['Открыть файл',
                 'Показать Контакты',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Сохранить файл',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'    {i+1}. {menu_list[i]}')
    user_input = int(input('Введтите команду: '))
    return user_input


def show_all(db):
    if db_success(db):
        for i in range(len(db)):
            user_id = i+1
            print(user_id, end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def db_success(db):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
         print('Телефонная книга пуста')
         return False
def exit_program():
    print("Пока!!")
    exit()
    
    
def create_contact():
    print('Создание нового контакта')
    new_contact = dict()
    new_contact['Lostname'] = input('   Введите фамилию: ')
    new_contact['name'] = input('   Введите имя: ')
    new_contact['phone'] = input('     Введите номер телефона: ')
    new_contact['comment'] = input('    Введите комментарий: ')
    return new_contact