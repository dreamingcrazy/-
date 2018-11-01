
class RET:
    OK = "200"
    PATHERROR = "404"
    SEVEREROOR = "500"
    PARAMERROR = "5001"
    PICCODEERROR = "5002"
    PASSORUSERERROR = "5003"
    DBERROR = "5004"
    AUTHERROR = "5005"



err_msg ={
    RET.PARAMERROR:"参数不完整",
    RET.PICCODEERROR:"图片验证码错误",
    RET.PASSORUSERERROR: "用户名或者密码错误",
    RET.DBERROR:"数据库错误",
    RET.OK:"请求成功",
    RET.AUTHERROR:"用户未登录"
}