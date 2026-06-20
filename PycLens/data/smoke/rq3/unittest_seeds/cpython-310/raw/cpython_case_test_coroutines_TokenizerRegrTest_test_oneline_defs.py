# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: TokenizerRegrTest_test_oneline_defs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = []
    for i in range(500):
        buf.append('def i{i}(): return {i}'.format(i=i))
    buf = '\n'.join(buf)
    ns = {}
    exec(buf, ns, ns)
    self.assertEqual(ns['i499'](), 499)
    buf += '\nasync def foo():\n    return'
    ns = {}
    exec(buf, ns, ns)
    self.assertEqual(ns['i499'](), 499)
    self.assertTrue(inspect.iscoroutinefunction(ns['foo']))
