function listTitles () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      for (const result of data.results) {
        const title = da
      }
    }
  });
}
