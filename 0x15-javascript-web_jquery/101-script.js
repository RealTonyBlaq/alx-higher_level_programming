$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    const item = $('<li></li>').text('Item');
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list').remove('li:last');
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
