from DMP.Core.Exceptions import ValidationException


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
