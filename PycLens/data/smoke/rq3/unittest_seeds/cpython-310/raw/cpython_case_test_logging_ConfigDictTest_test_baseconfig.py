# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_baseconfig

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'atuple': (1, 2, 3), 'alist': ['a', 'b', 'c'], 'adict': {'d': 'e', 'f': 3}, 'nest1': ('g', ('h', 'i'), 'j'), 'nest2': ['k', ['l', 'm'], 'n'], 'nest3': ['o', 'cfg://alist', 'p']}
    bc = logging.config.BaseConfigurator(d)
    self.assertEqual(bc.convert('cfg://atuple[1]'), 2)
    self.assertEqual(bc.convert('cfg://alist[1]'), 'b')
    self.assertEqual(bc.convert('cfg://nest1[1][0]'), 'h')
    self.assertEqual(bc.convert('cfg://nest2[1][1]'), 'm')
    self.assertEqual(bc.convert('cfg://adict.d'), 'e')
    self.assertEqual(bc.convert('cfg://adict[f]'), 3)
    v = bc.convert('cfg://nest3')
    self.assertEqual(v.pop(1), ['a', 'b', 'c'])
    self.assertRaises(KeyError, bc.convert, 'cfg://nosuch')
    self.assertRaises(ValueError, bc.convert, 'cfg://!')
    self.assertRaises(KeyError, bc.convert, 'cfg://adict[2]')
