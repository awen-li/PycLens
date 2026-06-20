# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_writestr_compresslevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipfp = zipfile.ZipFile(TESTFN2, 'w', compresslevel=1)
    zipfp.writestr('a.txt', 'hello world', compress_type=self.compression)
    zipfp.writestr('b.txt', 'hello world', compress_type=self.compression, compresslevel=2)
    a_info = zipfp.getinfo('a.txt')
    self.assertEqual(a_info.compress_type, self.compression)
    self.assertEqual(a_info._compresslevel, 1)
    b_info = zipfp.getinfo('b.txt')
    self.assertEqual(b_info.compress_type, self.compression)
    self.assertEqual(b_info._compresslevel, 2)
