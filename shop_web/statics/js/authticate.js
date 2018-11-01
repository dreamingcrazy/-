// alert('ok')


$(document).ready(function () {
    $(".logout").hide();
    $(".user-name").hide()
$.get("/authticate",function (data) {
    if (data.errcode=="200"){
        // console.log(data);
        // alert('ok');
        $(".logout").show();
        $(".login").hide();
        $(".user-name span").html(data["data"])
        $(".user-name").show()
        console.log(data["data"])

    }
    else {
        // location.href ='/login'
    }


})



})