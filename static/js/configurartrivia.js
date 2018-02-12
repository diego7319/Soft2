function getCookie(name)
{
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
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});
var table = document.getElementById("missalas");
function agregarrow(sala,grupo,posic){
  var row = table.insertRow(posic);

cell1=row.insertCell(0).innerHTML=sala;
cell1=row.insertCell(1).innerHTML=grupo;

}

function llenartabla(datos){
  for (i in datos)
  {
    for (h in datos[i]){
            sala=h
            grupo=datos[i][h]
agregarrow(grupo,sala,i)


                }
  }
}

function Ajaxobtenersalas(){
  parametros={'usuario':user()};
  $.ajax({

            type: "POST",
            url: '../obtenerSalas/',
            data: parametros,

            success: function(data)
            {

          llenartabla(data)

            }
        });


}


function pagar(){}
