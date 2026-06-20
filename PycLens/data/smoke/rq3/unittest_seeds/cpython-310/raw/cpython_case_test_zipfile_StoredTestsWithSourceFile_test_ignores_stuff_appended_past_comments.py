# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_ignores_stuff_appended_past_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.comment = b'this is a comment'
        zipfp.write(TESTFN, TESTFN)
    with open(TESTFN2, 'a', encoding='utf-8') as f:
        f.write('abcdef\r\n')
    with zipfile.ZipFile(TESTFN2, 'r') as zipfp:
        self.assertIsInstance(zipfp, zipfile.ZipFile)
        self.assertEqual(zipfp.comment, b'this is a comment')
