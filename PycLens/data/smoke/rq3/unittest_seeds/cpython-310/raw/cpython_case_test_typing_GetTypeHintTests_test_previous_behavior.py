# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_previous_behavior

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def testf(x, y):
        ...
    testf.__annotations__['x'] = 'int'
    self.assertEqual(gth(testf), {'x': int})

    def testg(x: None):
        ...
    self.assertEqual(gth(testg), {'x': type(None)})
