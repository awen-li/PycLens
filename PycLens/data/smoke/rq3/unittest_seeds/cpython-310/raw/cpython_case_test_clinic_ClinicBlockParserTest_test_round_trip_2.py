# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicBlockParserTest_test_round_trip_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.round_trip('\n    verbatim text here\n    lah dee dah\n/*[inert]\nabc\n[inert]*/\ndef\n/*[inert checksum: 7b18d017f89f61cf17d47f92749ea6930a3f1deb]*/\nxyz\n')
