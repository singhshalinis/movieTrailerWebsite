import media
import os
import webbrowser
import re
import readXML

# HTML Content
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <title>Rotten Potato</title>

    <!--CSS -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">

    <!--Javascript-->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <style type="text/css" media="screen">

        html {
            position: relative;
            min-height: 100%;
        }
        body {
            margin-bottom: 40px;
            padding-top: 80px;
            }

          #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
          }

          #trailer-video {
            width: 100%;
            height: 100%;
          }

          .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
          }

          .movie-tile {
            margin-bottom: 5px;
            padding-top: 8px;
          }

          .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
          }

        .storyline:hover {
            background-color: #EEE;
            cursor: pointer;
        }

          .scale-media {
            padding-bottom: 56.25%;
            position: relative;
          }

          .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
          }

        .brand {
            font-size:170%;
            font-weight:bold;
            color:rgb(254,247,245);
        }

        .common-font-color {
            color:rgb(254,247,245)
        }

        .movie-title {
            font-size:150%;
            font-weight:bold;
        }

        .nav-header-color {
            background-color:#0ACCCE;
        }

        .movie-title-color {
            background-color:#FF466E;
        }

        a:visited {
            color:rgb(254,247,245)
        }


        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            /* Set the fixed height of the footer here */
            height: 30px;
            background-color:#0ACCBF ;

        }

      </style>

      <script type="text/javascript" charset="utf-8">
      $(document).ready(function(){
          // Pause the video when the modal is closed
          $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
              // Remove the src so the player itself gets removed, as this is the only
              // reliable way to ensure the video stops playing in IE
              $("#trailer-video-container").empty();
          });

          // Start playing the video whenever the trailer modal is opened
          $(document).on('click', '.movie-tile', function (event) {
              var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
              var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
              $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                                                                'id': 'trailer-video',
                                                                'type': 'text-html',
                                                                'src': sourceUrl,
                                                                'frameborder': 0
              }));
          });

          //Fetch and add data to the storyline modal
          $('.storyline').on('click', function (event) {

              var ele = event.currentTarget;
              movieTitle = $(ele).siblings('.movie-title').html();
              story = $(ele).children('.storylinedata').html();

              $("#storyline-modal-title").html(movieTitle);
              $("#storyline-modal-text").html(story);
          });
        });
      </script>
  </head>
'''


# The main page layout, nav, modals
main_page_content = '''
<body>
    <!--Movie Trailer Modal definition -->
      <div class="modal" id="trailer">
          <div class="modal-dialog">
              <div class="modal-content">
                  <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                      <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                  </a>
                  <div class="scale-media" id="trailer-video-container"></div>
              </div>
          </div>
      </div>

      <!--storyline Modal definition -->
      <div id="storylineModal" class="modal fade" role="dialog">
        <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title" id="storyline-modal-title"></h4>
          </div>
          <div class="modal-body" >
            <p id="storyline-modal-text"></p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>

      </div>
    </div>

    <!--The Navigation Bar -->
    <div>
      <nav class="navbar navbar-light navbar-fixed-top nav-header-color">
          <div>
              <a class="navbar-brand brand" href="#">THEJh</a>
          </div>
          <div>
              <ul class="nav navbar-nav ">
                  <li class="nav-item common-font-color active">
                    <a class="nav-link" href="#">Movie Trailers </a>
                  </li>
                </ul>

                <ul class="nav navbar-nav pull-right ">
                    <li class="nav-item common-font-color">
                        <a class="nav-link" href="about.html">About Us</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    <div class="container" style="margin-top:0px">

        {movie_tiles}

    </div>
      <!--Static Footer -->
      <footer class="footer">
            <div class="container">
                <span class="text-muted" style="color:rgb(254,247,245)">
                Powered by THEJh &copy; 2016</span>
            </div>
        </footer>
    </body>
</html>
'''

# A single movie entry template
movie_content = '''
        <div class="col-sm-4" style="padding:25px;">
            <div class="card" style="border: 1px groove grey; border-radius:5px;">
                <div class="card-header text-center movie-title movie-title-color common-font-color">
                    {movie_title}
                </div>

                <img class="card-img-top movie-tile center-block" height="80%" width="80%" src="{poster_image_url}"
                     data-toggle="modal" data-target="#trailer" data-trailer-youtube-id="{trailer_youtube_id}">

                <div class="card-block storyline" data-toggle="modal" data-target="#storylineModal">
                    <h4 class="text-muted" align="center" style="font-size:80%;font-style:italic">
                    Read a brief storyline here.
                    </h4>

                    <div hidden class="storylinedata">
                        {movie_storyline}
                    </div>

                </div>
            </div>
        </div>
'''


# Function definition
def open_movies_page(movies):

    # Create or overwrite the output file
    output_file = open('movie_trailers.html', 'w')

    # Fill movie information in the HTML page
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output to the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


def create_movie_tiles_content(movies):

    # Create the The HTML content for this section of the page
    content = ''

    for movie in movies:

        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)

        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)

        trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_content.format(
                    movie_title=movie.title,
                    movie_storyline=movie.storyline,
                    poster_image_url=movie.poster_image_url,
                    trailer_youtube_id=trailer_youtube_id
                    )

    return content

# Call to open the browser


def main():
    aMovieList = readXML.readMoviesXML("movies.xml")
    open_movies_page(aMovieList)

main()
