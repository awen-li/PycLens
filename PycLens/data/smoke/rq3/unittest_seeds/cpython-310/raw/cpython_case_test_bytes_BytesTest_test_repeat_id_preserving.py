# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytesTest_test_repeat_id_preserving

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = b'123abc1@'
    b = b'456zyx-+'
    self.assertEqual(id(a), id(a))
    self.assertNotEqual(id(a), id(b))
    self.assertNotEqual(id(a), id(a * -4))
    self.assertNotEqual(id(a), id(a * 0))
    self.assertEqual(id(a), id(a * 1))
    self.assertEqual(id(a), id(1 * a))
    self.assertNotEqual(id(a), id(a * 2))

    class SubBytes(bytes):
        pass
    s = SubBytes(b'qwerty()')
    self.assertEqual(id(s), id(s))
    self.assertNotEqual(id(s), id(s * -4))
    self.assertNotEqual(id(s), id(s * 0))
    self.assertNotEqual(id(s), id(s * 1))
    self.assertNotEqual(id(s), id(1 * s))
    self.assertNotEqual(id(s), id(s * 2))
