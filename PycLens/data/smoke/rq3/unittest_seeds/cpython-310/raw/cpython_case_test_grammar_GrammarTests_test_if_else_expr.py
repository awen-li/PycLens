# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_if_else_expr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _checkeval(msg, ret):
        """helper to check that evaluation of expressions is done correctly"""
        print(msg)
        return ret
    self.assertEqual([x() for x in (lambda : True, lambda : False) if x()], [True])
    self.assertEqual([x(False) for x in (lambda x: False if x else True, lambda x: True if x else False) if x(False)], [True])
    self.assertEqual(5 if 1 else _checkeval('check 1', 0), 5)
    self.assertEqual(_checkeval('check 2', 0) if 0 else 5, 5)
    self.assertEqual(5 and 6 if 0 else 1, 1)
    self.assertEqual(5 and 6 if 0 else 1, 1)
    self.assertEqual(5 and (6 if 1 else 1), 6)
    self.assertEqual(0 or _checkeval('check 3', 2) if 0 else 3, 3)
    self.assertEqual(1 or _checkeval('check 4', 2) if 1 else _checkeval('check 5', 3), 1)
    self.assertEqual(0 or 5 if 1 else _checkeval('check 6', 3), 5)
    self.assertEqual(not 5 if 1 else 1, False)
    self.assertEqual(not 5 if 0 else 1, 1)
    self.assertEqual(6 + 1 if 1 else 2, 7)
    self.assertEqual(6 - 1 if 1 else 2, 5)
    self.assertEqual(6 * 2 if 1 else 4, 12)
    self.assertEqual(6 / 2 if 1 else 3, 3)
    self.assertEqual(6 < 4 if 0 else 2, 2)
