// alert('ok')


function loginClick() {
    var loginusername = $(".loginusername").val();
    var loginuserpassword = $(".loginuserpassword").val();
    var data = {
        "loginuserpassword":loginuserpassword,
        "loginusername": loginusername
    };
    data_json = JSON.stringify(data);
    $.ajax({

        url: "/login",
        method: "POST",
        data: data_json,
        contentType: "application/json",
        success: function (data) {
            // alert('ok')
            if(data.errcode=="200"){
                location.href = "/"
            }else {
                alert(data.errmsg)
            }


        }
    })


}