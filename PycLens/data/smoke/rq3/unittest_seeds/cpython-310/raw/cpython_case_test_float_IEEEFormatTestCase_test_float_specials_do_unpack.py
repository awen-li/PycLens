# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: IEEEFormatTestCase_test_float_specials_do_unpack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (fmt, data) in [('>f', BE_FLOAT_INF), ('>f', BE_FLOAT_NAN), ('<f', LE_FLOAT_INF), ('<f', LE_FLOAT_NAN)]:
        struct.unpack(fmt, data)
