from models.user import User
from models.movie import Movie
from models.theatre import Theatre
from models.screen import Screen
from models.seat import Seat
from models.show import Show
from services.bookingservice import BookingService
from services.searchservice import SearchService
from datetime import datetime

# Users
user1 = User("u1", "Nayan","nayanmudewar2002@gmail.com")

# Movies
movie1 = Movie("m1", "Jawan", 160, "Hindi")
movie2 = Movie("m2", "Leo", 155, "Tamil")
movies = [movie1, movie2]

# Theatre
theatre1 = Theatre("t1", "INOX", "Nagpur")

# Screen
screen1 = Screen("s1", "Screen 1")

# Seats
for i in range(1, 6):  # 5 seats
    seat = Seat(f"S{i}", "Silver", 150)
    screen1.add_seat(seat)

# Shows
show1 = Show("sh1", movie1, screen1,
             datetime(2024, 4, 20, 14, 0),
             datetime(2024, 4, 20, 16, 40))
screen1.add_show(show1)

show2 = Show("sh2", movie2, screen1,
             datetime(2024, 4, 20, 18, 0),
             datetime(2024, 4, 20, 20, 35))
screen1.add_show(show2)

# Added Screen
theatre1.add_screen(screen1)

# Services
booking_service = BookingService()
search_service = SearchService([theatre1], movies)

# Search
print("Movies in Nagpur:")
for movie in search_service.get_movies_by_city("Nagpur"):
    print(movie.name)

print("\nShows for 'Jawan' in Nagpur:")
for show in search_service.get_shows_by_movie_and_city("Jawan", "Nagpur"):
    print(f"{show.show_id} - {show.movie.name} - {show.start_time}")

#Booking
print("\nBooking 2 seats for show1...")
booking = booking_service.create_booking(user1, show1, ["S1", "S2"])
print(f"Booking Status: {booking.status}")
print(f"Booked Seats: {booking.seat_ids if booking.status == 'BOOKED' else []}")

# Cancel Booking
print("\nCancelling booking...")
booking_service.cancel_booking(booking.booking_id)
print(f"Updated Status: {booking.status}")
