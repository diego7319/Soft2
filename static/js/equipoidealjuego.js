paises=[]
jugadores={}
equipoideal=[]
jugadoresusados=[]
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
  console.log((jugadoresusados.indexOf(jugadores[pais][i]) >= 0) + "--"+jugadores[pais][i]+"-"+jugadoresusados)
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
document.getElementById("r"+jugadorid).innerHTML=jugador;
jugadoresusados.push(jugador)
document.getElementById("pais").selectedIndex = "0";


return false;
}

$("#pais").change(function () {
  $("#jugador").empty();
   var select = $("#pais option:selected").val();
   llenarjugadores(select)

                                })
