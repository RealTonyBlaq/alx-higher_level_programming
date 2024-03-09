function setColor () {
  $('header').css('color', 'red');
}

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    setColor();
  });
});
