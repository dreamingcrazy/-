from tornado.web import RequestHandler
import json
from utils.session import Session


class BaseHandler(RequestHandler):


    def db(self):
        return self.application.db


    def redis(self):
        return self.application.redis
    def handerjson(self):
        json_data = self.request.body
        json_data = json_data.decode('utf-8')
        json_data = json.loads(json_data)
        # print(json_data)
        return json_data
    def get_current_user(self):
        self.session = Session(self)
        return self.session.data
