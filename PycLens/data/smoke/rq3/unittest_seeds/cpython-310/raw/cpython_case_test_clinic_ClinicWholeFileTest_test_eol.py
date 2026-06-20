# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicWholeFileTest_test_eol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = clinic.Clinic(clinic.CLanguage(None), filename='file')
    raw = '/*[clinic]\nfoo\n[clinic]*/'
    cooked = c.parse(raw).splitlines()
    end_line = cooked[2].rstrip()
    self.assertNotEqual(end_line, '[clinic]*/[clinic]*/')
    self.assertEqual(end_line, '[clinic]*/')
