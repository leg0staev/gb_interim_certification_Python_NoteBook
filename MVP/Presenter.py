import datetime

from MVP.ConsoleView import ConsoleView
from MVP.Model import Model
from Core.Models.Note import Note


class Presenter:

	def __init__(self, model: Model, view: ConsoleView):
		self.model = model
		self.view = view

	def show_menu(self) -> str:
		self.view.console_clear()
		choise = self.view.show_menu()
		return str(choise)

	def display_clear(self) -> None:
		self.view.console_clear()

	def display_wrong_choise(self) -> None:
		self.view.console_clear()
		self.view.display('Такого пункта меню нет..')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def display(self, data: str) -> None:
		self.view.console_clear()
		self.view.display(data)

	def add_note(self) -> None:
		self.view.console_clear()
		self.model.get_current_book() \
			.add_note(Note(id=1,
							title=self.view.get_value('Введите название заметки: '),
							body=self.view.get_value('Введите тело заметки: '),
							date_created=datetime.datetime.now(),
							date_modified=datetime.datetime.now()))
		self.view.display('Заметка добавлена!')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def save_notes_to_file(self) -> None:
		self.view.console_clear()
		self.model.get_current_book() \
			.save_notes_db_to_file()
		self.view.display('Файл заметок сохранен!')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def load_notes_from_file(self) -> None:
		self.view.console_clear()
		self.view.display(self.model.get_current_book()
									.load_notes_db_from_file())
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def find_note_by_id(self) -> None:
		self.view.console_clear()
		try:
			id_from_user: int = int(self.view.get_value('введите ID заметки для поиска: '))
			self.view.display(self.model.get_current_book()
										.get_note_by_id(id_from_user))
			self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
		except:
			self.view.display('Заметки с таким ID нет..')
			self.view.user_waiting('Нажмите Enter чтобы продолжить..')

	def show_all_notes(self) -> None:
		self.view.console_clear()
		notes_list: list[Note] = self.model.get_current_book().get_notes_list()
		for note in notes_list:
			self.view.display(str(note))
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
