class AbstractView:
	def get_note_title(self) -> str:
		pass

	def get_note_body(self) -> str:
		pass

	def show_menu(self):
		pass

	def get_value(self, title: str):
		pass

	def display(self, data: str):
		pass