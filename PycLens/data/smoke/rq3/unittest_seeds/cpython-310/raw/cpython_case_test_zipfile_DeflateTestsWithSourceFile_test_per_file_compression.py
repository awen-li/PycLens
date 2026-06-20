# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: DeflateTestsWithSourceFile_test_per_file_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        zipfp.write(TESTFN, 'storeme', zipfile.ZIP_STORED)
        zipfp.write(TESTFN, 'deflateme', zipfile.ZIP_DEFLATED)
        sinfo = zipfp.getinfo('storeme')
        dinfo = zipfp.getinfo('deflateme')
        self.assertEqual(sinfo.compress_type, zipfile.ZIP_STORED)
        self.assertEqual(dinfo.compress_type, zipfile.ZIP_DEFLATED)
