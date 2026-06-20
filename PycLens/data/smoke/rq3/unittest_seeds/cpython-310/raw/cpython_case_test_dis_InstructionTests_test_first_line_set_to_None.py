# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: InstructionTests_test_first_line_set_to_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual = dis.get_instructions(simple, first_line=None)
    self.assertEqual(list(actual), expected_opinfo_simple)
