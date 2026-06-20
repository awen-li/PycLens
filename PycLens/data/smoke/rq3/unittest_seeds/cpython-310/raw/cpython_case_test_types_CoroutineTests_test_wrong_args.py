# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_wrong_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samples = [None, 1, object()]
    for sample in samples:
        with self.assertRaisesRegex(TypeError, 'types.coroutine.*expects a callable'):
            types.coroutine(sample)
