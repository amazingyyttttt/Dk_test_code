from api.course import CourseAPI


class TestCourseAPI:
    def setup(self):
        self.course_api = CourseAPI()

    # 课程删除成功
    def test01_delete_success(self, token):
        response = self.course_api.delete_course(course_id=110, token=token)
        print(response.json())
        assert 200 == response.status_code
        assert "成功" in response.text
        assert 200 == response.json().get("code")

    # 课程删除失败（课程id不存在）
    def test02_delete_fail_id_not_exist(self, token):
        response = self.course_api.delete_course(course_id=9999, token=token)
        print(response.json())
        assert 200 == response.status_code
        assert "失败" in response.text
        assert 500 == response.json().get("code")

    # 课程删除失败（用户未登录）
    def test03_delete_fail(self):
        response = self.course_api.delete_course(course_id=110, token="xxx")
        print(response.json())
        assert 200 == response.status_code
        assert "认证失败" in response.text
        assert 401 == response.json().get("code")
