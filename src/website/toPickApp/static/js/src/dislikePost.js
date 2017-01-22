function dislikePost(instanceID, id, csrf_token) {

    var myData = {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        'postID': id
    }
    jQuery.ajax({
        url: 'ajax/adddislike/' + instanceID,
        type: 'POST',
        data: myData,
        success: function(response) {
            if(response.result == "fail"){

            }
            else {
                postID = response.postID;
                id = "#" + postID + "dislikecount";
                imgid = "#" + postID + "disliked";
                newCount = response.count;
                newCount2 = response.count2;
                isDislike = response.isDislike;
                $(id).html(newCount);
                if (isDislike == true){
                    $(imgid).attr('src', '/static/icons/dislike_white.png')
                    $(imgid).attr('alt', 'notdisliked')
                }
                else {
                    likeid = "#" + postID + "liked";
                    likecount = "#" + postID + "likecount";
                    $(likecount).html(newCount2)
                    $(likeid).attr('src', '/static/icons/like_white.png')
                    $(likeid).attr('alt', 'notliked')
                    $(imgid).attr('src', '/static/icons/dislike_black.png')
                    $(imgid).attr('alt', 'disliked')
                }
            }
        }
    });
}
