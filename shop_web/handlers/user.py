from tornado.web import RequestHandler,authenticated
from utils.captcha.captcha import create_validate_code
from utils.response_code import RET,err_msg
import io
from .BaseHandler import BaseHandler
import json
import hashlib
import constants
from utils.session import Session
from utils.auth_check import login_required



class RegisterHandler(BaseHandler):

    def get(self):
        '''显示注册页面'''
        self.render('register.html')

    def post(self, *args, **kwargs):
        json_data = self.request.body
        # 从b变成utf8的形式
        json_data = json_data.decode("utf-8")
        json_data = json.loads(json_data)
        # {"username": "1", "password": "1", "cpassword": "1", "phone": "1", "checkcode": "1"}

        # 这是获取参数
        username = json_data.get("username")
        password = json_data.get("password")
        phone = json_data.get("phone")
        checkcode = json_data.get("checkcode")
        prefix_id = json_data.get("prefix_id")
        e_mail = "123@qq.com"
        # 检查参数完整
        if not all([username,password,phone,checkcode]):
            return self.write({RET.PARAMERROR:"参数不能为空"})
        # 校验图片验证码的问题
        try:
            redis_piccode = self.redis().get(prefix_id)
            redis_piccode=redis_piccode.decode('utf-8')

        except Exception as e:
            print(e)


        # if checkcode != redis_piccode:
        #     print(checkcode)
        #     print(redis_piccode)
        #     return self.write({RET.PICCODEERROR:err_msg[RET.PICCODEERROR]})
        # 正则校验数据格式是否正确
        # 课后作业
        # 插入数据库
        # 加密密码
        password = password.encode('utf-8')
        password = hashlib.md5(password).hexdigest()

        sql = 'insert into user_info(user_name,password,phone,e_mail) VALUES(%(name)s,%(pwd)s,%(tel)s,%(e_mal)s)'
        try:
            user_id = self.db().execute(sql,name=username,pwd=password,tel=phone,e_mal=e_mail)
            print(user_id)
            print('插入成功')
        except Exception as e:
            print(e)



        self.write({"asd":123})


class PicCodeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # 获取之前一次的图片ID
        pre_id = self.get_query_argument('prefix_id')
        # 获取当前的id
        code_id = self.get_query_argument('current_id')
        print('之前一次',pre_id)
        print('当前',code_id)

        # 创建一个文件流
        imgio = io.BytesIO()
        # 生成图片对象和对应字符串
        img, code = create_validate_code()

        # 2.将图片上的文字：code 存入到REDIS数据库中
        # 2.1链接数据库
        #  def setex(self, name, time, value):
        try:
            # 如果之前的图片存在，那么删除,不存在则加入
            if pre_id:
                self.redis().delete(pre_id)
            self.redis().setex(code_id,constants.PIC_CODE_EXPIRS_SECONDS,code)
            print('插入redis成')
        except Exception as e:
            print(e)

        # 将图片信息保存到文件流
        img.save(imgio, 'GIF')
        # 返回图片
        self.write(imgio.getvalue())


class LoginHandler(BaseHandler):
    def get(self):
        # self.set_secure_cookie('name','xiaowang')
        # self.set_cookie('name','pin')
        # print(self.get_secure_cookie('name'))
        self.render('login.html')

    def post(self):
        # 1 取出前段传入的JSON数据并且转为Python形式
        data = self.handerjson()
        # 2、从data中取出用户名和密码
        loginusername = data.get("loginusername")
        loginuserpassword = data.get("loginuserpassword")
        # {'loginuserpassword': '123', 'loginusername': '白白'}
        print(loginusername)
        print(loginuserpassword)
        # 3、校验参数数据是否完整
        if not all([loginuserpassword,loginusername]):
            # print(err_msg[RET.PARAMERROR])
            return self.write({RET.PARAMERROR:err_msg[RET.PARAMERROR]})
        # 4、数据库中的信息进行对比
        # 4.1 查询数据库里是否有此人
        sql = 'select * from user_info where user_name=%(username)s'
        try:
            result = self.db().get(sql,username=loginusername)
            # db.cursor().execute(sql,[loginusername])
            print('瞎写的人的查询结果',result)

        except Exception as e:
            print(e)
            return self.write({"errcode":RET.DBERROR,"errmsg":err_msg[RET.DBERROR]})
        # 4.2 加密密码，用来对比
        loginuserpassword=loginuserpassword.encode("utf-8")
        logpass = hashlib.md5(loginuserpassword).hexdigest()
        # 4.3 进行密码的校验
        if result:
            if result["password"] == logpass:
                print('登陆成功')
                session = Session(self)
                print(session.session_id)
                session.data["name"] = result["user_name"]
                session.data["loginuserpassword"] = result["password"]
                session.save()

            else:
        #         真实的错误是密码错误
                return self.write({"errcode": RET.PASSORUSERERROR, "errmsg": err_msg[RET.PASSORUSERERROR]})

        else:
            # 真实的错误是用户名错误
            return self.write({"errcode": RET.PASSORUSERERROR, "errmsg": err_msg[RET.PASSORUSERERROR]})
        # 使用session配合cookie来做
        self.write({"errcode": RET.OK, "errmsg": err_msg[RET.OK]})


class LogoutHandler(BaseHandler):

    @authenticated
    def get(self):
        session = Session(self)
        session.clear()
        self.render("index.html")
class AuthHandler(BaseHandler):
    @login_required
    def get(self):
        if self.get_current_user():
            redis_data = self.get_current_user()
            self.write({"errcode":RET.OK,"data":redis_data["name"]})
        else:
            self.write(dict(errcode=RET.DBERROR,date=""))