(document).ready(function () {
  $('#add_item').on('click', function () {
    $('<li>Item</li>').appendTo('.my_list');
  });
});
