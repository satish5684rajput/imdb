Steps:

Installation:
1. Intall python virtual environment using "$ pip install virtualenv" command
(https://virtualenv.pypa.io/en/stable/userguide/)
2. Create viratul environment using "$ virtualenv ENV"
3. Activat viratul environment using "$ source bin/activate" command
4. Intall dependencies by "$ pip install -r requirements.txt" command
5. Migrate appication server using "$ python manage.py migrate" command
6. Run appication server using "$ python manage.py runserver" command

Now you are able to search and get the movie_list

For Admin Portal:
1. Click on Admin button(on top of the right) for accessing admin panel:

2. Enter input credential:
   Username: admin
   password: admin@123
3. Now admin can add, delete, edit movies, genre, user and group

API Information
1. Get all movie api:
   URL: http://127.0.0.1:8000/movies/
   method: GET

2. Add New movie(Only for admin):
	URL: http://127.0.0.1:8000/movies/
   	method: POST
   	parameters: [ username:admin,
                  password: admin@123,
                  movie_name: movie name(character field),
                  director_name: director name(character field),
                  imdb_score: imdb score(decimal field),
                  popularity_score: popularity score(decimal field)
   				]
3. Get movie detail by id:
	URL: http://127.0.0.1:8000/movies/{{id}}
   	method: GET

4. Edit movie detail by id(Only for admin):
	URL: http://127.0.0.1:8000/movies/{{id}}
   	method: PUT
   	parameters: [ username:admin,
                  password: admin@123,
                  movie_name: movie name(character field),
                  director_name: director name(character field),
                  imdb_score: imdb score(decimal field),
                  popularity_score: popularity score(decimal field)
   				]

5. Delete movie by id(Only for admin):
	URL: http://127.0.0.1:8000/movies/{{id}}
   	method: DELETE
   	parameters: [ username:admin,
                  password: admin@123,
   				]

6. Search movie:
	URL: http://127.0.0.1:8000/movies-search/{{search_teram}}
   	method: GET


Thank You



