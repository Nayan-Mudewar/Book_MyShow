from models.booking import Booking

class BookingService:
    def __init__(self):
        self.bookings = {}  

    def create_booking(self, user, show, seat_ids):
        booking = Booking(user, show, seat_ids)
        if booking.status == "BOOKED":
            self.bookings[booking.booking_id] = booking
        return booking

    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings[booking_id]
            booking.cancel_booking()
            return booking
        return None

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)
