# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_file_not_found_with_bad_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(FileNotFoundError) as c:
        subprocess.Popen(['exit', '0'], cwd='/some/nonexistent/directory')
    self.assertEqual(c.exception.filename, '/some/nonexistent/directory')
