# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: UntokenizeTest_test_bad_input_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Untokenizer()
    u.prev_row = 2
    u.prev_col = 2
    with self.assertRaises(ValueError) as cm:
        u.add_whitespace((1, 3))
    self.assertEqual(cm.exception.args[0], 'start (1,3) precedes previous end (2,2)')
    self.assertRaises(ValueError, u.add_whitespace, (2, 1))
