/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */
 //5 preguntas por jueg
 cantidadPreguntas=0
 // tiempo-->Llega a 0 y cambia de pregunta
 tiempo=10
 segundo=1000
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
function botonactivado(){
  console.log('activando');
  document.getElementById("d0").style.pointerEvents = 'auto';
  document.getElementById("d1").style.pointerEvents = 'auto';
  document.getElementById("d2").style.pointerEvents = 'auto';
  document.getElementById("d3").style.pointerEvents = 'auto';
}
function botondesactivado(){
  console.log('desactivando')
  document.getElementById("d0").style.pointerEvents = 'none';
  document.getElementById("d1").style.pointerEvents = 'none';
  document.getElementById("d2").style.pointerEvents = 'none';
  document.getElementById("d3").style.pointerEvents = 'none';
}
$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

function obtenerpregunta(){
    $.get("../mostrarpregunta/",
    function(data){
    console.log()
    document.getElementById("pregunta").innerHTML = data.pregunta;
        document.getElementById("d0").innerHTML=data.d0
        document.getElementById("d1").innerHTML=data.d1
        document.getElementById("d2").innerHTML=data.d2
        document.getElementById("d3").innerHTML=data.d3
cantidadPreguntas=cantidadPreguntas+1;tiempo=10;
});document.getElementById("rpta").innerHTML='';
botonactivado()

};

function tiemporestante(segundo){

  document.getElementById("tiemporestante").innerHTML=segundo

}


function reply_click(id){

pregunta=$('#pregunta').html();
id='#'+id
grupo=$( "#grupotrivia option:selected" ).text();
respuesta=$(id).html();
parametros={'pregunta':pregunta,'respuesta':respuesta,'grupo':grupo}

    $.ajax({
              type: "POST",
              url: '../score/',
              data: parametros,

              success: function(data)
              {

            document.getElementById("rpta").innerHTML=data.resultado;
            tiempo=1;

              }
          });botondesactivado();
       }

x=setInterval(function() {
console.log(tiempo)

tiemporestante(tiempo)
tiempo=tiempo-1;
if (tiempo==-1){
      if (cantidadPreguntas==5){clearInterval(x);
        botondesactivado();
        document.getElementById("tiemporestante").innerHTML="Juego terminado"
        }else{
          tiempo=10 ;obtenerpregunta(); }
        }else {}

}, segundo);
