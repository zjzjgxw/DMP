CODE_MAP = {
    200: "",
    10001: "参数验证错误"
}


def get_msg(code):
    if code in CODE_MAP:
        return CODE_MAP[code]
    else:
        return ""
