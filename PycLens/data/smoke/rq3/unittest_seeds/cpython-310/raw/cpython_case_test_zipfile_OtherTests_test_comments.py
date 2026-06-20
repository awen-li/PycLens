# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        self.assertEqual(zipf.comment, b'')
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipfr:
        self.assertEqual(zipfr.comment, b'')
    comment = b'Bravely taking to his feet, he beat a very brave retreat.'
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.comment = comment
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipfr:
        self.assertEqual(zipf.comment, comment)
    comment2 = ''.join(['%d' % (i ** 3 % 10) for i in range((1 << 16) - 1)])
    comment2 = comment2.encode('ascii')
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.comment = comment2
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipfr:
        self.assertEqual(zipfr.comment, comment2)
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        with self.assertWarns(UserWarning):
            zipf.comment = comment2 + b'oops'
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipfr:
        self.assertEqual(zipfr.comment, comment2)
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.comment = b'original comment'
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='a') as zipf:
        zipf.comment = b'an updated comment'
    with zipfile.ZipFile(TESTFN, mode='r') as zipf:
        self.assertEqual(zipf.comment, b'an updated comment')
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.comment = b"original comment that's longer"
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    original_zip_size = os.path.getsize(TESTFN)
    with zipfile.ZipFile(TESTFN, mode='a') as zipf:
        zipf.comment = b'shorter comment'
    self.assertTrue(original_zip_size > os.path.getsize(TESTFN))
    with zipfile.ZipFile(TESTFN, mode='r') as zipf:
        self.assertEqual(zipf.comment, b'shorter comment')
