function obtenerpregunta(){

    $.get("../mostrarpregunta/",

    function(data){
        console.log()

        document.getElementById("pregunta").innerHTML = data.pregunta;
   document.getElementById("d0").innerHTML=data.d0
        document.getElementById("d1").innerHTML=data.d1
        document.getElementById("d2").innerHTML=data.d2
        document.getElementById("d3").innerHTML=data.d3
    });
};
