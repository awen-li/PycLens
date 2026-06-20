# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_eval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(eval('1+1'), 2)
    self.assertEqual(eval(' 1+1\n'), 2)
    globals = {'a': 1, 'b': 2}
    locals = {'b': 200, 'c': 300}
    self.assertEqual(eval('a', globals), 1)
    self.assertEqual(eval('a', globals, locals), 1)
    self.assertEqual(eval('b', globals, locals), 200)
    self.assertEqual(eval('c', globals, locals), 300)
    globals = {'a': 1, 'b': 2}
    locals = {'b': 200, 'c': 300}
    bom = b'\xef\xbb\xbf'
    self.assertEqual(eval(bom + b'a', globals, locals), 1)
    self.assertEqual(eval('"å"', globals), 'å')
    self.assertRaises(TypeError, eval)
    self.assertRaises(TypeError, eval, ())
    self.assertRaises(SyntaxError, eval, bom[:2] + b'a')

    class X:

        def __getitem__(self, key):
            raise ValueError
    self.assertRaises(ValueError, eval, 'foo', {}, X())
