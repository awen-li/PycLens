# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytesTest_test_custom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __bytes__(self):
            return b'abc'
    self.assertEqual(bytes(A()), b'abc')

    class A:
        pass
    self.assertRaises(TypeError, bytes, A())

    class A:

        def __bytes__(self):
            return None
    self.assertRaises(TypeError, bytes, A())

    class A:

        def __bytes__(self):
            return b'a'

        def __index__(self):
            return 42
    self.assertEqual(bytes(A()), b'a')

    class A(str):

        def __bytes__(self):
            return b'abc'
    self.assertEqual(bytes(A('€')), b'abc')
    self.assertEqual(bytes(A('€'), 'iso8859-15'), b'\xa4')

    class A:

        def __bytes__(self):
            return OtherBytesSubclass(b'abc')
    self.assertEqual(bytes(A()), b'abc')
    self.assertIs(type(bytes(A())), OtherBytesSubclass)
    self.assertEqual(BytesSubclass(A()), b'abc')
    self.assertIs(type(BytesSubclass(A())), BytesSubclass)
