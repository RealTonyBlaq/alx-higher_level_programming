$(document).ready(function () {
  const langCode = $('INPUT#language_code').attr();
  $.ajax({
    url: `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`,
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      
    }
  })

});
