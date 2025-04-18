class Seat:
    def __init__(self, seat_id, seat_number, seat_type):
        self.seat_id = seat_id
        self.seat_number = seat_number
        self.seat_type = seat_type  
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def cancel(self):
        self.is_booked = False
