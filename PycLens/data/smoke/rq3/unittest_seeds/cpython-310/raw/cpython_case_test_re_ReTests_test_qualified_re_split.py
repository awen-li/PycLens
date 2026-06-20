# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_qualified_re_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.split(':', ':a:b::c', 2), ['', 'a', 'b::c'])
    self.assertEqual(re.split(':', ':a:b::c', maxsplit=2), ['', 'a', 'b::c'])
    self.assertEqual(re.split(':', 'a:b:c:d', maxsplit=2), ['a', 'b', 'c:d'])
    self.assertEqual(re.split('(:)', ':a:b::c', maxsplit=2), ['', ':', 'a', ':', 'b::c'])
    self.assertEqual(re.split('(:+)', ':a:b::c', maxsplit=2), ['', ':', 'a', ':', 'b::c'])
    self.assertEqual(re.split('(:*)', ':a:b::c', maxsplit=2), ['', ':', '', '', 'a:b::c'])
