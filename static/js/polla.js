$(document).ready(function () {

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

    var p = 2;
    $.ajax({
        type: "GET",
        url: '../obtenerPartidos/',
        data: p,

        success: function (data) {
            var obj = JSON.parse(data);
            documentos = obj;
            console.log("Cantidado de partidos : " + obj.length);
            for (var i = 0; i < obj.length; i++) {
                if (obj[i].fields.estado) {
                    $("#contenido").append(
                        `
                        <div id="${obj[i].pk}" titulo="${obj[i].fields.equipo1} vs ${obj[i].fields.equipo2}" class="col-sm-6" style="text-align: center;">
                            <div class="partidos">
                                <div class="btn-group btn-group-lg" role="group" aria-label="...">
                                    <button type="button" class="apuesta btn btn-default">${obj[i].fields.equipo1}
                                        <br> ${Number(obj[i].fields.monto1).toFixed(2)}</button>
                                    <button type="button" class="apuesta btn btn-default">E
                                        <br> ${Number(obj[i].fields.montoempate).toFixed(2)}</button>
                                    <button type="button" class="apuesta btn btn-default">${obj[i].fields.equipo2}
                                        <br> ${Number(obj[i].fields.monto2).toFixed(2)}</button>
                                </div>
                            </div>
                        </div>
                        `
                    );
                }
                if (i === obj.length - 1) {
                    $(`.apuesta`).bind("click", function () {
                        var id_partido = $(this).parent().parent().parent().attr("id");
                        swal({
                            title: $(this).parent().parent().parent().attr("titulo"),
                            text: `El la opcion ${$(this).html().split("<br>")[0]} se le declarara como ganador
                            con un multiplicador de ${$(this).html().split("<br>")[1]} `,
                            type: 'warning',
                            showCancelButton: true,
                            confirmButtonColor: '#3085d6',
                            cancelButtonColor: '#d33',
                            confirmButtonText: 'Si',
                            cancelButtonText: 'No',
                            closeOnConfirm: true
                        }).then((result) => {
                            if (result.value) {
                                updatePartido(id_partido, function () {
                                    swal({
                                        type: 'success',
                                        confirmButtonColor: '#3085d6',
                                        confirmButtonText: 'Ok'
                                    }).then((result) => {
                                        location.reload(true);
                                    })
                                });
                            }
                        });
                    });
                }
            }

        }
    });


    function updatePartido(id_partido, callback) {
        var parametros = {
            'usuario': user(),
            'idpartido': id_partido,
            'ganador' : "L"
        };
        $.ajax({
            type: "POST",
            url: '../updatePartido/',
            data: parametros,
            success: function (data) {
                console.log("CORRECTO");
                console.log(data);
                callback();
            }
        });

    }


});