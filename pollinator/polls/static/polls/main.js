// Tutorial from: https://realpython.com/blog/python/django-and-ajax-form-submissions/
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log('form submitted!')
    create_post();

})

function create_post(){
    console.log("You've successfully created a post!")
    $.ajax({
        url : "create_post/",
        type : "POST",
        data : { a_post : $('#post-text').val() },

        success : function(json) {
            $('#post-text').val('');
            console.log(json);
            console.log("SUCCESS!");

        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }



    })


}