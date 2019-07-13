var num = 50; //number of pixels before modifying styles
$(window).bind('scroll', function () {
    if ($(window).scrollTop() > num) {
        $('.menu').addClass('fixed');
    } else {
        $('.menu').removeClass('fixed');
    }
});
/* attach a submit handler to the form */
$("#feedbackForm").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    /* Prevent abuse of people submitting multiple times */
    $("#submit").attr('disabled', 'disabled');
    /* Show some loading icon so that the user knows something happened */
    $("#result").empty().append('Submitting...');
    /* get some values from elements on the page: */
    var $form = $(this),
        url = $form.attr('action');
    /* Send the data using post */
    var posting = $.post(url, {
        Name: $('#name').val(),
        Email: $('#email').val(),
        Subject: $('#subject').val(),
        Message: $('#message').val()
    });
    /* Put the results in a div */
    posting.done(function(data) {
        if (data.result == "success") {
            $("#result").empty().append("Your feedback has been submitted, thank you!");
        } else {
            $("#result").empty().append("Oops! Something bad happened. Please reload this page and try again.");
            $('#submit').removeAttr('disabled');
        };
    });
});
