$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.getJSON(apiUrl, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error: Language not found');
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
