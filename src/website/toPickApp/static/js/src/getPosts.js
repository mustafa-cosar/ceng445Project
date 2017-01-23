function getPosts(component, instanceID) {

    var myData = {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
    };

    jQuery.ajax({
        url: '/ajax/getposts/'+ instanceID,
        type: 'POST',
        data: myData,
        success: function(response) {
            if (!response.error){
                $('#posts'+instanceID).html(response);
            }
        }
    });
}
