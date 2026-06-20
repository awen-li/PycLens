# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstempInner_test_collision_with_existing_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with _inside_empty_temp_dir(), _mock_candidate_names('aaa', 'aaa', 'bbb'):
        dir = tempfile.mkdtemp()
        self.assertTrue(dir.endswith('aaa'))
        (fd, name) = self.make_temp()
        os.close(fd)
        self.assertTrue(name.endswith('bbb'))
