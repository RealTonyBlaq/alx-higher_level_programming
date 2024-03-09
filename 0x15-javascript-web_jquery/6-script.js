function updateHeader () {
  $('header').text('New Header!!!');
}

$(document).ready(function () {
  $('DIV#update_header').on('click', updateHeader());
})
