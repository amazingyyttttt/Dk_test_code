from api.course import CourseAPI


class TestCourseAPI:
    def setup(self):
        self.course_api = CourseAPI()

    # 课程修改成功
    def test01_update_success(self, token):
        update_data = {
            "id": 109,
            "name": "接口测试0001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍0001",
        }
        response = self.course_api.update_course(test_data=update_data, token=token)
        print(response.json())
        assert 200 == response.status_code
        assert "成功" in response.text
        assert 200 == response.json().get("code")

    # 课程修改失败（未登录）
    def test02_update_fail(self):
        update_data = {
            "id": 109,
            "name": "接口测试0001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍0001",
        }
        response = self.course_api.update_course(test_data=update_data, token="xxx")
        print(response.json())
        assert 200 == response.status_code
        assert "认证失败" in response.text
        assert 401 == response.json().get("code")
