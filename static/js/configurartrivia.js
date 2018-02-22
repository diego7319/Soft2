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




function botondeuda(estado,usuario,grupo,sala){
  if(estado=='deuda'){
    id2=usuario+grupo+sala
    id=estado+usuario+grupo+sala
    func="restPago('"+usuario+"','"+grupo+"','"+sala+"');"
t0='<input class="btn btn-primary" id='+id2+' type="submit" value="Pagar Aqui" onclick="'+func+'">';
  return t0}
  else {return 'Habilitado para Jugar'}


}

function botondeudaadmin(estado,usuario,grupo,sala){
  if(estado=='deuda'){
    id2=usuario+grupo+sala
    id=estado+usuario+grupo+sala
    func="restPagoadmin('"+sala+"');"
t0='<input class="btn btn-primary" id='+id2+' type="submit" value="Pagar Aqui" onclick="'+func+'">';
  return t0}



}


function restPago(usuario, grupo, sala) {
    id = usuario + grupo + sala
    parametros = { 'jugarusuario': usuario, 'jugarsala': sala, 'jugargrupo': grupo }
    $.ajax({
        type: "POST",
        url: '../pagar_sala/',
        data: parametros,

        success: function (data) {

            if (data.rpta == 'No hay saldo suficiente en tu cuenta')
            {document.getElementById(id).setAttribute('value',"Saldo insuficiente")}
        else{window.location.href = window.location.href;  }

        }
    });


          }




function datosPOSTJuego(usuario, grupo, sala, habilitado) {
    if (habilitado == 'si') {
        csrftoken = getCookie('csrftoken');
        t0 = " <form method='POST' action='../iniciarjuego/'>";
        t0 = t0 + "<input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>";
        t1 = "<input value='" + usuario + "' id='jugarusuario' name='jugarusuario' hidden></input>";
        t2 = "<input  value='" + grupo + "' id='jugargrupo' name='jugargrupo' hidden></input>";
        t3 = "<input  value='" + sala + "' id='jugarsala' name='jugarsala' hidden></input>";
        t4 = "<input class='btn btn-primary'  type='submit' value='Jugar'></form>";
        return t0 + t1 + t2 + t3 + t4
    }
    else {

        return "<input class='btn btn-primary'  type='submit' value='Jugar' disabled='disabled'>"
    }
}

function datosPOSTJuegoadmin(sala) {

        csrftoken = getCookie('csrftoken');
        t0 = " <form method='POST' action='../obtenerganador/'>";
        t0 = t0 + "<input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>";
        t3 = "<input  value='" + sala + "' id='jugarsala' name='jugarsala' hidden></input>";
        t4 = "<input class='btn btn-primary'  type='submit' value='Obtener Ganador'></form>";
        return t0 + t3 + t4
    }




function agregarrow(grupo, sala, posic, contador, estado) {
  var table = document.getElementById("missalas");
    var row = table.insertRow(posic);
    cell1 = row.insertCell(0).innerHTML = grupo;
    cell1 = row.insertCell(1).innerHTML = sala;
    x = botondeuda(estado, user(), grupo, sala);
    if (x == 'Habilitado para Jugar') {
        cell1 = row.insertCell(2).innerHTML = x;
        habilitado = 'si'
        cell1 = row.insertCell(3).innerHTML = datosPOSTJuego(user(), grupo, sala, habilitado);
    }
    else {
        habilitado = 'no'
        cell1 = row.insertCell(2).innerHTML = x;
        cell1 = row.insertCell(3).innerHTML = datosPOSTJuego(user(), grupo, sala, habilitado);
    }

}


function agregarrowadmin(grupo, sala, posic, contador) {
  var tableadmin = document.getElementById("missalasadmin");
    var row = tableadmin.insertRow(posic);
    cell1 = row.insertCell(0).innerHTML = grupo;
    cell1 = row.insertCell(1).innerHTML = sala;
    cell1 = row.insertCell(2).innerHTML = datosPOSTJuegoadmin(sala);
    }



function llenartabla(datos) {
    contador = 0
    for (i in datos) {
        contador = contador + 1;
        sala = datos[i].sala;
        grupo = datos[i].grupo;
        estado = datos[i].estado;
        agregarrow(grupo, sala, i, contador, estado);
    }

}

function llenartablaadmin(datos){
  contador=0
  for (i in datos)
  {contador=contador+1
    sala=datos[i].sala
    grupo=datos[i].grupo

agregarrowadmin(grupo,sala,i,contador)
                }

}

function Ajaxobtenersalas(){
  parametros={'usuario':user()};
  $.ajax({
            type: "POST",
            url: '../obtenerSalas/',
            data: parametros,
        success: function (data) {
  console.log('salas')
  console.log(data)
            llenartabla(data)

        }
    });

}

function Ajaxobtenersalasadmin(){
  parametros={'usuario':user()};
  $.ajax({
            type: "POST",
            url: '../obtenerSalasadmin/',
            data: parametros,
            success: function(data)
            {
              console.log('admin')
                console.log(data)
  llenartablaadmin(data)

          }
        });

}
