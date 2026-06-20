# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    one_hour = 60 * 60
    half_hour = 30 * 60
    half_minute = 30
    ((*_, offset), _, offset_fraction) = _strptime._strptime('+0130', '%z')
    self.assertEqual(offset, one_hour + half_hour)
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-0100', '%z')
    self.assertEqual(offset, -one_hour)
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-013030', '%z')
    self.assertEqual(offset, -(one_hour + half_hour + half_minute))
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-013030.000001', '%z')
    self.assertEqual(offset, -(one_hour + half_hour + half_minute))
    self.assertEqual(offset_fraction, -1)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('+01:00', '%z')
    self.assertEqual(offset, one_hour)
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-01:30', '%z')
    self.assertEqual(offset, -(one_hour + half_hour))
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-01:30:30', '%z')
    self.assertEqual(offset, -(one_hour + half_hour + half_minute))
    self.assertEqual(offset_fraction, 0)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('-01:30:30.000001', '%z')
    self.assertEqual(offset, -(one_hour + half_hour + half_minute))
    self.assertEqual(offset_fraction, -1)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('+01:30:30.001', '%z')
    self.assertEqual(offset, one_hour + half_hour + half_minute)
    self.assertEqual(offset_fraction, 1000)
    ((*_, offset), _, offset_fraction) = _strptime._strptime('Z', '%z')
    self.assertEqual(offset, 0)
    self.assertEqual(offset_fraction, 0)
