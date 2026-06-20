# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_issue3297

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = compile("a, b = '𐄏', '\\U0001010F'", 'dummy', 'exec')
    d = {}
    exec(c, d)
    self.assertEqual(d['a'], d['b'])
    self.assertEqual(len(d['a']), len(d['b']))
    self.assertEqual(ascii(d['a']), ascii(d['b']))
