# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_writestr_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipfp = zipfile.ZipFile(TESTFN2, 'w')
    zipfp.writestr('b.txt', 'hello world', compress_type=self.compression)
    info = zipfp.getinfo('b.txt')
    self.assertEqual(info.compress_type, self.compression)
