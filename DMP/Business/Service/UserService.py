from DMP.Business.Models.User import UserSerializer
from DMP.Core.Service import BasicService


class UserService(BasicService):
    """
    用户服务
    """

    @classmethod
    def create_admin_user(cls, email, business_id):
        pass
