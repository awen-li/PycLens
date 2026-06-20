# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_peephole_opt_unreachable_code_array_access_in_bounds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def unused_code_at_end():
        return 3
        raise RuntimeError('unreachable')
    self.assertEqual('RETURN_VALUE', list(dis.get_instructions(unused_code_at_end))[-1].opname)
