# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestVariousIteratorArgs_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('123', '', range(1000), ('do', 1.2), range(2000, 2200, 5)):
        for g in (seq_tests.Sequence, seq_tests.IterFunc, seq_tests.IterGen, seq_tests.IterFuncStop, seq_tests.itermulti, seq_tests.iterfunc):
            self.assertEqual(list(deque(g(s))), list(g(s)))
        self.assertRaises(TypeError, deque, seq_tests.IterNextOnly(s))
        self.assertRaises(TypeError, deque, seq_tests.IterNoNext(s))
        self.assertRaises(ZeroDivisionError, deque, seq_tests.IterGenExc(s))
