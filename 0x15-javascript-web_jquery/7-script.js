function getData () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const text = data.name;
      $('DIV#character').text(text);
    }
  });
}

$(document).ready(function () {
  getData();
});
