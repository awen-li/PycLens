# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_195

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {'bandwidth': 0, 'latency': 1, 'key': 'value'}
    match x:
        case {'bandwidth': b, 'latency': l, **rest}:
            y = 0
    self.assertEqual(x, {'bandwidth': 0, 'latency': 1, 'key': 'value'})
    self.assertIs(b, x['bandwidth'])
    self.assertIs(l, x['latency'])
    self.assertEqual(rest, {'key': 'value'})
    self.assertEqual(y, 0)
