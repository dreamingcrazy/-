from tornado.web import RequestHandler
from .BaseHandler import BaseHandler
from  utils.response_code import RET,err_msg
from constants import LIST_CACHE_EXPIRS_SECONDS,LIST_PER_PAGE_NUM

class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self):
        self.write('OK')
class ListHandler(BaseHandler):
    '''这是处理商品的列表页'''
    def get(self,style_id):
        print(style_id)
        sort = self.get_query_argument('sort')
        page = self.get_query_argument('page')

        sql = 'select * from goodsdetail where type_id=%(type)s '
        result = self.db().query(sql,type=style_id)
        print(result)
        self.render('goodslist.html',**{"data":result})



class ListHandler2(BaseHandler):
    def get(self):
        sort = self.get_query_argument('sort','')
        style_id = self.get_query_argument('style_id','')
        page = self.get_query_argument('page','')
        try:
            page = int(page)
        except Exception as e:
            page = 1

        sql = 'select name,real_price,unite from goodsdetail where type_id=%(type_id)s'
        if sort == '1':
            sql = sql +'order by real_price asc'
        elif sort == '2':
            sql = sql + 'order by sales'
        elif sort == '3':
            sql = sql + 'order by create_time desc'
        else:
            sql = sql + 'order by real_pice desc'
        sql = sql + ' limit %s,8' % str((page - 1) * 8 +1)
        result = self.db().query(sql,type_id=style_id)
        handler_data = []
        for obj in result:
            obj['real_price'] =  str(obj['real_price'])
            handler_data.append(obj)
        self.write({'errcode':RET.OK,'errmsg':err_msg[RET.OK],'goodsdata':handler_data})


class DetaileHandler(BaseHandler):
    '''这是商品的详情页面'''
    def get(self,goods_id):
        sql = 'select * from goodsdetail where id=%(id)s'
        try:
            result = self.db().get(sql,id=goods_id)
        except Exception as e:
            print(e)
        self.render('detailgoods.html',**{"data":result})