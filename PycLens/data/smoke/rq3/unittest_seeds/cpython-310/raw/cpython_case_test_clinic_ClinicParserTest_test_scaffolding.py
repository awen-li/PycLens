# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_scaffolding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(clinic.unspecified), '<Unspecified>')
    self.assertEqual(repr(clinic.NULL), '<Null>')
    with support.captured_stdout() as stdout:
        with self.assertRaises(SystemExit):
            clinic.fail('The igloos are melting!', filename='clown.txt', line_number=69)
    self.assertEqual(stdout.getvalue(), 'Error in file "clown.txt" on line 69:\nThe igloos are melting!\n')
