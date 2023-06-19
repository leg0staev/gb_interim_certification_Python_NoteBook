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

	def display_wrong_choise(self, data: str) -> None:
		self.view.console_clear()
		self.view.display(data)
		self.view.user_waiting()

	def display(self, data: str) -> None:
		self.view.console_clear()
		self.view.display(data)

	def add_note(self) -> None:
		self.view.console_clear()
		self.model.get_current_book()\
			.add_note(Note(self.view.get_note_title(),
							self.view.get_note_body()))
		self.view.display('Заметка добавлена!')
		self.view.user_waiting()

