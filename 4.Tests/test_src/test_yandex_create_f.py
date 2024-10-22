# from unittest import TestCase
# import unittest
import pytest
from src.script_2 import create_folder, get_folder_info, get_yandex_token


token_ = get_yandex_token()
# print(token_)


class Test_Create_Folder_Pytest:

    @pytest.mark.parametrize("code, folder_name, token", [
        (201, 'test_dir', token_), (400, 'test_dir', token_), (401, 'test_dir', token_),
        (403, 'test_dir', token_), (404, 'test_dir', token_), (406, 'test_dir', token_),
        (409, 'test_dir', token_), (413, 'test_dir', token_), (423, 'test_dir', token_),
        (429, 'test_dir', token_), (503, 'test_dir', token_), (507, 'test_dir', token_),
        (200, 'test_dir', token_)
    ])
    def test_status_code_create_folder_pytest(self, code, folder_name, token):
        result = create_folder(folder_name, token).status_code
        assert code == result

    @pytest.mark.parametrize("code, folder_name, token", [
        (201, 'test_dir', token_), (400, 'test_dir', token_), (401, 'test_dir', token_),
        (403, 'test_dir', token_), (404, 'test_dir', token_), (406, 'test_dir', token_),
        (409, 'test_dir', token_), (413, 'test_dir', token_), (423, 'test_dir', token_),
        (429, 'test_dir', token_), (503, 'test_dir', token_), (507, 'test_dir', token_),
        (200, 'test_dir', token_)
    ])
    def test_status_code_info_pytest(self, code, folder_name, token):
        result = get_folder_info(folder_name, token).status_code
        assert code == result


# class Test_Create_Folder_Unittest(TestCase):
#
#     @pytest.mark.parametrize("code, folder_name, token", [
#         (201, 'test_dir', token_), (400, 'test_dir', token_), (401, 'test_dir', token_),
#         (403, 'test_dir', token_), (404, 'test_dir', token_), (406, 'test_dir', token_),
#         (409, 'test_dir', token_), (413, 'test_dir', token_), (423, 'test_dir', token_),
#         (429, 'test_dir', token_), (503, 'test_dir', token_), (507, 'test_dir', token_),
#         (200, 'test_dir', token_)
#     ])
#     def test_status_code_create_folder_unittest(self, code, folder_name, token):
#         result = create_folder(folder_name, token).status_code
#         self.assertEqual(code, result)
#
#     @pytest.mark.parametrize("code, folder_name, token", [
#         (201, 'test_dir', token_), (400, 'test_dir', token_), (401, 'test_dir', token_),
#         (403, 'test_dir', token_), (404, 'test_dir', token_), (406, 'test_dir', token_),
#         (409, 'test_dir', token_), (413, 'test_dir', token_), (423, 'test_dir', token_),
#         (429, 'test_dir', token_), (503, 'test_dir', token_), (507, 'test_dir', token_),
#         (200, 'test_dir', token_)
#     ])
#     def test_status_code_info_unittest(self, code, folder_name, token):
#         result = get_folder_info(folder_name, token).status_code
#         self.assertEqual(code, result)
#
#
# if __name__ == '__main__':
#     unittest.main()