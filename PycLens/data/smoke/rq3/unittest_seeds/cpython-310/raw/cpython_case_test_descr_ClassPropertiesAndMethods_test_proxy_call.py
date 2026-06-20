# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_proxy_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class FakeStr:
        __class__ = str
    fake_str = FakeStr()
    self.assertIsInstance(fake_str, str)
    with self.assertRaises(TypeError):
        str.split(fake_str)
    with self.assertRaises(TypeError):
        str.__add__(fake_str, 'abc')
