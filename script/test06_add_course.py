from api.course import CourseAPI


class TestCourseAPI:
    def setup(self):
        self.course_api = CourseAPI()

    def teardown(self):
        pass

    # 课程添加成功
    def test01_add_success(self, token):
        add_data = {
            "name": "测试开发提升课001",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
        }
        response = self.course_api.add_course(test_data=add_data, token=token)
        print(response.json())
        assert 200 == response.status_code
        assert "成功" in response.text
        assert 200 == response.json().get("code")

    # 课程添加失败（未登录）
    def test02_add_fail(self):
        add_data = {
            "name": "测试开发提升课002",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
        }
        response = self.course_api.add_course(test_data=add_data, token="xxx")
        print(response.json())
        assert 200 == response.status_code
        assert "认证失败" in response.text
        assert 401 == response.json().get("code")

