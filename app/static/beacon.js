$(function(){

    $('table tr td #edit-beacon-btn').click(function(){
        location.href='edit?id='+$(this).attr('name');
    });

});