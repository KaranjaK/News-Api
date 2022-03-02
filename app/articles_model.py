class Articles:

    def __init__(self, id, name, title, urlToImage, author, publishedAt, description):
        self.id = id
        self.name = name
        self.title = title
        self.urlToImage = urlToImage
        self.author = author
        self.publishedAt = publishedAt
        self.description = description

class Display:

    articles_display = []

    def __ini__(self, id, name, title, urlToImage, author, publishedAt, description):
        self.id = id
        self.name = name
        self.title = title
        self.urlToImage = urlToImage
        self.author = author
        self.publishedAt = publishedAt
        self.description = description

    def save_display(self):
        Display.articles_display.append(self)