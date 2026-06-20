# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestInterpreterStack_test_trace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len(git.tr), 3)
    self.assertEqual(revise(*git.tr[0][1:]), (modfile, 43, 'argue', ['            spam(a, b, c)\n'], 0))
    self.assertEqual(revise(*git.tr[1][1:]), (modfile, 9, 'spam', ['    eggs(b + d, c + f)\n'], 0))
    self.assertEqual(revise(*git.tr[2][1:]), (modfile, 18, 'eggs', ['    q = y / 0\n'], 0))
