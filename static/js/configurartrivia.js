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

function datosPOSTJuego(usuario,grupo,sala){
  csrftoken = getCookie('csrftoken');
t0=" <form method='POST' action='../iniciarjuego/'>";
t0=t0+"<input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>";
t1="<input value='"+usuario+ "' id='jugarusuario' name='jugarusuario' hidden></input>";
t2="<input  value='"+grupo+ "' id='jugargrupo' name='jugargrupo' hidden></input>";
t3="<input  value='"+sala+ "' id='jugarsala' name='jugarsala' hidden></input>";
t4="<input class='btn btn-primary'  type='submit' value='Jugar'></form>";


return t0+t1+t2+t3+t4
}


var table = document.getElementById("missalas");
function agregarrow(grupo,sala,posic,contador){

  var row = table.insertRow(posic);


cell1=row.insertCell(0).innerHTML=grupo;
cell1=row.insertCell(1).innerHTML=sala;
cell1=row.insertCell(2).innerHTML='testEstado';
cell1=row.insertCell(3).innerHTML=datosPOSTJuego(user(),grupo,sala);
}
function llenartabla(datos){
  contador=0
  for (i in datos)
  {contador=contador+1
    for (h in datos[i]){
            grupo=h
            sala=datos[i][h]
agregarrow(sala,grupo,i,contador)
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
