# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('hello', tuple('hello'), list('hello'), range(5)):
        self.assertEqual(operator.length_hint(reversed(s)), len(s))
        r = reversed(s)
        list(r)
        self.assertEqual(operator.length_hint(r), 0)

    class SeqWithWeirdLen:
        called = False

        def __len__(self):
            if not self.called:
                self.called = True
                return 10
            raise ZeroDivisionError

        def __getitem__(self, index):
            return index
    r = reversed(SeqWithWeirdLen())
    self.assertRaises(ZeroDivisionError, operator.length_hint, r)
