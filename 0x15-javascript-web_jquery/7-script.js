function getData () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function () {
        
    }
  })
}

$(document).ready(function () {
  getData();
});
