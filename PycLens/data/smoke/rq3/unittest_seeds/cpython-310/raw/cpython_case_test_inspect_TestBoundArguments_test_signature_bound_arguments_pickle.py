# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBoundArguments_test_signature_bound_arguments_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a, b, *, c: 1={}, **kw) -> {42: 'ham'}:
        pass
    sig = inspect.signature(foo)
    ba = sig.bind(20, 30, z={})
    for ver in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(pickle_ver=ver):
            ba_pickled = pickle.loads(pickle.dumps(ba, ver))
            self.assertEqual(ba, ba_pickled)
