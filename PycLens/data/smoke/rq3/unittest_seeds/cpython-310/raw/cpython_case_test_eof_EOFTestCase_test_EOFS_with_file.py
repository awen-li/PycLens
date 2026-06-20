# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_EOFS_with_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = '(<string>, line 1)'
    with os_helper.temp_dir() as temp_dir:
        file_name = script_helper.make_script(temp_dir, 'foo', "'''this is \na \ntest")
        (rc, out, err) = script_helper.assert_python_failure(file_name)
    self.assertIn(b'unterminated triple-quoted string literal (detected at line 3)', err)
