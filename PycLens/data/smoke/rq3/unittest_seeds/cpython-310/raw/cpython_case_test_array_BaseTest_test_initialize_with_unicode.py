# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_initialize_with_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.typecode != 'u':
        with self.assertRaises(TypeError) as cm:
            a = array.array(self.typecode, 'foo')
        self.assertIn('cannot use a str', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            a = array.array(self.typecode, array.array('u', 'foo'))
        self.assertIn('cannot use a unicode array', str(cm.exception))
    else:
        a = array.array(self.typecode, 'foo')
        a = array.array(self.typecode, array.array('u', 'foo'))
