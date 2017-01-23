

if (typeof(addPost) === 'undefined')
{
    var addPost = {
        submit: function (form, instanceID) {
            console.log(form);
            jQuery.ajax({
                url: form.attr('action'),
                type: 'POST',
                data: form.serialize(),
                success: function (response) {
                    if (!response.error)
                    {
                        console.log(response);
                        $('#success'+instanceID).show('fast');
                        setTimeout(function(){
                            $('#success'+instanceID).hide('fast');
                        }, 3000);
                        form.find('textarea').val('');
                    }
                    else
                    {
                        alert('An error occurred.');
                    }
                }
            });
        }
    }
}
