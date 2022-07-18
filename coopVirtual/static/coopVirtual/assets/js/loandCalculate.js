$(document).ready(function () {
    
    $(document).on("change", "#tipo-prestamo", function () { 
        const type = $('option:selected', this).val();

        if(parseInt(type) === 1){
            $("#monto").val(45000.00).prop('readonly',true);
        } else if ($('#monto').prop('readonly')){
            $("#monto").val('').prop('readonly',false);
        }
    });

    $(document).on("click", "#amortizar", loadCalculate);

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
        
        $('#list').DataTable().destroy();

        $('#list').DataTable({
            ajax:  `${getUrl()}loan_calculate/calculate?${params}`,
            paging      : false,
            ordering    : true,
            autoWidth   : false,
            responsive  : true,
            deferRender : true,
	        retrieve    : true,
	        processing  : true,       
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