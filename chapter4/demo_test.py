import unittest

from chapter3.po_demo import Search
import paramunittest
import unittest


# @paramunittest.parametrized(
#     ('admin', 'Aa123456', 'admin', 'test_login_admin is ok'),
#     ('test1', 'Aa123456', 'test1', 'test_login_test1 is ok'),
#     ('test2', 'Aa123456', 'test2', 'test_login_test2 is ok')
# )
# class TestSearch(unittest.TestCase, Search):
#
#     def setParameters(self, user, pwd, ass, txt):
#         self.user = user
#         self.pwd = pwd
#         self.ass = ass
#         self.txt = txt
#
#     def test_login(self):
#         self.get()
#         self.login(self.user, self.pwd)
#         assert self.element(self.user_name).text == self.ass
#         print(self.txt)
#         self.logout()

    # def test_login_admin(self):
    #     self.get()
    #     self.login('admin', 'Aa123456')
    #     assert self.element(self.user_name).text == 'admin'
    #     print('test_login_admin is ok!')
    #     self.logout()
    #
    # def test_login_test1(self):
    #     self.get()
    #     self.login('test1', 'Aa123456')
    #     assert self.element(self.user_name).text == 'test1'
    #     print('test_login_test1 is ok!')
    #     self.logout()
    #
    # def test_login_test2(self):
    #     self.get()
    #     self.login('test2', 'Aa123456')
    #     assert self.element(self.user_name).text == 'test2'
    #     print('test_login_test2 is ok!')
    #     self.driver.quit()


data = (
    {"user": 'admin', 'pwd': 'Aa123456', 'ass': 'admin', 'txt': 'test_login_admin is ok!'},
    {"user": 'test1', 'pwd': 'Aa123456', 'ass': 'test1', 'txt': 'test_login_test1 is ok!'},
    {"user": 'test2', 'pwd': 'Aa123456', 'ass': 'test8', 'txt': 'test_login_test2 is ok!'}
)


class A(unittest.TestCase, Search):

    def test_login(self):
        for d in data:
            # 使用上下文管理器打开
            with self.subTest(d):
                self.get()
                self.login(d['user'], d['pwd'])
                assert self.element(self.user_name).text == d['ass'], \
                    self.driver.save_screenshot(f"./{d['ass']}.png")
                print(d['txt'])
                self.logout()


if __name__ == '__main__':
    unittest.main()
