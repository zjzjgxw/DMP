import jwt


class JwtToken:
    secret_key = "123456"

    def get_token(self, **kwargs):
        return jwt.encode(kwargs, self.secret_key, algorithm='HS256')

    def get_info(self, token):
        return jwt.decode(token, self.secret_key)


def auth_permission_required(perms):
    """
    登录权限验证
    :param perms:
    :return:
    """

    def decorator(func):
        def wrapper(view_set, request, *args, **kw):
            token = request.META.get('HTTP_AUTHORIZATION')
            jwt_object = JwtToken()
            user = jwt_object.get_info(token)
            request.dmp_user = user
            return func(view_set, request, *args, **kw)

        return wrapper

    return decorator
