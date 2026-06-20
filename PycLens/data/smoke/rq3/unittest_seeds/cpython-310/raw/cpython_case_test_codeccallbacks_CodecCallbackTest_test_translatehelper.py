# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_translatehelper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D(dict):

        def __getitem__(self, key):
            raise ValueError
    self.assertRaises(ValueError, 'ÿ'.translate, {255: sys.maxunicode + 1})
    self.assertRaises(TypeError, 'ÿ'.translate, {255: ()})
