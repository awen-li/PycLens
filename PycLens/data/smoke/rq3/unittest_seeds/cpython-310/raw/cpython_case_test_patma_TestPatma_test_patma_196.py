# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_196

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {'bandwidth': 0, 'latency': 1}
    match x:
        case {'latency': l, 'bandwidth': b, **rest}:
            y = 0
    self.assertEqual(x, {'bandwidth': 0, 'latency': 1})
    self.assertIs(l, x['latency'])
    self.assertIs(b, x['bandwidth'])
    self.assertEqual(rest, {})
    self.assertEqual(y, 0)
