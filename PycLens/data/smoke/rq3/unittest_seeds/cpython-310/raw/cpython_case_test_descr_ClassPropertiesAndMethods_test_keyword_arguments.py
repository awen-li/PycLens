# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_keyword_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a):
        return a
    self.assertEqual(f.__call__(a=42), 42)
    ba = bytearray()
    bytearray.__init__(ba, 'abc½€', encoding='latin1', errors='replace')
    self.assertEqual(ba, b'abc\xbd?')
