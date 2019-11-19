CODE_MAP = {
    200: "",
    10001: "参数错误"
}


def get_msg(code):
    if code in CODE_MAP:
        return CODE_MAP[code]
    else:
        return ""
