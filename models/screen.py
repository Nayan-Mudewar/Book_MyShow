class Screen:
    def __init__(self,screen_id,screen_name):
        self.screen_id = screen_id
        self.screen_name = screen_name
        self.seats=[]

    def add_seat(self,seat):
        self.seats.append(seat)