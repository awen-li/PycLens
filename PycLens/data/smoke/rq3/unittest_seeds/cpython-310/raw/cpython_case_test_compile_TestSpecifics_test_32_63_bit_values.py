# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_32_63_bit_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = +4294967296
    b = -4294967296
    c = +281474976710656
    d = -281474976710656
    e = +4611686018427387904
    f = -4611686018427387904
    g = +9223372036854775807
    h = -9223372036854775807
    for variable in self.test_32_63_bit_values.__code__.co_consts:
        if variable is not None:
            self.assertIsInstance(variable, int)
