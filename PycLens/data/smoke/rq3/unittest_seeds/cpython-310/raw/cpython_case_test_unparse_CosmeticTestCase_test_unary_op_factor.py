# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_unary_op_factor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for prefix in ('+', '-', '~'):
        self.check_src_roundtrip(f'{prefix}1')
    for prefix in ('not',):
        self.check_src_roundtrip(f'{prefix} 1')
