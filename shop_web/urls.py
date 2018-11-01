from tornado.web import StaticFileHandler
from handlers.goods import IndexHandler,ListHandler,DetaileHandler
from handlers.user import RegisterHandler,PicCodeHandler,LoginHandler,LogoutHandler,AuthHandler

import os
urls = [
    (r'/',IndexHandler),
    (r'/register',RegisterHandler),
    (r'/piccode',PicCodeHandler),
    (r'/login',LoginHandler),
    (r'/logout',LogoutHandler),
    (r'/authticate',AuthHandler),
    (r'/list/(\d+)', ListHandler),  # 展示商品的列表页
    (r'/detail/(\d+)', DetaileHandler),
    (r'/(.*)',StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),'templates'),default_filename='index.html')),


    ]