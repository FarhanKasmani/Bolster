$(function() {
  console.log("YoYoHoneySIngh");
  $("button[class='btn btn-info']").on('click', function(event){
      console.log("Event click performed");
      event.preventDefault();
      var uid = this.id;
      console.log(uid);
      $.ajax({
          url : 'http://127.0.0.1:8000/patients/profile',
          type : 'POST',
          data : {
            msgbox : uid,
            //csrfmiddlewaretoken: '{{ csrf_token }}'
          },
          success : function() {
              console.log("success")
              $t = $('#code')
              console.log($t.text())
          },
          failure: function(){
            console.log("Failure")
          }
      });
      /**$.post("http://127.0.0.1:8000/patients/profile",
      {
        msgbox: uid,
    });**/
  });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
