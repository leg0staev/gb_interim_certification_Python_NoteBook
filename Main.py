from MVP.Presenter import Presenter
from MVP.Model import Model
from MVP.ConsoleView import ConsoleView

if __name__ == '__main__':
    presenter: Presenter = Presenter(Model(), ConsoleView())

    RUN = True
    while RUN:
        user_choice = presenter.show_menu()
        match user_choice:
            case '1':
                presenter.add_note()
            case '0':
                RUN = False
                presenter.display('Программа завершила работу. До свидания!')
            case _:
                presenter.display_wrong_choise('Такого пункта меню нет')