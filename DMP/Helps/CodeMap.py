CODE_MAP = {
    200: "",
    999: "查找不到对应信息",
    10001: "参数验证错误",
    10002: "请输入账号",
    10003: "请输入密码",
    10004: "用户不存在",
    10005: "账号密码错误",
    10006: "无效token,认证失败",
    10007: "参数类型错误",
    10008: "用户账号已经存在",
    10009: "参数必须为int",
    10010: "参数数据范围错误",
    10011: "权限不足",
    20010: "缺少规格参数",
    20011: "属性参数有误",
    20012: "缺少name属性",
    20013: "缺少option属性",
    20014: "name最多支持10个字符",
    20015: "option最多支持10个字符",
    20016: "缺少attribute_list或者attribute_list参数内容错误",
    20017: "缺少main_images或者main_images参数内容错误",
    20018: "缺少describe_images或者describe_images参数内容错误"
}


def get_msg(code):
    if code in CODE_MAP:
        return CODE_MAP[code]
    else:
        return ""
