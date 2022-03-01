class Sources:

    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.langauge = language
        self.country = country


class Display:

    source_display = []

    def __ini__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.langauge = language
        self.country = country

    def save_display(self):
        Display.source_display.append(self)

    