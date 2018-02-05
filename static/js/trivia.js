$.ajax({
  url: form.attr(""),
  data: form.serialize(),
  dataType: 'json',
  success: function (data) {
    if (data.is_taken) {
      alert(data.error_message);
    }
  }
});

$("nuevapregunta").click(function(){
    $.get("mostrarpregunta/",

    function(data, status){
        console.log(data)
    });
});
