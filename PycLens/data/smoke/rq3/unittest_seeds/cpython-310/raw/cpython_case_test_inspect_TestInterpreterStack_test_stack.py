# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestInterpreterStack_test_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(len(mod.st) >= 5)
    self.assertEqual(revise(*mod.st[0][1:]), (modfile, 16, 'eggs', ['    st = inspect.stack()\n'], 0))
    self.assertEqual(revise(*mod.st[1][1:]), (modfile, 9, 'spam', ['    eggs(b + d, c + f)\n'], 0))
    self.assertEqual(revise(*mod.st[2][1:]), (modfile, 43, 'argue', ['            spam(a, b, c)\n'], 0))
    self.assertEqual(revise(*mod.st[3][1:]), (modfile, 39, 'abuse', ['        self.argue(a, b, c)\n'], 0))
    record = mod.st[0]
    self.assertIs(record.frame, mod.fr)
    self.assertEqual(record.lineno, 16)
    self.assertEqual(record.filename, mod.__file__)
    self.assertEqual(record.function, 'eggs')
    self.assertIn('inspect.stack()', record.code_context[0])
    self.assertEqual(record.index, 0)
