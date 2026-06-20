# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_tzset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from os import environ
    xmas2002 = 1040774400.0
    eastern = 'EST+05EDT,M4.1.0,M10.5.0'
    victoria = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
    utc = 'UTC+0'
    org_TZ = environ.get('TZ', None)
    try:
        environ['TZ'] = eastern
        time.tzset()
        environ['TZ'] = utc
        time.tzset()
        self.assertEqual(time.gmtime(xmas2002), time.localtime(xmas2002))
        self.assertEqual(time.daylight, 0)
        self.assertEqual(time.timezone, 0)
        self.assertEqual(time.localtime(xmas2002).tm_isdst, 0)
        environ['TZ'] = eastern
        time.tzset()
        self.assertNotEqual(time.gmtime(xmas2002), time.localtime(xmas2002))
        self.assertEqual(time.tzname, ('EST', 'EDT'))
        self.assertEqual(len(time.tzname), 2)
        self.assertEqual(time.daylight, 1)
        self.assertEqual(time.timezone, 18000)
        self.assertEqual(time.altzone, 14400)
        self.assertEqual(time.localtime(xmas2002).tm_isdst, 0)
        self.assertEqual(len(time.tzname), 2)
        environ['TZ'] = victoria
        time.tzset()
        self.assertNotEqual(time.gmtime(xmas2002), time.localtime(xmas2002))
        self.assertIn(time.tzname[0], 'AESTEST', time.tzname[0])
        self.assertTrue(time.tzname[1] in ('AEDT', 'EDT'), str(time.tzname[1]))
        self.assertEqual(len(time.tzname), 2)
        self.assertEqual(time.daylight, 1)
        self.assertEqual(time.timezone, -36000)
        self.assertEqual(time.altzone, -39600)
        self.assertEqual(time.localtime(xmas2002).tm_isdst, 1)
    finally:
        if org_TZ is not None:
            environ['TZ'] = org_TZ
        elif 'TZ' in environ:
            del environ['TZ']
        time.tzset()
