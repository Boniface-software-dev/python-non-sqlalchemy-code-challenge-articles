class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        if not isinstance(title, str) or not (5 <= len(title) <=50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")  
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise ValueError("Name is immutable.")
       
    
    # Add relationships (articles written by this author)  
    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        unique = {}
        for article in self.articles():
            unique[article.magazine] = article.magazine
        return list(unique.values())

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({a.magazine.category for a in self.articles()}) or None
    
class Magazine:
    def __init__(self, name, category):       
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):       
        return [a.title for a in self.articles()] or None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2] or None 

    @classmethod
    def top_publisher(cls):
        magazine_count = {}
        for article in Article.all:
            mag = article.magazine
            magazine_count[mag] = magazine_count.get(mag, 0) + 1
        return max(magazine_count, key=magazine_count.get, default=None)
