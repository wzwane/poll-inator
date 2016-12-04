// Tutorial from: https://realpython.com/blog/python/django-and-ajax-form-submissions/
$(document).ready(function(){

    $('#question-form').on('submit', function(event){
        event.preventDefault();
        console.log("Question submitted!")
        create_question();
    });

    function create_question(){
        console.log("You've successfully created a post!")
        console.log($('#question-text').val())
        $.ajax({
            url : "create_question/",
            type : "POST",
            data : { a_post : $('#question-text').val() },

            success : function(json) {
                $('#question-text').val('');
                console.log(json);
                console.log("SUCCESS!");

            },

            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    var questionsList = [];
    var questionId = 0;
    var newQuestionTitle = document.getElementById("questionTitle");
    var newQuestionDescription = document.getElementById("questionDescription");


    function insertQ () {
        displayQ();
        clearQ();
    }

    function displayQ(){
        questionId += 1;
        console.log(questionId)
        questionsList.push({id: questionId, title: newQuestionTitle.value, des:newQuestionDescription.value })
        $(".questions").append($('<div class="question shadowedBox">')
        .append($('<div class="questionInfo">')
            .append($('<h3 class="questionTitle">')
            .append($("<p>").append(newQuestionTitle.value)))
            .append($('<p class="questionContent">').append($("<p>").append(newQuestionDescription.value))))
            .append($('<div class="options"><button class="btn btn-primary upvote">^</button><button class="btn btn-primary downvote">V</button><button class="btn btn-primary comment">Comment</button>')

            ));
        console.log(questionsList)
    }


    function clearQ(){
        newQuestionTitle.value = "";
        newQuestionDescription.value = "";
    }
});
