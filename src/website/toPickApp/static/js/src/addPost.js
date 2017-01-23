

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
                    console.log(response);
                    $('#success'+instanceID).show('fast');
                    setTimeout(function(){
                        $('#success'+instanceID).hide('fast');
                    }, 3000);
                }
            });
        }
    }
}
