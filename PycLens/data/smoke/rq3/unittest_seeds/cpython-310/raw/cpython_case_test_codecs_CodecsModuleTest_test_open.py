# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    for mode in ('w', 'r', 'r+', 'w+', 'a', 'a+'):
        with self.subTest(mode), codecs.open(os_helper.TESTFN, mode, 'ascii') as file:
            self.assertIsInstance(file, codecs.StreamReaderWriter)
