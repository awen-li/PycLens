# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_read_after_write_unicode_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        zipfp.writestr('приклад', b'sample')
        self.assertEqual(zipfp.read('приклад'), b'sample')
