# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.AllowPickle():
        f = self.partial(signature, ['asdf'], bar=[True])
        f.attr = []
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            f_copy = pickle.loads(pickle.dumps(f, proto))
            self.assertEqual(signature(f_copy), signature(f))
