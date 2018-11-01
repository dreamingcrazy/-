import functools
from utils.response_code import RET,err_msg


def login_required(func):
    @functools.wraps(func)
    def wrapper(hanler_obj,*args,**kwargs):
        if hanler_obj.get_current_user():
            func(hanler_obj,*args,**kwargs)
        else:
            hanler_obj.write({"errcode":RET.AUTHERROR,"errmsg":err_msg[RET.AUTHERROR]})

    return wrapper