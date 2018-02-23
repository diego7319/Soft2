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

paises=[]
jugadores={}
equipoideal=[]
jugadoresusados=[]

inicial_key=['rarquero','rcentral1','rcentral2','rlateralD','rlateralI',
'rvolante1','rvolante2','rcarrileroI','rcarrileroD','rmediapunta',
'rdelantero'
]
inicial={'rarquero':'Arquero','rcentral1':'Central 1',
'rcentral2':'Central 2','rlateralD':'Lateral Derecho',
'rlateralI':'Lateral Izquierdo','rvolante1':'Volante 1',
'rvolante2':'Volante 2','rcarrileroI':'Carrilero Izquierdo','rcarrileroD':'Carrilero Derecho',
'rmediapunta':'Media Punta','rdelantero':'Delantero'}

final={'rarquero':'Arquero','rcentral1':'Central 1',
'rcentral2':'Central 2','rlateralD':'Lateral Derecho',
'rlateralI':'Lateral Izquierdo','rvolante1':'Volante 1',
'rvolante2':'Volante 2','rcarrileroI':'Carrilero Izquierdo','rcarrileroD':'Carrilero Derecho',
'rmediapunta':'Media Punta','rdelantero':'Delantero'}

function confirmarOnceIdeal(){
  valido=0;

for (i in inicial){
if(final[i]==inicial[i]) {valido+=1}else {}

}
return valido
}

function obteneridradiobutton(){
    d=$('input[type=radio]:checked', '#listajug').attr('id');
    console.log(d);return d
  };

function borrarjugadoresusados(datos){
if (datos in jugadoresusados)
{jugadoresusados = jugadoresusados.filter(item => item !== datos)
}
}

function llenarselectpais(datos,selectid){

  select = document.getElementById(selectid);
for (i in datos){
var opt = document.createElement('option');
opt.id=datos[i];opt.innerHTML=datos[i]
select.appendChild(opt)

                }
                                        }

function llenarjugadores(pais){

  select = document.getElementById('jugador');

for (i in jugadores[pais]){

if (jugadoresusados.indexOf(jugadores[pais][i]) >= 0){console.log("ya usado-"+jugadores[pais][i])} else {
  var opt = document.createElement('option');
  opt.id=jugadores[pais][i];opt.innerHTML=jugadores[pais][i]
  select.appendChild(opt)
                          }}

}

function obtenerdatos(){
  fetch('../jugadores/')
  .then((resp) => resp.json())  // Call the fetch function passing the url of the API as a parameter
  .then(function(data) {
    for (i in data){
for (j in data[i]){paises.push(j);jugadores[j]=data[i][j];
                  }
}llenarselectpais(paises,'pais','');
})
  .catch(function() {
      // This is where you run code if the server returns any errors
  });

}

function agregarjugador(){
jugadorid=obteneridradiobutton();
jugadoranterior=document.getElementById("r"+jugadorid).innerText
jugadoresusados = jugadoresusados.filter(item => item !== jugadoranterior)
pais=$("#pais option:selected").val();
jugador=$("#jugador option:selected").val();
tmp="r"+jugadorid
$("#jugador").empty();
if (jugador==null){}else{
document.getElementById(tmp).innerHTML=jugador;
final[tmp]=jugador;
console.log('0000')
jugadoresusados.push(jugador);
document.getElementById("pais").selectedIndex = "0";
$("#jugador").empty();}

return false;
}

$("#pais").change(function () {
  $("#jugador").empty();
   var select = $("#pais option:selected").val();
   llenarjugadores(select)})

function confirmarjugadores() {
if (confirmarOnceIdeal()==0){
  parametros={'g':final,'sala':sala,'usuario':user(),'grupo':rrgrupo()}
       $.ajax({
           type: "POST",
           url: '../scoreEI/',
           data: parametros,
           success: function (data) {

    if (data.t==1)    {
      document.getElementById('g2').innerHTML =data.rpta
      $('#gg').removeAttr('hidden')

    }else{
             document.getElementById('g2').innerHTML =data.rpta
             $('#gg').removeAttr('hidden')
}document.getElementById('gg').className=='alert alert-info'
           }
       });


   }     else {
     document.getElementById('g2').innerHTML ="Complete la lista"
     $('#gg').attr("class",'alert alert-warning')

     $('#gg').removeAttr('hidden')

   }       }
