function setColor () {
  $('header').css('color', 'red');
}

$(document).ready(function () {
  $('header').on('click', function () {
    setColor();
  });
});
