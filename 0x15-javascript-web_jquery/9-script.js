/* Task 9 -script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello
*/
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (query) {
  $('#hello').text(query.hello);
});
