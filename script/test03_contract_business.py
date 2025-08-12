import config
from api.course import CourseAPI
from api.contract import ContractAPI


class TestContractBusiness:
    def setup(self):
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

    # 1、课程新增成功
    def test01_add_course(self, token):
        add_data = {"name": "测试开发提升课01", "subject": "6", "price": 899, "applicablePerson": "2", "info": "测试开发提升课01"}
        response = self.course_api.add_course(test_data=add_data, token=token)
        print(response.json())

    # 2、上传合同成功
    def test02_upload_contract(self, token):
        f = open(config.BASE_PATH + "/data/test.pdf", "rb")
        response = self.contract_api.upload_contract(test_data=f, token=token)
        print(response.json())

    # 3、合同新增成功
    def test03_add_contract(self, token):
        add_data = {
            "name": "测试88",
            "phone": "13612345678",
            "contractNo": "HT20230007",
            "subject": "6",
            "courseId": " 99",
            "channel": "0",
            "activityId": 77,
            "fileName": "xxx",
        }
        response = self.contract_api.add_contract(test_data=add_data, token=token)
        print(response.json())





