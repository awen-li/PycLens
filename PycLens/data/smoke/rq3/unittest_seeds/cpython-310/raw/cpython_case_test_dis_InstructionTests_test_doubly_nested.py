# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: InstructionTests_test_doubly_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with captured_stdout():
        inner = outer()()
    actual = dis.get_instructions(inner, first_line=expected_inner_line)
    self.assertEqual(list(actual), expected_opinfo_inner)
