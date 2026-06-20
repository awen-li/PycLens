# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_keyerror_without_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict()
    try:
        d1[1,]
    except KeyError as err:
        self.assertEqual(err.args[0], (1,))
    else:
        self.fail('expected KeyError')
