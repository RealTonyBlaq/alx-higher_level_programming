function toggleClass () {
  if ($('header').hasClass('red') && $('header').hasClass('green')) {
    $('header').removeClass('green');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('');
  } else if ($('header').hasClass('blue')) {
    $('header').removeClass('blue');
    $('header').addClass('red');
  } else {
    $('header').addClass('blue');
  }
}

$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    toggleClass();
  });
});
