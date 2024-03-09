$(document).ready(function () {
  const item = $('<li></li>').text('Item');
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').on('click', function)
});
