$(document).ready(function () {
  function setColor() {
    $('header').css('color', 'red');
  }
});
  
$('header').on('click', function() {
    setColor();
  });
  