# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_per_file_compresslevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', compresslevel=1) as zipfp:
        zipfp.write(TESTFN, 'compress_1')
        zipfp.write(TESTFN, 'compress_9', compresslevel=9)
        one_info = zipfp.getinfo('compress_1')
        nine_info = zipfp.getinfo('compress_9')
        self.assertEqual(one_info._compresslevel, 1)
        self.assertEqual(nine_info._compresslevel, 9)
