$(document).ready(function() {
    $("#login_form").submit(function(event) {
        event.preventDefault();
        data = new FormData($('#login_form')[0]);

        $.ajax({
            type: 'POST',
            url: '/login/',
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false
        });/*.done(function(json) {
            if (json.success) {
                window.location.replace(json.url);
            } else {
                $.toast({
                    heading: 'Error',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'error',
                    position: 'top-right',
                })

            }
        }).fail(function(jqXHR, status, errorThrown) {
            //console.log(errorThrown);
            //console.log(jqXHR.responseText);
            //console.log(jqXHR.status);
            //showSuccessMessage('');
            alert(status);
        });*/
    });

});