
function getTopicsFilter(componentID, filterID)
{
    jQuery.ajax({
        url: 'ajax/filtertopics/' + filterID,
        type: 'POST',
        data: $('#filterTopicsForm' + componentID).serialize(),
        success: function(response){
            if (!response.error)
            {
                $('#topicList' + componentID).html(response);
            }
        }
    });
};
