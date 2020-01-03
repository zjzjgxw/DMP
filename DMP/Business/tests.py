from django.test import TestCase
from DMP.Business.Service.BusinessService import BusinessService
from DMP.Business.Models.BasicInfo import BasicInfo
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class BusinessServiceTest(APITestCase):
    multi_db = True

    def setUp(self):
        BasicInfo.objects.create(name="x", logo_img_id=1)

    def test_create_ss(self):
        data = {
            "name": "新信息",
            "logo_img_id": 1,
            "email": "244583485@qq.com",
        }
        business_id = BusinessService.create(**data)
        self.assertIsInstance(business_id, int)
