# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_bad_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        _strptime._strptime('-01:30:30.', '%z')
    with self.assertRaises(ValueError):
        _strptime._strptime('-0130:30', '%z')
    with self.assertRaises(ValueError):
        _strptime._strptime('-01:30:30.1234567', '%z')
    with self.assertRaises(ValueError):
        _strptime._strptime('-01:30:30:123456', '%z')
    with self.assertRaises(ValueError) as err:
        _strptime._strptime('-01:3030', '%z')
    self.assertEqual('Inconsistent use of : in -01:3030', str(err.exception))
