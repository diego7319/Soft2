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


function alerta(data,tipo,id){
  var div = document.createElement("div");
var parser = new DOMParser();

  d=""
if (tipo=='1'){
d="<div id='unic' class='alert alert-success alert-dismissible'><a href='#' class='close' data-dismiss='alert' " +"aria-label='close'>&times;</a>"
d=d+ data+"</div>"}
else {
d="<div id ='unic' class='alert alert-danger alert-dismissible'><a href='#' class='close' data-dismiss='alert' " +"aria-label='close'>&times;</a>"
d=d+ data+"</div>"}
div.innerHTML = d;
console.log(d)
x=parser.parseFromString(d, "text/html");
f=x.getElementById('unic')
document.getElementById(id).appendChild(f)
}


function msjAgregarGrupo(mensaje){}

function creargrupo() {
    nombregrupo = document.getElementById('nombregrupo').value
    parametros = {'nombregrupo':nombregrupo}
    $.ajax({
        type: "POST",
        url: '../agregargrupo/',
        data: parametros,

        success: function (data) {
    console.log(data.rpta)

alerta(data.rpta,data.tipo,'agregargrupo')

            }


    });
return false

}
function invitar() {
    nombre = document.getElementById('invitado').value

    parametros = {'grupo':$('#grupo').val(),'invitado':nombre}
    $.ajax({
        type: "POST",
        url: '../invitarusuario/',
        data: parametros,

        success: function (data) {
    console.log(data.rpta)

alerta(data.rpta,data.tipo,'invita')

            }


    });
return false

}
