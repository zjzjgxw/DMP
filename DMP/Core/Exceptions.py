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
            response.data['code'] = exc.code
            response.data['msg'] = get_msg(exc.code)
    return response


class CustomException(APIException):
    status_code = 200
    code = 200


class ValidationException(CustomException):
    """
    自定义验证错误异常
    """
    code = 10001
