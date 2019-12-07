from django.core.management.base import BaseCommand, CommandError
from DMP.Business.Models.PermissionGroup import PermissionGroup, PermissionGroupSerializer
import json
from django.conf import settings


class Command(BaseCommand):
    help = "导入权限元数据"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.BASE_DIR + "/DMP/Business/Meta/PermissionGroup.json", "r") as f:
            groups = json.load(f)
            print(groups)
        for item in groups:
            obj = PermissionGroup(id=item["id"], name=item["name"], permission_desc=item["permission_desc"])
            obj.save()
