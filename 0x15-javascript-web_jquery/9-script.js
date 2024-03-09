function fetch () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const text = data.hello;
      $('DIV#hello').text(text);
    }
  });
}

$(document).ready(function () {
    fetch
})
