import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import urls
import config
import torndb_for_python3
import redis

tornado.options.define('port',default=9000,type=int, help='server port')

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb_for_python3.Connection(
        host='localhost',
        database='tor_db',
        user='zhanglin',
        password='123456'
        )
        self.redis = redis.StrictRedis(host='localhost', port=6379,
                 db=9)




def main():
    tornado.options.options.log_file_prefix = 'logs/log'
    tornado.options.options.logging = 'none'
    # none为关闭log日志，debug模式
    tornado.options.parse_command_line()
    print(tornado.options.options.port)

    app = Application(urls.urls, **config.settings)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()