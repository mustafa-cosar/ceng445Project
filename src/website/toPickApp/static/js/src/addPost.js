

if (typeof(addPost) === 'undefined')
{
    var addPost = {
        submit: function (form) {
            console.log(form);
            jQuery.ajax({
                url: form.attr('action'),
                type: 'POST',
                data: form.serialize(),
                success: function (response) {
                    console.log(response);
                }
            });
        }
    }
}
