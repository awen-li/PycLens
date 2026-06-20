# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_in_literal_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def containtest():
        return x in [a, b]
    self.assertEqual(count_instr_recursively(containtest, 'BUILD_LIST'), 0)
    self.check_lnotab(containtest)
