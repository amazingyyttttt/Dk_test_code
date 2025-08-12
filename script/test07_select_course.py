from api.course import CourseAPI


class TestCourseAPI:
    def setup(self):
        self.course_api = CourseAPI()

    # 查询存在的课程
    def test01_select_success(self, token):
        response = self.course_api.select_course(test_data="?name=测试开发提升课001", token=token)
        print(response.json())
        assert 200 == response.status_code
        assert "成功" in response.text
        assert 200 == response.json().get("code")

    # 查询失败（用户未登录）
    def test02_select_fail(self):
        response = self.course_api.select_course(test_data="?subject=6", token="xxx")
        print(response.json())
        assert 200 == response.status_code
        assert "认证失败" in response.text
        assert 401 == response.json().get("code")
