# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestRoundtrip_test_indentation_semantics_retained

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if False:\n\tx=3\n\tx=3\n'
    codelines = self.roundtrip(code).split('\n')
    self.assertEqual(codelines[1], codelines[2])
    self.check_roundtrip(code)
