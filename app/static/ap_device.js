$(function(){
    $('#add_ap_btn').click(function(){
        location.href = "edit"
    });

    $('tbody tr td span').click(function(){
        alert($(this).attr("id"))
        location.href = "delete_deployer?id="+$(this).attr("id")
     });

     $('myTab li:eq(1) a').tab('show');

});