var serverUrl = 'http://13.59.13.218/empires';

function submitHandler(e) {
  e.preventDefault();

  var requestData = {
    major: $('#major').val(),
    colour: $('#colour').val(),
    language: $('#language').val(),
    email: $('#email').val()
  }

  $.ajax({
      type: 'POST',
      url: serverUrl,
      data: JSON.stringify(requestData),
      success: responseHandler,
      contentType: "application/json",
      dataType: 'json'
  });
}

function responseHandler(data) {
  data = data.text;

  var htmlTitle = '<h1>' +
    data.first_name + ', ' +
    data.title + ', ' +
    data.class_name + '</h1>';

  var htmlBody = '<h3>' +
    data.misc_skill.number + ' ' +
    data.misc_skill.skill + '</h3>';

  htmlBody += '<h3>' +
    data.language_skill.number + ' ' +
    data.language_skill.skill + '</h3>';

  htmlBody += '<h3>' +
    data.colour_skill.number + ' ' +
    data.colour_skill.skill + '</h3>';

  var html = htmlTitle + htmlBody;

  swal({
    titleText: 'You are...',
    html: html,
    confirmButtonText: 'Frosh on!',
    width: '70%',
    imageUrl: '/img/warrior.png',
    imageWidth: '200px',
    imageHeight: '200px',
    onClose: function() { window.location.reload(); }
  });
}

function init() {
  $('#form').submit(submitHandler);
}

window.onload = init;
