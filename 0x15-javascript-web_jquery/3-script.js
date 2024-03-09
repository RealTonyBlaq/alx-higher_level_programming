function addRedClass () {
  if (! $('header').hasClass('red')) {
    $('header').addClass('red');
  } else {
    $('header').css('color', 'blue');
  }
}

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    addRedClass();
  });
});
