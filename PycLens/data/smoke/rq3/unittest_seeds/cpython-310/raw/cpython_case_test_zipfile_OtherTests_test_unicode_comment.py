# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_unicode_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, 'w', zipfile.ZIP_STORED) as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
        with self.assertRaises(TypeError):
            zipf.comment = 'this is an error'
