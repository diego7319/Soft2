$(document).ready(function () {
    console.log("READY PARA JUEGO PARTIDOS POLLA")

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
                $("#contenido").append(
                    `
                    <div class="en_marco col-sm-4 no_margen row" >
                        <div class="marco" >
                            <div id="${obj[i].pk}" titulo="${obj[i].fields.equipo1} vs ${obj[i].fields.equipo2}" class="col-sm-12 no_margen" >
                            <h3 class="blockquote-footer tx_center"> GRUPO ${obj[i].fields.Grupo} </h3>    
                            <div class="partidos tx_center">
                                    <div class="btn-group btn-group" role="group" aria-label="...">
                                        <button pro="L" type="button" class="apuesta btn btn-light">${obj[i].fields.equipo1}
                                            <br> ${Number(obj[i].fields.monto1).toFixed(2)}</button>
                                        <button pro="E" type="button" class="apuesta btn btn-primary">E
                                            <br> ${Number(obj[i].fields.montoempate).toFixed(2)}</button>
                                        <button pro="V" type="button" class="apuesta btn btn-danger">${obj[i].fields.equipo2}
                                            <br> ${Number(obj[i].fields.monto2).toFixed(2)}</button>
                                    </div>
                            </div>
                        </div>
                    </div>
                    `
                );
                if (i === obj.length - 1) {
                    $(`.apuesta`).bind("click", function () {
                        var id_partido = $(this).parent().parent().parent().attr("id");
                        var pronostico = $(this).attr("pro");
                        swal({
                            title: $(this).parent().parent().parent().attr("titulo"),
                            type: 'question',
                            html: `
                            <h5>Para la opcion ${$(this).html().split("<br>")[0]} 
                            con un multiplicador de ${$(this).html().split("<br>")[1]} se apostara el monto...  </h5>
                            <input id="monto" type="number" class="swal2-input">
                            <input id="multi" class="" type="hidden" value="${$(this).html().split("<br>")[1]}"> `,
                            showCancelButton: true,
                            confirmButtonColor: '#3085d6',
                            cancelButtonColor: '#d33',
                            confirmButtonText: 'Apostar',
                            cancelButtonText: 'Cancelar'
                        }).then((result) => {
                            if (result.value) {
                                var monto = $('#monto').val();
                                var multi = $('#multi').val();
                                var datos = {
                                    idparido: id_partido,
                                    monto: monto,
                                    ganancia: (monto * multi).toFixed(2),
                                    pronostico: pronostico
                                }
                                var res = Math.round(Math.random());
                                console.log(datos);
                                console.log("Res "  + res)
                                if (res == 0) {
                                    swal(
                                        'Perdiste',
                                        'Vuelva a intentarlo',
                                        'error'
                                    )
                                } else {
                                    swal(
                                        'Ganaste',
                                        'Se sumara a tu cuenta el monto de ' + datos.ganancia,
                                        'success'
                                    )
                                }
                            }
                        })
                    });
                }
            }

        }
    });


});