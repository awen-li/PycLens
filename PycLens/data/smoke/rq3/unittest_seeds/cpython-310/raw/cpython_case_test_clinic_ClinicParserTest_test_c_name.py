# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_c_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('module os\nos.stat as os_stat_fn')
    self.assertEqual('os_stat_fn', function.c_basename)
