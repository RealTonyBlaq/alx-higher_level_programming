function addList () {
  const item = $('<li></li>').text('Item');
  $('UL.my_list').append(item);
}

$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    addList
  })
})
