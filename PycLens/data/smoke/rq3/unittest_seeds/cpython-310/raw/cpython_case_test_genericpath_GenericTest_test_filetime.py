# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_filetime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    create_file(filename, b'foo')
    with open(filename, 'ab', 0) as f:
        f.write(b'bar')
    with open(filename, 'rb', 0) as f:
        data = f.read()
    self.assertEqual(data, b'foobar')
    self.assertLessEqual(self.pathmodule.getctime(filename), self.pathmodule.getmtime(filename))
