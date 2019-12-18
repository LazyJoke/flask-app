import glob
import os
import unittest

from app import ENV_CONF


# ------------------- 动态加载-测试用例 ----------------------
source = os.path.join(ENV_CONF.ROOT_DIR, 'api',  '**/test.py')
files = glob.glob(source, recursive=True)

for test_file_path in files:
    # 转换 文件路径 为 模块加载路径，如：/app/api/label/test.py => app.api.label.test
    file_path = test_file_path.replace(".py", '')
    file_path = file_path.replace("{}/".format(ENV_CONF.ROOT_DIR), '')
    module_path = '.'.join(file_path.split('/'))
    # 动态加载
    exec("from app.{} import *".format(module_path), globals())


if __name__ == '__main__':
    unittest.main()
