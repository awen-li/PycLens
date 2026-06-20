# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_buffer_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import binascii

    class MyBytes(bytes):
        pass
    base = b'abc'
    m = MyBytes(base)
    self.assertEqual(binascii.b2a_hex(m), binascii.b2a_hex(base))

    class MyInt(int):
        pass
    m = MyInt(42)
    try:
        binascii.b2a_hex(m)
        self.fail('subclass of int should not have a buffer interface')
    except TypeError:
        pass
