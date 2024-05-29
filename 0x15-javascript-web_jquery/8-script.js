/* Task 8 -script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
*/
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (query) {
  query.results.forEach(function (movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
