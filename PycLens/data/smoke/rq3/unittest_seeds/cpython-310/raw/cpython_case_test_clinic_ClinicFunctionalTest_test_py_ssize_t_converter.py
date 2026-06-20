# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicFunctionalTest_test_py_ssize_t_converter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PY_SSIZE_T_MIN, PY_SSIZE_T_MAX
    with self.assertRaises(OverflowError):
        ac_tester.py_ssize_t_converter(PY_SSIZE_T_MIN - 1)
    with self.assertRaises(OverflowError):
        ac_tester.py_ssize_t_converter(PY_SSIZE_T_MAX + 1)
    with self.assertRaises(TypeError):
        ac_tester.py_ssize_t_converter([])
    self.assertEqual(ac_tester.py_ssize_t_converter(), (12, 34, 56))
    self.assertEqual(ac_tester.py_ssize_t_converter(1, 2, None), (1, 2, 56))
