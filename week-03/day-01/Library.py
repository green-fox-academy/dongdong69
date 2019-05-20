class Books:
    
    __init__(self, author = "", title = "", year = ""):
        self.author = author
        self.title = title
        self.year = year
        
    __str__(self):
        return f"{self.author}: {self.title} ({year})"