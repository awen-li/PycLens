# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestsWithMultipleOpens_test_many_opens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.make_test_archive(TESTFN2)
    with zipfile.ZipFile(TESTFN2, mode='r') as zipf:
        for x in range(100):
            zipf.read('ones')
            with zipf.open('ones') as zopen1:
                pass
    with open(os.devnull, 'rb') as f:
        self.assertLess(f.fileno(), 100)
