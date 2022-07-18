$(document).ready(function () {
    
    $('#list').DataTable({
        ajax:  `${getUrl()}loand_application/datatable`,
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
            {"data": 'tipoPrestamo',    "sClass": "dt-tipoPrestamo",    "defaultContent": "<i class='na'>-</i>"},
            {"data": 'fechaSolicitud',  "sClass": "dt-fechaSolicitud",  "defaultContent": "<i class='na'>-</i>"},
            {"data": 'cuotas',          "sClass": "dt-cuotas",          "defaultContent": "<i class='na'>-</i>"},
            {"data": 'monto',           "sClass": "dt-monto",           "defaultContent": "<i class='na'>-</i>"},
            {"data": 'estado',          "sClass": "dt-estado",          "defaultContent": "<i class='na'>-</i>"},
            {"data": 'accion',          "sClass": "dt-accion",          "width": "5%",  "defaultContent": "<i class='na'>-</i>"},
        ],
        columnDefs: [
            {targets: 3, render: $.fn.dataTable.render.number(',', '.', 2, '')},
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

    $(document).on("change", "#tipo-prestamo, #monto, #cuotas", loadCalculate);

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

const loadCalculate = () => {
    const interes = parseFloat($('option:selected', '#tipo-prestamo').data().interes),
        amount  = $("#monto").val(),
        cuotes  = $("#cuotas").val();

    if($('.form-validate').valid()) {

        const params = $.param({amount : amount, cuotes : cuotes, interes : (interes / 100), csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()});
        
        $('#list2').DataTable().destroy();

        $('#list2').DataTable({
            ajax:  `${getUrl()}loan_calculate/calculate?${params}`,
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
    }
};

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
            statusData = {class : "danger", text : "Denegada"}
            break;
    };

    return `<button class="btn btn-${statusData.class} btn-block btn-sm">${statusData.text}</button>`;
};

const actionLink = (data) => {
    let html =`<div class="btn-group"><button class="btn btn-secondary btn-sm" data-id = "${data.id}"><i class="fas fa-file-alt"></i></button>`;

    if(parseInt(data.estado) === 1){
        html += `<button class="btn btn-danger btn-sm delete" data-id = "${data.id}"><i class="fa fa-times"></i></button>`;
    }

    html += '</div>';
    return html;
};