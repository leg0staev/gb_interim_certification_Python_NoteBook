import os
import platform
from MVP.AbstractView import AbstractView


class ConsoleView(AbstractView):

	def get_note_title(self) -> str:
		return str(input('Введите название заметки: '))

	def get_note_body(self) -> str:
		return str(input('Введите тело заметки: '))

	def get_value(self, title: str) -> str:
		return str(input(title))

	def display(self, data: str) -> None:
		print(data)

	def show_menu(self) -> str:
		print('''
Введите номер действия:
1 - Добавить заметку
2 - ...
3 - ...
4 - ...
5 - ...
6 - ...
0 - Выход''')
		print()
		return str(input('ваш выбор > '))

	def console_clear(self) -> None:
		"""очистка консоли"""

		if os.name == 'posix':  # для Unix-подобных систем (Linux, macOS)
			os.system('clear')
		else:
			os.system('cls')

	def user_waiting(self):
		input('нажмите Enter чтобы вернуться в меню')
