function langTranslate () {
  const langCode = $('INPUT#language_code').val();
  $.ajax({
    url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    langTranslate();
  });
  $('INPUT#btn_translate').on('keydown', function () {
    langTranslate();
  });
});
