# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArraySubclassTest_test_init_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class subclass(bytearray):

        def __init__(me, newarg=1, *args, **kwargs):
            bytearray.__init__(me, *args, **kwargs)
    x = subclass(4, b'abcd')
    x = subclass(4, source=b'abcd')
    self.assertEqual(x, b'abcd')
    x = subclass(newarg=4, source=b'abcd')
    self.assertEqual(x, b'abcd')
