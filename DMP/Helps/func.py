from DMP.Helps.CodeMap import get_msg


def return_format(code=200, msg='', data=None):
    if len(msg) == 0:
        msg = get_msg(code)
    return {"code": code, "msg": msg, "data": data}
