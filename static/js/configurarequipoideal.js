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



function botondeuda(estado, usuario, grupo, sala) {
    if (estado == 'deuda') {
        id2 = usuario + grupo + sala
        id = estado + usuario + grupo + sala
        func = "restPago('" + usuario + "','" + grupo + "','" + sala + "');"
        t0 = '<input class="btn btn-primary" id=' + id2 + ' type="submit" value="Pagar Aqui" onclick="' + func + '">';
        return t0
    }
    else { return 'Habilitado para Jugar' }
}

function botondeudaadmin(estado, usuario, grupo, sala) {
    if (estado == 'deuda') {
        id2 = usuario + grupo + sala
        id = estado + usuario + grupo + sala
        func = "restPagoadmin('" + sala + "');"
        t0 = '<input class="btn btn-primary" id=' + id2 + ' type="submit" value="Pagar Aqui" onclick="' + func + '">';
        return t0
    }
}


function restPago(usuario, grupo, sala) {
    id = usuario + grupo + sala
    parametros = { 'jugarusuario': usuario, 'jugarsala': sala, 'jugargrupo': grupo }
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

function datosPOSTJuego(usuario, grupo, sala, habilitado) {
    if (habilitado == 'si') {
        csrftoken = getCookie('csrftoken');
        t0 = " <form method='POST' action='../iniciarjuegoEI/'>";
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
    sala= '"'+sala+'"'
    t0 =  "<input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>";
    t4 = "<input class='btn btn-primary' onclick='Calcularganador("+sala+")' type='submit' value='Obtener Ganador'>";
    return  t4
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

function llenartablaadmin(datos) {
    contador = 0
    for (i in datos) {
        contador = contador + 1
        sala = datos[i].sala
        grupo = datos[i].grupo

        agregarrowadmin(grupo, sala, i, contador)
    }

}

function Ajaxobtenersalas() {
  $('#missalas').empty();
    parametros = { 'usuario': user() };
    $.ajax({
        type: "POST",
        url: '../obtenerSalasEI/',
        data: parametros,
        success: function (data) {
            console.log('salas')
            console.log(data)
            llenartabla(data)

        }
    });

}

function Ajaxobtenersalasadmin() {
  $('#missalasadmin').empty();
    parametros = { 'usuario': user() };
    $.ajax({
        type: "POST",
        url: '../obtenerSalasEIadmin/',
        data: parametros,
        success: function (data) {
            console.log('admin')
            console.log(data)
            llenartablaadmin(data)

        }
    });

}

function AjaxAgregarsala() {
    nombresala = document.getElementById('nombresala').value
    grupo = $("#grupo :selected").val();
    cantpago = document.getElementById('pago').value
    parametros = {
        'usuario': user(), 'nombresala': nombresala,
        'grupo': grupo, 'pago': cantpago
    };
    $.ajax({
        type: "POST",
        url: '../crearjuegoEI/',
        data: parametros,
        success: function (data) {
            console.log(data);
            switch (data.rpta) {
                case 'Sala ya existe':
                    document.getElementById('msj').className="alert alert-danger"
                    document.getElementById('msj').setAttribute("role", "alert");
                    document.getElementById('Resultado').innerHTML = 'Sala ya existe.'
                    $('#msj').removeAttr('hidden')
                    break;
                default:
                    Ajaxobtenersalas(); Ajaxobtenersalasadmin()
                    document.getElementById('msj').className="alert alert-success alert-dismissible fade show"
                    document.getElementById('Resultado').innerHTML = 'Sala creada.'
                    $('#msj').removeAttr('hidden')
            }
        }
    });}


    function Calcularganador(sala) {
      console.log(sala)
        parametros = { 'sala':sala };
        $.ajax({
            type: "POST",
            url: '../obtenerganadorEI/',
            data: parametros,
            success: function (data) {
Ajaxobtenersalas();
Ajaxobtenersalasadmin();
            }
        });

    }
