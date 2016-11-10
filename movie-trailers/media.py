import webbrowser


class Movie:
    """To represent movie related inforation"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # A utility method for watching the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # A utility method for displaying Movie details
    def printMovieDetails(self):
        print("\nTitle: " + self.title)
        print("Storyline: " + self.storyline)
        print("Poster Image URL: " + self.poster_image_url)
        print("Youtube URL: " + self.trailer_youtube_url)
