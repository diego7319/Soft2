$(document).ready(function () {
    console.log("ANALITICA");

    $.ajax({
        type: "GET",
        url: '../getAnalitica',
        data: 1,
        success: function (data) {
            console.log("CORRECTO");
            console.log(data);
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ["Ver", "Registro", "Login", "Logout", "Invitar", "Crear Grupo", "Respuesta Invitacion"],
                    datasets: [{
                        label: '# de acciones',
                        data: [data.ver, data.registro, data.login, data.logout, data.invitar, data.crear_grupo, data.rpta_invitacion],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 99, 132, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)',
                            'rgba(255,99,132,1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
    });


});