# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_exclusive_create_zip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unlink(TESTFN2)
    filename = 'testfile.txt'
    content = b'hello, world. this is some content.'
    with zipfile.ZipFile(TESTFN2, 'x', zipfile.ZIP_STORED) as zipfp:
        zipfp.writestr(filename, content)
    with self.assertRaises(FileExistsError):
        zipfile.ZipFile(TESTFN2, 'x', zipfile.ZIP_STORED)
    with zipfile.ZipFile(TESTFN2, 'r') as zipfp:
        self.assertEqual(zipfp.namelist(), [filename])
        self.assertEqual(zipfp.read(filename), content)
