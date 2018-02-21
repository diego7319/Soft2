
function obtenerdatos(){
  fetch('../jugadores/') // Call the fetch function passing the url of the API as a parameter
  .then(function() {
      // Your code for handling the data you get from the API
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
