# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'#': 'hash'}
    self.assertEqual(f"{'#'}", '#')
    self.assertEqual(f"{d['#']}", 'hash')
    self.assertAllRaise(SyntaxError, "f-string expression part cannot include '#'", ["f'{1#}'", "f'{3(#)}'", "f'{#}'"])
    self.assertAllRaise(SyntaxError, "f-string: unmatched '\\)'", ["f'{)#}'"])
