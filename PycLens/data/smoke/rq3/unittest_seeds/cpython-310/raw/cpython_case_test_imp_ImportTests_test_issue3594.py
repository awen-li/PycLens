# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue3594

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_mod_name = 'test_imp_helper'
    sys.path.insert(0, '.')
    try:
        with open(temp_mod_name + '.py', 'w', encoding='latin-1') as file:
            file.write("# coding: cp1252\nu = 'test.test_imp'\n")
        (file, filename, info) = imp.find_module(temp_mod_name)
        file.close()
        self.assertEqual(file.encoding, 'cp1252')
    finally:
        del sys.path[0]
        os_helper.unlink(temp_mod_name + '.py')
        os_helper.unlink(temp_mod_name + '.pyc')
