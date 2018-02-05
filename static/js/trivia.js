function obtenerpregunta(){

    $.get("../mostrarpregunta/",

    function(data){
        var parsed = $.parseJSON(data);
        console.log(parsed)
        document.getElementById("pregunta").innerHTML = 'a';


    });
};
