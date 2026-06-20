# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_unicode_join_endcase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class OhPhooey:

        def __init__(self, seq):
            self.it = iter(seq)
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            i = self.i
            self.i = i + 1
            if i == 2:
                return 'fooled you!'
            return next(self.it)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        f.write('a\n' + 'b\n' + 'c\n')
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        got = ' - '.join(OhPhooey(f))
        self.assertEqual(got, 'a\n - b\n - fooled you! - c\n')
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
