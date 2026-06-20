# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestZeroCopySendfile_test_non_regular_file_dst

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'rb') as src:
        with io.BytesIO() as dst:
            with self.assertRaises(_GiveupOnFastCopy):
                self.zerocopy_fun(src, dst)
            shutil.copyfileobj(src, dst)
            dst.seek(0)
            self.assertEqual(dst.read(), self.FILEDATA)
