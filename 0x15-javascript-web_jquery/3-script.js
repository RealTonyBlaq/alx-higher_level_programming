function addRedClass () {
  if (! $('header').hasClass('red')) {
    $('header').addClass('red');
  } else {
    $('header').addClass
  }
}

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    addRedClass();
  });
});
