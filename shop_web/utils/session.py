import uuid
import constants
import json
class Session(object):
    def __init__(self,handler_obj):
        '''这是初始化'''
        self.handler = handler_obj
        self.session_id = handler_obj.get_secure_cookie("session")
        # self.session_id = uuid.uuid4().hex
        # self.handler.set_secure_cookie('session', self.session_id)
        # 这是返回给前端的安全cookie，包含我的session_id,但是session_id会经过加密
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            self.handler.set_secure_cookie("session",self.session_id)
            self.data = {}
        else:
            try:
                data_redis = handler_obj.redis().get(self.session_id)
                print('redis里面的session_id对应的值',data_redis)
            except Exception as e:
                print(e)
            if not data_redis:
                self.data = {}
            else:
                self.data = json.loads(data_redis.decode("utf-8"))



    def save(self):
        '''将session数据存入redis数据库'''
        # redis :k v
        import json
        json_data = json.dumps(self.data)
        try:
            self.handler.redis().setex(self.session_id, constants.SESSION_EXPIRS_SECONDS,json_data)
            # def setex(self, name, time, value):
        except Exception as e:
            print(e)
            print('session插入redis失败')

    def clear(self):
        '''从redis里面清除session'''
        try:
            self.handler.redis().delete(self.session_id)
        except Exception as e:
            print(e)
            print('redis删除session失败')
        self.handler.clear_cookie("session")