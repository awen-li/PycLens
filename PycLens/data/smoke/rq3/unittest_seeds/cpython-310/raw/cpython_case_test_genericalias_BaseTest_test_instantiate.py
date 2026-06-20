# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_instantiate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in (tuple, list, dict, set, frozenset, defaultdict, deque):
        tname = t.__name__
        with self.subTest(f'Testing {tname}'):
            alias = t[int]
            self.assertEqual(alias(), t())
            if t is dict:
                self.assertEqual(alias(iter([('a', 1), ('b', 2)])), dict(a=1, b=2))
                self.assertEqual(alias(a=1, b=2), dict(a=1, b=2))
            elif t is defaultdict:

                def default():
                    return 'value'
                a = alias(default)
                d = defaultdict(default)
                self.assertEqual(a['test'], d['test'])
            else:
                self.assertEqual(alias(iter((1, 2, 3))), t((1, 2, 3)))
