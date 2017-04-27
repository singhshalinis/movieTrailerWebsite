The Movie Trailer Website
=========================


What is it? (Functionality)
---------------------------
The movie trailer website ("Rotten Potato") allows you to watch your favourite 
movies' trailer all at one place. Each movie also shows a brief storyline. 


Last Update Date
-----------------
September 26, 2016


System-specific Notes
----------------------
Backend developed on Python 3.5.2
The webpage was tested for Edge Browser. It seemed to work as expected in 
Mozilla and Chrome browsers too. It has not been tested for small screens.


Package Details (Files involved) 
-------------------------------
The folder "movie-trailers" has below files that are used to dynamically 
generate the movie trailer web page. 

  1. media.py - Contains class definition for movie object.
  
  2. movies_entertainment.py - This is the main python file that generates the 
	 webpage. It creates html file by concatenating different strings defined 
	 in it for each of - head, body and movie content. It dynamically reads the
	 input movies and creates the content for the webpage.
	 
  3. readXML.py - It takes movies in the form of an XML as an input and 
	 processes it and returns a list of movie class objects for the 
	 movies_entertainment.py file to use.
	 
  4. movies.xml - This is the input list of favourite movies in XML format.
  
  5. about.html - This serves the About Us section of the website. 
  
  6. movie_trailers.html - This is generated when movies_entertainment.py is
	 run. It is not present in downloaded package.

	
Compling and Running the Program
---------------------------------
  1. From the Python shell, locate and open file "movies_entertainment.py".
  
  2. Run it.
  
  3. The program creates an html file called "movie_trailers.html" which is
	 automatically opened in the default browser. 
  
  4. Browse through the movies in the webpage and take a look at the trailers, 
	 or read the storyline by simply clicking the links.
	 
Note: "movie_trailers.html" gets overwritten each time we run the program.


Adding more movies
-------------------
To add a new movie, simply find the movie image URL, movie trailer URL, and 
screenplay description and add a new entry to movies.xml file. Be careful to
take care of tags and keep the XML well formed.


Known Issues
-------------
1. The height for each row on the website is not fixed. If one of the image 
   that we use for box-art has height more than others in the row, there would
   be no image immediately below it. The current order of movies in movies.xml 
   file does not show this issue.
   
2. The html lines defined in movies_entertainment.py have length > 79 chars and so 
   it does not fulfill Pep8 requirements completely. 
   
   
References, Credits & Acknowledgements
---------------------------------------
	1. https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py
	   movies_entertainment.py is taken from this file with changes made mostly
	   to the look and feel only.
	   
	2. http://getbootstrap.com/	
	
	3. http://www.w3schools.com/	
	
	4. https://www.tutorialspoint.com/python/python_xml_processing.htm	
	
	5. Color Schemes - https://color.adobe.com/create/color-wheel
	
	6. README - http://svn.apache.org/repos/asf/httpd/httpd/trunk/README
    
    7. http://pep8online.com/
    
    8. http://stackoverflow.com/


Contact Information
--------------------
For any comments, queries, issues, and bugs, please contact singhshalinis@gmail.com.
