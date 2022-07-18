$(document).ready(function(){
    jQuery.extend(jQuery.validator.messages, {
        required: "Este campo es requerido",
        email   : "Por favor digitar una direccion de correo valido.",
    });

    //Initialize inputmask Elements
    $('[data-mask]').inputmask();

    $(".currency").inputmask('decimal', {
        'groupSeparator': ',',
        'digits': 2,
        'radixPoint': ".",
        'prefix': '$ ',
        'placeholder': ''
    });

    //Initialize Select2 Elements
    $('.select2').select2({
        theme: 'bootstrap4'
    });

    $(document).on("click", ".cancel", function () { 
        let module = $(this).data().moduleName;
        
        module = (typeof module == 'undefined')? '' : module;

        Swal.fire({
            title: 'Atención',
            icon: 'warning',
            text: 'No se han guardado los cambios. Deseas salir y descartar los cambios?',
            showCancelButton: true,
            confirmButtonColor: '#ef5350',
            confirmButtonText: 'Salir',
            cancelButtonText: `Cancelar`,
            showCloseButton: true,
        }).then((result) => {
            if (result.isConfirmed) {
                window.location = getUrl() + module;
            } 
        });
    });
});

const getUrl = () => {
    return "http://127.0.0.1:8000/coop_virtual/";
};