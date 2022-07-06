$(document).ready(function () { 
    $(document).on('click', '#btn-login', function () {
        $(".alert-danger").html("");

        const url   = $("#login-form").attr("action");

        $.ajax({
            method: "POST",
            url: url, 
            data: $("#login-form").serialize(),
            statusCode: {
                200: (response) => {
                    window.location = getUrl();
                },
                400: (response) => {
                    $(".alert-danger").html(`Usuario o Contraseña incorrecta!!`);
                    $(".alert-danger").removeClass("d-none");
                }
            }
        });
    });
});