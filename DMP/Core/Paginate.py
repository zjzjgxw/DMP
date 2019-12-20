from DMP.Core.Exceptions import ValidationException
from django.db import models


class PagePaginate:
    page = 1
    page_size = 10

    def __init__(self, request):
        if "page" in request.data:
            self.page = request.data["page"]
        if "page_size" in request.data:
            self.page_size = request.data["page_size"]
        if not isinstance(self.page, int):
            raise ValidationException(10009)
        if not isinstance(self.page_size, int):
            raise ValidationException(10009)
        if self.page < 1 or self.page_size <= 0:
            raise ValidationException(10010)


class PageManager(models.Manager):
    _count = -1

    def count(self, **kwargs):
        self._count = self.filter(**kwargs, delete_flag=0).count()
        return self._count

    def list(self, page=1, page_size=10, **kwargs):
        if page < 1:
            page = 1
        bottom = (page - 1) * page_size
        top = bottom + page_size
        if self._count == -1:
            self._count = self.count(**kwargs)
        if top > self._count:
            top = self._count
        return self.filter(**kwargs, delete_flag=0)[bottom: top]
