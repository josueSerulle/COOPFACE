$(document).ready(function () {
    
    $('#list').DataTable({
        ajax:  `${getUrl()}loan_application/datatable`,
        paging      : true,
        ordering    : true,
        autoWidth   : false,
        responsive  : true,       
        language : {
            sProcessing     : "Procesando...",
            sLengthMenu     : "Mostrar _MENU_ registros",
            sZeroRecords    : "No se encontraron resultados",
            sEmptyTable     : "Ningún dato disponible en esta tabla",
            sInfo           : "Mostrando registros del _START_ al _END_ de un total de _TOTAL_",
            sInfoEmpty      : "Mostrando registros del 0 al 0 de un total de 0",
            sInfoFiltered   : "(filtrado de un total de _MAX_ registros)",
            sInfoPostFix    : "",
            sSearch         : "Buscar:",
            sUrl            : "",
            sInfoThousands  : ",",
            sLoadingRecords : "Cargando...",
            oPaginate : {
            sFirst      : "Primero",
            sLast       : "Último",
            sNext       : "Siguiente",
            sPrevious   : "Anterior"
            },
            oAria : {
                sSortAscending  : ": Activar para ordenar la columna de manera ascendente",
                sSortDescending : ": Activar para ordenar la columna de manera descendente"
            }
        },
        columns: [
            {"data": 'socio',           "sClass": "dt-socio",           "defaultContent": "<i class='na'>-</i>"},
            {"data": 'tipoPrestamo',    "sClass": "dt-tipoPrestamo",    "defaultContent": "<i class='na'>-</i>"},
            {"data": 'fechaSolicitud',  "sClass": "dt-fechaSolicitud",  "defaultContent": "<i class='na'>-</i>"},
            {"data": 'cuotas',          "sClass": "dt-cuotas",          "defaultContent": "<i class='na'>-</i>"},
            {"data": 'monto',           "sClass": "dt-monto",           "defaultContent": "<i class='na'>-</i>"},
            {"data": 'estado',          "sClass": "dt-estado",          "defaultContent": "<i class='na'>-</i>"},
            {"data": 'accion',          "sClass": "dt-accion",          "width": "5%",  "defaultContent": "<i class='na'>-</i>"},
        ],
        columnDefs: [
            {targets: 4, render: $.fn.dataTable.render.number(',', '.', 2, '')},
        ],
        createdRow: function (row, data, index) {
            $('.dt-estado', row).html(statusButton(data));
            $('.dt-accion', row).html(actionLink(data));
        }
    });


    $(document).on("change", "#tipo-prestamo", function () { 
        const type = $('option:selected', this).val();

        if(parseInt(type) === 1){
            $("#monto").val(45000.00).prop('readonly',true);
        } else if ($('#monto').prop('readonly')){
            $("#monto").val('').prop('readonly',false);
        }
    });

    $(function () {
        $('.form-validate').validate({
            rules: {
                cuotas: {
                    required: true,
                    max: 60,
                    min: 1,
                },
                tipo_prestamo: {
                    required: true,
                }
            },
            messages: {
                cuotas: {
                    max: "Numero de cuotas menor o igual a 60",
                    min: "Numero de cuotas mayor o igual a 1"
                },
            },
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).removeClass('is-invalid');
            }
        });
    });
});

const statusButton = (data) => {
    let statusData = {};

    switch (data.estado) {
        case 1:
            statusData = {class : "info", text : "Recibido"}
            break;
        case 2: 
            statusData = {class : "warning", text : "Revisando"}
            break;
        case 3: 
            statusData = {class : "success", text : "Aprobado"}
            break;
        case 4: 
            statusData = {class : "danger", text : "Declinada"}
            break;
    };

    return `<button class="btn btn-${statusData.class} btn-block btn-sm">${statusData.text}</button>`;
};

const actionLink = (data) => {
    return `<a class="btn btn-warning btn-sm" href="${getUrl()}loan_form/${data.id}" ><i class="fas fa-pencil-alt"></i></a>`;
};