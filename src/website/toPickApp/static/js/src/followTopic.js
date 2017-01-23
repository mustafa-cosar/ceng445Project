function followTopic(instanceID, id, csrf_token) {
    var myData = {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        'topicID': id
    }
    jQuery.ajax({
        url: 'ajax/followtopic/' + instanceID,
        type: 'POST',
        data: myData,
        success: function(response) {

            if(response.result == "success"){
                topicID = "#" + response.topicID + "following"
                following = response.following
                if(following == true) { // unfollow
                    $(topicID).attr('src', '/static/icons/follow_button.png')
                }
                else { // follow
                    $(topicID).attr('src', '/static/icons/tick_button.png')
                }
            }
        }
    });
}
