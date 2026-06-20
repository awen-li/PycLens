# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: InstructionTests_test_default_first_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual = dis.get_instructions(simple)
    self.assertEqual(list(actual), expected_opinfo_simple)
