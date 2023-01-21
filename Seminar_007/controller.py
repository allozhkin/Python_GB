import model
import view



def inp_handler(inp: int):
    match inp:
        case 1:
            model.read_bd('database.txt')
            view.db_success(model.db_list)
        case 2:
            view.show_all(model.db_list)
        case 4:
            model.db_list.append(view.create_contact())
        case 7:
            view.exit_program()
def start():
    while True:               
        user_inp = view.main_menu()
        inp_handler(user_inp)