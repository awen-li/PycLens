# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = datetime.datetime.now()
    dtime = xmlrpclib.DateTime(now.timetuple())
    self.assertTrue(dtime == now)
    self.assertTrue(now == dtime)
    then = now + datetime.timedelta(seconds=4)
    self.assertTrue(then >= dtime)
    self.assertTrue(dtime < then)
    dstr = now.strftime('%Y%m%dT%H:%M:%S')
    self.assertTrue(dtime == dstr)
    self.assertTrue(dstr == dtime)
    dtime_then = xmlrpclib.DateTime(then.timetuple())
    self.assertTrue(dtime_then >= dstr)
    self.assertTrue(dstr < dtime_then)
    dbytes = dstr.encode('ascii')
    dtuple = now.timetuple()
    self.assertFalse(dtime == 1970)
    self.assertTrue(dtime != dbytes)
    self.assertFalse(dtime == bytearray(dbytes))
    self.assertTrue(dtime != dtuple)
    with self.assertRaises(TypeError):
        dtime < float(1970)
    with self.assertRaises(TypeError):
        dtime > dbytes
    with self.assertRaises(TypeError):
        dtime <= bytearray(dbytes)
    with self.assertRaises(TypeError):
        dtime >= dtuple
    self.assertTrue(dtime == ALWAYS_EQ)
    self.assertFalse(dtime != ALWAYS_EQ)
    self.assertTrue(dtime < LARGEST)
    self.assertFalse(dtime > LARGEST)
    self.assertTrue(dtime <= LARGEST)
    self.assertFalse(dtime >= LARGEST)
    self.assertFalse(dtime < SMALLEST)
    self.assertTrue(dtime > SMALLEST)
    self.assertFalse(dtime <= SMALLEST)
    self.assertTrue(dtime >= SMALLEST)
