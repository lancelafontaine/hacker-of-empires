var serverUrl = 'http://localhost:5000/';

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
  alert(JSON.stringify(data.text));
}

function init() {
  $('#form').submit(submitHandler);
}

window.onload = init;
