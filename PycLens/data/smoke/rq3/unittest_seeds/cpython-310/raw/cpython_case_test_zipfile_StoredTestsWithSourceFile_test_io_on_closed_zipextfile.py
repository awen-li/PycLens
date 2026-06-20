# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_io_on_closed_zipextfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = 'somefile.txt'
    with zipfile.ZipFile(TESTFN2, mode='w') as zipfp:
        zipfp.writestr(fname, 'bogus')
    with zipfile.ZipFile(TESTFN2, mode='r') as zipfp:
        with zipfp.open(fname) as fid:
            fid.close()
            self.assertRaises(ValueError, fid.read)
            self.assertRaises(ValueError, fid.seek, 0)
            self.assertRaises(ValueError, fid.tell)
            self.assertRaises(ValueError, fid.readable)
            self.assertRaises(ValueError, fid.seekable)
