class Books:
    
    def __init__(self, author = "", title = "", year = ""):
        self.author = author
        self.title = title
        self.year = year
        
    def __str__(self):
        return f"{self.author}: {self.title} ({self.year})"