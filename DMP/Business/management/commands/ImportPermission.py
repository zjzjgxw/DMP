from django.core.management.base import BaseCommand, CommandError
from DMP.Business.Models.Permission import Permission
import json
from django.conf import settings


class Command(BaseCommand):
    help = "导入权限元数据"

    def add_arguments(self, parser):
        parser.add_argument('business_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        business_id = options["business_ids"]
        with open(settings.BASE_DIR + "/DMP/Business/Meta/Permissions.json", "r") as f:
            groups = json.load(f)
            print(groups)
        for item in groups:
            obj = Permission(id=item["id"], name=item["name"], permission_desc=item["permission_desc"],
                             group_id=item["business_permission_group_id"])
            obj.save()
