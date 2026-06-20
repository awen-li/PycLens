# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicLinearFormatTest_test_multiline_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test('\n          abc\n          {name}\n          def\n          ', '\n          abc\n          bingle\n          bungle\n\n          def\n          ', name='bingle\nbungle\n')
