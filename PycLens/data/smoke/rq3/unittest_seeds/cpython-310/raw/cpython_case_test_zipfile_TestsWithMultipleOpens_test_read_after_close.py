# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestsWithMultipleOpens_test_read_after_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in get_files(self):
        self.make_test_archive(f)
        with contextlib.ExitStack() as stack:
            with zipfile.ZipFile(f, 'r') as zipf:
                zopen1 = stack.enter_context(zipf.open('ones'))
                zopen2 = stack.enter_context(zipf.open('twos'))
            data1 = zopen1.read(500)
            data2 = zopen2.read(500)
            data1 += zopen1.read()
            data2 += zopen2.read()
        self.assertEqual(data1, self.data1)
        self.assertEqual(data2, self.data2)
