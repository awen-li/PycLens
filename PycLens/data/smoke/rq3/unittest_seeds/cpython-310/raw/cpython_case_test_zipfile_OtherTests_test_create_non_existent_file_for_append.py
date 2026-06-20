# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_create_non_existent_file_for_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.path.exists(TESTFN):
        os.unlink(TESTFN)
    filename = 'testfile.txt'
    content = b'hello, world. this is some content.'
    try:
        with zipfile.ZipFile(TESTFN, 'a') as zf:
            zf.writestr(filename, content)
    except OSError:
        self.fail('Could not append data to a non-existent zip file.')
    self.assertTrue(os.path.exists(TESTFN))
    with zipfile.ZipFile(TESTFN, 'r') as zf:
        self.assertEqual(zf.read(filename), content)
