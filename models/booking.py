import uuid
from datetime import datetime

class Booking:
    def __init__(self, user, show, seat_ids):
        self.booking_id = str(uuid.uuid4())  
        self.user = user                   
        self.show = show                    
        self.seat_ids = seat_ids            
        self.booking_time = datetime.now()
        self.status = "BOOKED"              

        
        self.successfully_booked = []
        for seat_id in seat_ids:
            if self.show.book_seat(seat_id):
                self.successfully_booked.append(seat_id)

        if len(self.successfully_booked) != len(seat_ids):
            self.status = "FAILED"
            for s_id in self.successfully_booked:
                self.show.cancel_seat(s_id)

    def cancel_booking(self):
        if self.status == "BOOKED":
            for seat_id in self.seat_ids:
                self.show.cancel_seat(seat_id)
            self.status = "CANCELLED"
