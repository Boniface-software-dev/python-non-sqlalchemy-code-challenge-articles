class Article:
    _all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <=50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self.title = title
        Article._all.append(self)

    @classmethod
    def all(cls):
        """Returns a list of all articles."""
        return cls._all
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.name = name

    @property
    def name(self):
        return self._name
  
    def articles(self):
        return [a for a in Article.all() if a.author == self]

    def magazines(self):
        return list(a.magazine for a in self.articles())

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({m.category for m in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= leng(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.stri()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [a for a in Article.all() if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        return [a for a in set (authors) if authors.count(a) > 2] or None

    @classmethod
    def top_publisher(cls):
        magazines = {a.magazines: 0 for a in Article.all()}
        for artile in Article.all():
            magazines[article.magazine] += 1
        return max(magines.items(), key=lambda x: x[1])[0] if magazines else None
