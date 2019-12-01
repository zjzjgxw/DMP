from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from DMP.Helps.CodeMap import get_msg


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if isinstance(exc, CustomException):
            response.data['code'] = exc.msg_code
            response.data['msg'] = get_msg(exc.msg_code)
            del response.data['detail']
    return response


class CustomException(APIException):
    status_code = 200
    msg_code = 200

    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)


class ValidationException(CustomException):
    """
    自定义验证错误异常
    """
    default_msg_code = 10001

    def __init__(self, msg_code=None, detail=None, code=None):
        if msg_code is None:
            self.msg_code = self.default_msg_code
        else:
            self.msg_code = msg_code
        super().__init__(detail, code)


class UserNotExistException(CustomException):
    """
    用户不存在错误异常
    """
    msg_code = 10004


class AccountPasswordWrongException(CustomException):
    """
    账号密码错误
    """
    msg_code = 10005
