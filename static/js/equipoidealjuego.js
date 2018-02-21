
function obtenerdatos(){
  fetch('../jugadores/')
  .then((resp) => resp.json())  // Call the fetch function passing the url of the API as a parameter
  .then(function(data) {
paises=[]
jugadores=[]
console.log(data)
    for (i in data){
for (j in i){console.log(i)}

};console.log(paises)
  })
  .catch(function() {
      // This is where you run code if the server returns any errors
  });


}



function pais(arr) {
    $("#city").empty();//To reset cities
    $("#city").append("<option>--Select--</option>");
    $(arr).each(function (i) {//to list cities
        $("#city").append("<option value=\"" + arr[i].value + "\">" + arr[i].display + "    </option>")
    });
}
