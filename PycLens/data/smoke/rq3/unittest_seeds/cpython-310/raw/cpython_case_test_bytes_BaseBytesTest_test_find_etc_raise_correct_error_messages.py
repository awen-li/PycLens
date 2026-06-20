# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_find_etc_raise_correct_error_messages

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    x = self.type2test(b'x')
    self.assertRaisesRegex(TypeError, '\\bfind\\b', b.find, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\brfind\\b', b.rfind, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\bindex\\b', b.index, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\brindex\\b', b.rindex, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\bcount\\b', b.count, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\bstartswith\\b', b.startswith, x, None, None, None)
    self.assertRaisesRegex(TypeError, '\\bendswith\\b', b.endswith, x, None, None, None)
