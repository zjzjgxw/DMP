CODE_MAP = {
    200: "",
    999: "查找不到对应信息",
    10001: "参数验证错误",
    10002: "请输入账号",
    10003: "请输入密码",
    10004: "用户不存在",
    10005: "账号密码错误",
    10006: "无效token,认证失败",
    10007: "参数类型错误"
}


def get_msg(code):
    if code in CODE_MAP:
        return CODE_MAP[code]
    else:
        return ""
