# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___code__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (num_one, num_two) = (7, 8)

    def a():
        pass

    def b():
        return 12

    def c():
        return num_one

    def d():
        return num_two

    def e():
        return (num_one, num_two)
    for func in [a, b, c, d, e]:
        self.assertEqual(type(func.__code__), types.CodeType)
    self.assertEqual(c(), 7)
    self.assertEqual(d(), 8)
    d.__code__ = c.__code__
    self.assertEqual(c.__code__, d.__code__)
    self.assertEqual(c(), 7)
    try:
        b.__code__ = c.__code__
    except ValueError:
        pass
    else:
        self.fail('__code__ with different numbers of free vars should not be possible')
    try:
        e.__code__ = d.__code__
    except ValueError:
        pass
    else:
        self.fail('__code__ with different numbers of free vars should not be possible')
