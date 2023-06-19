from Core.Infrastructure.Notebook import Notebook


class Model:
	current_book: Notebook
	current_book_idx: int

	current_book = Notebook()

	def load_from_bin(self):
		pass

	def get_current_book(self) -> Notebook:
		return self.current_book