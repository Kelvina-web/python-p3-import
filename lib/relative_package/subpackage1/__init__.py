class Book:
    genres = []

    def __init__(self, title, author="", page_count=0):
        self.title = title
        self.author = author
        self.page_count = page_count

    @classmethod
    def genre(cls, genre):
        cls.genres.append(genre)