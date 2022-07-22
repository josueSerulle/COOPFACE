$(document).ready(function () {
    const stepper = new Stepper($('.bs-stepper')[0]);
    
    const params = $.param({amount : $("#monto").val(), cuotes : $("#cuota").val(), interes : (parseFloat($("#interes").val()) / 100), csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()});
    const table = $('#list').DataTable({
        ajax:  `http://127.0.0.1:8000/coop_virtual/loan_calculate/calculate?${params}`,
        paging: true,
        ordering: true,
        autoWidth: false,
        responsive: true,       
        language: {
    
            sProcessing:     "Procesando...",
            sLengthMenu:     "Mostrar _MENU_ registros",
            sZeroRecords:    "No se encontraron resultados",
            sEmptyTable:     "Ningún dato disponible en esta tabla",
            sInfo:           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_",
            sInfoEmpty:      "Mostrando registros del 0 al 0 de un total de 0",
            sInfoFiltered:   "(filtrado de un total de _MAX_ registros)",
            sInfoPostFix:    "",
            sSearch:         "Buscar:",
            sUrl:            "",
            sInfoThousands:  ",",
            sLoadingRecords: "Cargando...",
            oPaginate: {
            sFirst:    "Primero",
            sLast:     "Último",
            sNext:     "Siguiente",
            sPrevious: "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        columns: [
            {"data": 'cuoteNo',         "sClass": "dt-cuoteNo",         "defaultContent": "<i class='na'>-</i>"},
            {"data": 'monthCoute',      "sClass": "dt-monthCoute",      "defaultContent": "<i class='na'>-</i>"},
            {"data": 'interes',         "sClass": "dt-interes",         "defaultContent": "<i class='na'>-</i>"},
            {"data": 'amortizacion',    "sClass": "dt-amortizacion",    "defaultContent": "<i class='na'>-</i>"},
            {"data": 'amortizacionAc',  "sClass": "dt-amortizacionAc",  "defaultContent": "<i class='na'>-</i>"},
            {"data": 'saldoInsoluto',   "sClass": "dt-saldoInsoluto",   "defaultContent": "<i class='na'>-</i>"},
        ],
        columnDefs: [
            {targets: 1, render: $.fn.dataTable.render.number(',', '.', 2, '')},
            {targets: 2, render: $.fn.dataTable.render.number(',', '.', 2, '')},
            {targets: 3, render: $.fn.dataTable.render.number(',', '.', 2, '')},
            {targets: 4, render: $.fn.dataTable.render.number(',', '.', 2, '')},
            {targets: 5, render: $.fn.dataTable.render.number(',', '.', 2, '')}
        ],
    });

    $(document).on("click", ".next", function () { 
        stepper.next();
    });

    $(document).on("click", ".previous", function () { 
        stepper.previous();
    });

    $(function () {
        $('.form-validate').validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                },
                phone: {
                    required: true
                },
                cedula:{
                    cedula: true
                }
            },
            messages: {
                email: {
                    required: "Por favor digite un email valido",
                    email: "Por favor digite un email valido"
                },
                phone: "Por favor digite un email valido",
                required: "Este campo es requerido"
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