# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: SubclassTest_test_fromhex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test.fromhex('1a2B30')
    self.assertEqual(b, b'\x1a+0')
    self.assertIs(type(b), self.type2test)

    class B1(self.basetype):

        def __new__(cls, value):
            me = self.basetype.__new__(cls, value)
            me.foo = 'bar'
            return me
    b = B1.fromhex('1a2B30')
    self.assertEqual(b, b'\x1a+0')
    self.assertIs(type(b), B1)
    self.assertEqual(b.foo, 'bar')

    class B2(self.basetype):

        def __init__(me, *args, **kwargs):
            if self.basetype is not bytes:
                self.basetype.__init__(me, *args, **kwargs)
            me.foo = 'bar'
    b = B2.fromhex('1a2B30')
    self.assertEqual(b, b'\x1a+0')
    self.assertIs(type(b), B2)
    self.assertEqual(b.foo, 'bar')
