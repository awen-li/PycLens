# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_large_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    create_file(os_helper.TESTFN, b'test')
    with open(os_helper.TESTFN, 'rb') as fp:
        data = os.read(fp.fileno(), size)
    self.assertEqual(data, b'test')
