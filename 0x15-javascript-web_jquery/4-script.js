function toggleClass () {
  if ($('header').hasClass('red') && $('header').hasClass('green')) {
    $('header').removeClass('green');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').addClass('green');
  }
}

$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    toggleClass();
  });
});
