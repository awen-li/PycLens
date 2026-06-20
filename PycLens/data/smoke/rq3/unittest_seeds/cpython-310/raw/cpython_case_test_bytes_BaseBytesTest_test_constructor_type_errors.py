# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_constructor_type_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.type2test, 0.0)

    class C:
        pass
    self.assertRaises(TypeError, self.type2test, ['0'])
    self.assertRaises(TypeError, self.type2test, [0.0])
    self.assertRaises(TypeError, self.type2test, [None])
    self.assertRaises(TypeError, self.type2test, [C()])
    self.assertRaises(TypeError, self.type2test, encoding='ascii')
    self.assertRaises(TypeError, self.type2test, errors='ignore')
    self.assertRaises(TypeError, self.type2test, 0, 'ascii')
    self.assertRaises(TypeError, self.type2test, b'', 'ascii')
    self.assertRaises(TypeError, self.type2test, 0, errors='ignore')
    self.assertRaises(TypeError, self.type2test, b'', errors='ignore')
    self.assertRaises(TypeError, self.type2test, '')
    self.assertRaises(TypeError, self.type2test, '', errors='ignore')
    self.assertRaises(TypeError, self.type2test, '', b'ascii')
    self.assertRaises(TypeError, self.type2test, '', 'ascii', b'ignore')
