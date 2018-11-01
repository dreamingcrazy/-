// alert('ok')

var prefix_id = '';

function getImagecode() {
    var current_id = new Date().getTime();
    $('.piccode img').attr('src','/piccode?prefix_id='+prefix_id+'&current_id='+ current_id)
    prefix_id = current_id
     // /piccode?prefix_id =123 & current_id = 456
}

function ajaxPostfunc() {
    username = $('#username').val();
    password = $('#password').val();
    cpassword = $('#cpassword').val();
    phone = $('#phone').val();
    checkcode= $('#checkcode').val();

    if(!username){
        alert('kongzhi');
        return

    }
    if(password != cpassword){

        alert('两次密码不一致');
        return

    }
    var data = {
        "username":username,
        "password": password,
        "cpassword":cpassword,
        "phone":phone,
        "checkcode": checkcode,
        "prefix_id":prefix_id
    };
    var data_json = JSON.stringify(data)
    // alert(Object.keys(data).length)
    // alert(data)
    // console.log(data)

    $.ajax({
        url:'/register',
        method:'POST',
        data :data_json,
        contentType:'application/json, charset=utf-8',
        dataType:'json',
        success:function () {
            location.href = '/login'
        }
    })
}


$(document).ready(function () {
       getImagecode();

})