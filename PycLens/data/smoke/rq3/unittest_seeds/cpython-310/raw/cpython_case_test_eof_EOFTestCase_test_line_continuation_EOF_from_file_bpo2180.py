# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_line_continuation_EOF_from_file_bpo2180

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as temp_dir:
        file_name = script_helper.make_script(temp_dir, 'foo', '\\')
        (rc, out, err) = script_helper.assert_python_failure(file_name)
        self.assertIn(b'unexpected EOF while parsing', err)
        self.assertIn(b'line 1', err)
        self.assertIn(b'\\', err)
        file_name = script_helper.make_script(temp_dir, 'foo', 'y = 6\\')
        (rc, out, err) = script_helper.assert_python_failure(file_name)
        self.assertIn(b'unexpected EOF while parsing', err)
        self.assertIn(b'line 1', err)
        self.assertIn(b'y = 6\\', err)
