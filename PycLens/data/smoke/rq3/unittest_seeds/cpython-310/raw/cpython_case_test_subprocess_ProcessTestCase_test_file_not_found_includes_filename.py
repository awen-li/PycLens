# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_file_not_found_includes_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(FileNotFoundError) as c:
        subprocess.call(['/opt/nonexistent_binary', 'with', 'some', 'args'])
    self.assertEqual(c.exception.filename, '/opt/nonexistent_binary')
