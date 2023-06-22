from Core.Infrastructure.Notebook import Notebook


class Model:
	current_book: Notebook

	current_book = Notebook()

	def get_current_book(self) -> Notebook:
		return self.current_book
