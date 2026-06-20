# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_general_eval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M:
        """Test mapping interface versus possible calls from eval()."""

        def __getitem__(self, key):
            if key == 'a':
                return 12
            raise KeyError

        def keys(self):
            return list('xyz')
    m = M()
    g = globals()
    self.assertEqual(eval('a', g, m), 12)
    self.assertRaises(NameError, eval, 'b', g, m)
    self.assertEqual(eval('dir()', g, m), list('xyz'))
    self.assertEqual(eval('globals()', g, m), g)
    self.assertEqual(eval('locals()', g, m), m)
    self.assertRaises(TypeError, eval, 'a', m)

    class A:
        """Non-mapping"""
        pass
    m = A()
    self.assertRaises(TypeError, eval, 'a', g, m)

    class D(dict):

        def __getitem__(self, key):
            if key == 'a':
                return 12
            return dict.__getitem__(self, key)

        def keys(self):
            return list('xyz')
    d = D()
    self.assertEqual(eval('a', g, d), 12)
    self.assertRaises(NameError, eval, 'b', g, d)
    self.assertEqual(eval('dir()', g, d), list('xyz'))
    self.assertEqual(eval('globals()', g, d), g)
    self.assertEqual(eval('locals()', g, d), d)
    eval('[locals() for i in (2,3)]', g, d)
    eval('[locals() for i in (2,3)]', g, collections.UserDict())

    class SpreadSheet:
        """Sample application showing nested, calculated lookups."""
        _cells = {}

        def __setitem__(self, key, formula):
            self._cells[key] = formula

        def __getitem__(self, key):
            return eval(self._cells[key], globals(), self)
    ss = SpreadSheet()
    ss['a1'] = '5'
    ss['a2'] = 'a1*6'
    ss['a3'] = 'a2*7'
    self.assertEqual(ss['a3'], 210)

    class C:

        def __getitem__(self, item):
            raise KeyError(item)

        def keys(self):
            return 1
    self.assertRaises(TypeError, eval, 'dir()', globals(), C())
