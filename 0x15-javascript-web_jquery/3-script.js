function addRedClass () {
  if (! $('header').hasClass('red')) {
    $('header').addClass('red');
  }
}

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    addRedClass()
  })
})
