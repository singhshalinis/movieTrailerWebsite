from xml.dom.minidom import parse
import xml.dom.minidom
import media


def readMoviesXML(filename):
    '''
    This method takes an XML file as input, parses it and returns a list of
    movie class objects. It uses DOM parser for XML processing. Other parsers
    available in the Python library can also be used instead.
    Assumptions
    1: "filename" is a valid XML file (error conditions not handled)
    '''

    # List of movie objects
    movieClassList = []

    # Create a DOM tree
    tree = xml.dom.minidom.parse(filename)

    # Get the document from the tree
    document = tree.documentElement

    # Get all the movies from the XML file
    movies = document.getElementsByTagName("movie")

    # For each movie in the XML file,
    #   1. get all tags for the given movie
    #   2. create a movie class object
    #   3. add the movie to the movie list
    # [0] is used as we take only first child here
    for movie in movies:
        title = movie.getElementsByTagName('movie_title')[0]
        movie_storyline = movie.getElementsByTagName('movie_storyline')[0]
        poster_image = movie.getElementsByTagName('poster_image')[0]
        trailer_youtube = movie.getElementsByTagName('trailer_youtube')[0]

        movieClassList.append(media.Movie(title.childNodes[0].data,
                                          movie_storyline.childNodes[0].data,
                                          poster_image.childNodes[0].data,
                                          trailer_youtube.childNodes[0].data))

    # return the list of Movie objects extracted from the XML
    return movieClassList


# For testing purpose only
# a = readMoviesXML("movies.xml")
# for m in a:
#    m.printMovieDetails()
