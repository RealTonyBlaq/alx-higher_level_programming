function getData () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    method
  })
}

$(document).ready(function () {
  getData();
});
