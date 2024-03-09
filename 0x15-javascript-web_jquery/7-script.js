function getData () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, textStatus) {
    alert('Response' + data + ' with status: ' + textStatus);
  })
}

$(document).ready(function () {
  getData();
});
