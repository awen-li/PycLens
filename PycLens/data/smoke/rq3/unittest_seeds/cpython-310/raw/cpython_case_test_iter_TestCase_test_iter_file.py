# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        for i in range(5):
            f.write('%d\n' % i)
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        self.check_for_loop(f, ['0\n', '1\n', '2\n', '3\n', '4\n'], pickle=False)
        self.check_for_loop(f, [], pickle=False)
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
