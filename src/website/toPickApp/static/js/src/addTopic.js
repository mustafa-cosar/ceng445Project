
function addTopic(component) {

    jQuery.ajax({
        url: component.find('form').attr('action'),
        type: 'POST',
        data: component.find('form').serialize(),
        success: function(response) {
            console.log(response);
            if (response.result == 'success')
            {
                alert('Topic has been added succesfully!');
            }
            else if(response.error)
            {
                alert('An error occurred: ' + response.error);
            }
        }
    });
};
