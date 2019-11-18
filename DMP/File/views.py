from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.File.Service.FileService import FileService


# Create your views here.
class FileViewSet(ViewSet):
    """
    文件类
    """

    def list(self, request):
        params = request.data
        if 'ids' not in params:
            return Response(return_format(20002, ''))
        ids = params['ids']
        service = FileService()
        res = service.list(ids)
        if res:
            return Response(return_format(200, data=res))
        else:
            return Response(return_format(service.errors['code'], msg=service.errors['msg']))

    def create(self, request):
        if 'file' not in request.FILES:
            return Response(return_format(20002))
        file = request.FILES['file']
        service = FileService()
        res = service.upload(file)
        if res:
            return Response(return_format(200, '', data=res))
        else:
            return Response(return_format(200, '', data=service.errors))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
