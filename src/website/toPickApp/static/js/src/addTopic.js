
function addTopic(component, instanceID) {

    jQuery.ajax({
        url: component.find('form').attr('action'),
        type: 'POST',
        data: component.find('form').serialize(),
        success: function(response) {
            console.log(response);
            if (response.result == 'success')
            {
                $('#success'+instanceID).show('fast');
                setTimeout(function(){
                    $('#success'+instanceID).hide('fast');
                }, 3000);
            }
            else if(response.error)
            {
                alert('An error occurred: ' + response.error);
            }
        }
    });
};
