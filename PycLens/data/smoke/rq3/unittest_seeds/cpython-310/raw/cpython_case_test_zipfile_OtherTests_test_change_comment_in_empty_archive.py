# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_change_comment_in_empty_archive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, 'a', zipfile.ZIP_STORED) as zipf:
        self.assertFalse(zipf.filelist)
        zipf.comment = b'this is a comment'
    with zipfile.ZipFile(TESTFN, 'r') as zipf:
        self.assertEqual(zipf.comment, b'this is a comment')
