/* Task 7 -script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=jsonThe name must be displayed in the HTML tag DIV#character
*/
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (query) {
  $('#character').text(query.name);
});
