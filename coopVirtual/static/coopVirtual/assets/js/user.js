$(document).ready(function () {
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