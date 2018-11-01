import torndb_for_python3
import os
import redis
settings = {
    'debug':True,
    'static_path':os.path.join(os.path.dirname(__file__),'statics'),
    'template_path':os.path.join(os.path.dirname(__file__), 'templates'),
    # 'xsrf_cookies':False,
    'cookie_secret':'fkku7vj#x(o@ilr_u(jzh20q@lyi522%!0)qpg0_p0e2^xw49&',
    'login_url':'/login'
}



# 配置日志文件
