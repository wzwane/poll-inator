// Tutorial from: https://realpython.com/blog/python/django-and-ajax-form-submissions/
$(document).ready(function(){

    $('#question-form').on('submit', function(event){
        event.preventDefault();
        console.log("Question submitted!")  // sanity check
        create_question();
    });

    // AJAX for posting
    function create_question(){
        console.log("You've successfully created a question!") // sanity check
        console.log($('#question-text').val())
        $.ajax({
            url : "create_question/", // the endpoint
            type : "POST", // http method
            data : { the_question : $('#question-text').val() }, // data sent with the post request

            success : function(json) {
                $('#question-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#questions").append("<li><a href='/polls/"+json.questionpk+"/'>"+json.question_text+"</a></li>"); //
                console.log("SUCCESS!"); // sanity check
            },

            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    };

    $('#choice-form').on('submit', function(event){
        event.preventDefault();
        console.log("Choice submitted!")  // sanity check
        create_choice();
    });

    // function create_choice(){
    //     console.log("Choice created!") // sanity check
    //     console.log($('#choice-text').val())
    //     $.ajax({
    //         url : "create_choice/", // the endpoint
    //         type : "POST", // http method
    //         data : { the_choice : $('#choice-text').val() }, // data sent with the post request

    //         success : function(json) {
    //             $('#choice-text').val(''); // remove the value from the input
    //             console.log(json); // log the returned json to the console
    //             $("#choices").append("new choice"); //
    //             console.log("SUCCESS!"); // sanity check
    //         },

    //         error : function(xhr,errmsg,err) {
    //             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Error: "+errmsg+
    //                 " <a href='#' class='close'>&times;</a></div>");
    //             console.log(xhr.status + ": " + xhr.responseText);
    //         }
    //     });
    // };



    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
