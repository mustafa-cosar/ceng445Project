function likePost(instanceID, id, csrf_token) {

    var myData = {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        'postID': id
    }
    jQuery.ajax({
        url: 'ajax/addlike/' + instanceID,
        type: 'POST',
        data: myData,
        success: function(response) {
            if(response.result == "fail"){

            }
            else {
                postID = response.postID;
                id = "#" + postID + "likecount";
                imgid = "#" + postID + "liked";
                newCount = response.count;
                newCount2 = response.count2;
                isLike = response.isLike;
                $(id).html(newCount);
                if (isLike == true){
                    $(imgid).attr('src', '/static/icons/like_white.png')
                    $(imgid).attr('alt', 'notliked')
                }
                else {
                    dislikeid = "#" + postID + "disliked";
                    dislikecount = "#" + postID + "dislikecount";
                    $(dislikecount).html(newCount2)
                    $(dislikeid).attr('src', '/static/icons/dislike_white.png')
                    $(dislikeid).attr('alt', 'notdisliked')
                    $(imgid).attr('src', '/static/icons/like_red.png')
                    $(imgid).attr('alt', 'liked')
                }
            }
        }
    });
}
