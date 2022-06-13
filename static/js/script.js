$(document).ready(function() {
    $("#card-proj").hover(function() {
        $(this).css('background-color', 'red');
    }, function() {
        $(this).css('background-color', 'white')
    });
})