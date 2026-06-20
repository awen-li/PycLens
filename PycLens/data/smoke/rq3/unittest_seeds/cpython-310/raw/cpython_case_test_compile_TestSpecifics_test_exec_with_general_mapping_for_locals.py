# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_exec_with_general_mapping_for_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M:
        """Test mapping interface versus possible calls from eval()."""

        def __getitem__(self, key):
            if key == 'a':
                return 12
            raise KeyError

        def __setitem__(self, key, value):
            self.results = (key, value)

        def keys(self):
            return list('xyz')
    m = M()
    g = globals()
    exec('z = a', g, m)
    self.assertEqual(m.results, ('z', 12))
    try:
        exec('z = b', g, m)
    except NameError:
        pass
    else:
        self.fail('Did not detect a KeyError')
    exec('z = dir()', g, m)
    self.assertEqual(m.results, ('z', list('xyz')))
    exec('z = globals()', g, m)
    self.assertEqual(m.results, ('z', g))
    exec('z = locals()', g, m)
    self.assertEqual(m.results, ('z', m))
    self.assertRaises(TypeError, exec, 'z = b', m)

    class A:
        """Non-mapping"""
        pass
    m = A()
    self.assertRaises(TypeError, exec, 'z = a', g, m)

    class D(dict):

        def __getitem__(self, key):
            if key == 'a':
                return 12
            return dict.__getitem__(self, key)
    d = D()
    exec('z = a', g, d)
    self.assertEqual(d['z'], 12)
