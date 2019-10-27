from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# 不用APIViewSet 的话路由怎么定义，想要自定义路由怎么办，比如登录功能,下载文件功能
# url 想写在fileSystem 怎么办
# 多个模块url 要怎么组织？

class FileUploadAPIView(APIView):
    """
    upload File Class
    """

    def get(self, request):
        return Response("heelo")

    def download(self):
        pass
