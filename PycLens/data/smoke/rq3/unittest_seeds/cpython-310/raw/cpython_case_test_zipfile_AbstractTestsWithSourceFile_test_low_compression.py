# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractTestsWithSourceFile_test_low_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', self.compression) as zipfp:
        zipfp.writestr('strfile', '12')
    with zipfile.ZipFile(TESTFN2, 'r', self.compression) as zipfp:
        with zipfp.open('strfile') as openobj:
            self.assertEqual(openobj.read(1), b'1')
            self.assertEqual(openobj.read(1), b'2')
