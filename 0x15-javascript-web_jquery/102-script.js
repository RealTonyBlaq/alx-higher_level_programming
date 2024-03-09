$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`,
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
