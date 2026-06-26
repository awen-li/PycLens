# Source Generated with Decompyle++
# File: cpython-39-455cead0d77b.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import binascii
    
    class MyBytes(bytes):
'MyBytes'
    base = b'abc'
    m = MyBytes(base)
    self.assertEqual(binascii.b2a_hex(m), binascii.b2a_hex(base))
    
    class MyInt(int):
        iNualname__ = '__pybcsec_seed__.<locals>.MyInt'

    m = MyInt(42)
    
    try:
        binascii.b2a_hex(m)
        self.fail('subclass of int should not have a buffer interface')
    finally:
        pass


if __name__ == '__main__':
    __pybcsec_seed__()
