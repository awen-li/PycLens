# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: InstructionTests_test_jumpy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actual = dis.get_instructions(jumpy, first_line=expected_jumpy_line)
    self.assertEqual(list(actual), expected_opinfo_jumpy)
