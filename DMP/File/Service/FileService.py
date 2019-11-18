from DMP.File.models import *


class FileService:
    """
    文件服务类
    """
    errors = None

    def __init__(self, store_type=1, module_name="common"):
        """
        :param store_type:
        :param module_name:
        """
        self.module_name = module_name
        self.store_type = store_type

    def upload(self, file):
        serializer = FilesSerializers(
            data={'name': file.name, 'type': self.store_type, 'path': file, 'module': self.module_name})
        if serializer.is_valid():
            f = serializer.create(serializer.validated_data)
            serializer = FilesSerializers(f)
            return serializer.data
        self.errors = serializer.errors
        return False

    def list(self, ids):
        """
        获取文件列表
        :param ids:
        :return:
        """
        if not isinstance(ids, list):
            self.errors = {"msg": "参数必须为数组", "code": 20002}
            return False
        if len(ids) == 0:
            self.errors = {"msg": "数组为空", "code": 20002}
            return False

        query_set = Files.objects.filter(id__in=ids)
        serializer = FilesSerializers(query_set, many=True)
        return serializer.data
