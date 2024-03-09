$(document).ready(function () {
  let item = $('<li></li>').text('Item');
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list').remove('li':last)
  })
});
