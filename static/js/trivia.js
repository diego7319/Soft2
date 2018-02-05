function obtenerpregunta(){

    $.get("../mostrarpregunta/",

    function(data){
        console.log(data)
    });
};
