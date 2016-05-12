$(function(){
    $('#add_area_btn').click(function(){
        location.href = "/add_area"
    });

    $('#upload_image_btn').click(function(){

            $.ajaxFileUpload({
                url:'/upload_image',//处理图片脚本
                secureuri :false,
                fileElementId :'fileToUpload',//file控件id
                dataType : 'json',
                success : function (data, status){
                    if(typeof(data.error) != 'undefined'){
                        if(data.error != ''){
                            alert(data.error);
                        }else{
                            alert(data.msg);
                        }
                    }},
                    error: function(data, status, e){
                        alert(e);
                    }
            })
//         var filename = $("#file").val();
//         $.ajax({
//              type: "POST",
//              url: "/upload_image",
//              enctype: 'multipart/form-data',
//              data: {
//                file: filename
//              },
//              success: function () {
//                alert("Data Uploaded: ");
//              }
//          });
    });

    $('tbody tr td span').click(function(){
        alert($(this).attr("id"))
        location.href = "/detail_area"
     });
});