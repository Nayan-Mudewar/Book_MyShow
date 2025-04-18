class Theatre:
    def __init__(self,theatre_id,name,city):
        self.theatre_id = theatre_id
        self.name=name
        self.city=city
        self.screens=[]

    def add_screen(self,screen):
        self.screens.append(screen)