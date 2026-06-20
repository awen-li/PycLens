# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: HexFloatTestCase_test_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value_pairs = [('inf', INF), ('-Infinity', -INF), ('nan', NAN), ('1.0', 1.0), ('-0x.2', -0.125), ('-0.0', -0.0)]
    whitespace = ['', ' ', '\t', '\n', '\n \t', '\x0c', '\x0b', '\r']
    for (inp, expected) in value_pairs:
        for lead in whitespace:
            for trail in whitespace:
                got = fromHex(lead + inp + trail)
                self.identical(got, expected)
