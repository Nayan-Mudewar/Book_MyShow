class SearchService:
    def __init__(self, theatres, movies):
        self.theatres = theatres  
        self.movies = movies      

    def get_movies_by_city(self, city):
        movie_set = set()
        for theatre in self.theatres:
            if theatre.city.lower() == city.lower():
                for screen in theatre.screens:
                    for show in getattr(screen, 'shows', []):
                        movie_set.add(show.movie)
        return list(movie_set)

    def get_shows_by_movie_and_city(self, movie_name, city):
        shows = []
        for theatre in self.theatres:
            if theatre.city.lower() == city.lower():
                for screen in theatre.screens:
                    for show in getattr(screen, 'shows', []):
                        if show.movie.name.lower() == movie_name.lower():
                            shows.append(show)
        return shows
