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

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function listargrupo() {
    grupo=$("#sometext[value='2']").text();
    parametros = {}
    $.ajax({
        type: "POST",
        url: '../pagar_sala_EI/',
        data: parametros,

        success: function (data) {

            if (data.rpta == 'No hay saldo suficiente en tu cuenta') { document.getElementById(id).setAttribute('value', "Saldo insuficiente") }
            else {
                Ajaxobtenersalas()


            }

        }
    });


}
