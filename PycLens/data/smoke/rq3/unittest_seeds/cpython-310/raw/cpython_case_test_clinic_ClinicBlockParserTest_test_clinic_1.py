# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicBlockParserTest_test_clinic_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_clinic('\n    verbatim text here\n    lah dee dah\n/*[copy input]\ndef\n[copy start generated code]*/\nabc\n/*[copy end generated code: output=03cfd743661f0797 input=7b18d017f89f61cf]*/\nxyz\n', '\n    verbatim text here\n    lah dee dah\n/*[copy input]\ndef\n[copy start generated code]*/\ndef\n/*[copy end generated code: output=7b18d017f89f61cf input=7b18d017f89f61cf]*/\nxyz\n')
