/* Task 3 - script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
use the jQuery API to call div with id red_header
*/
$('#red_header').click(function () {
  $('header').addClass('red');
});
