# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_spwd.py
# case: TestSpwdRoot_test_getspnam

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = spwd.getspall()
    if not entries:
        self.skipTest('empty shadow password database')
    random_name = entries[0].sp_namp
    entry = spwd.getspnam(random_name)
    self.assertIsInstance(entry, spwd.struct_spwd)
    self.assertEqual(entry.sp_namp, random_name)
    self.assertEqual(entry.sp_namp, entry[0])
    self.assertEqual(entry.sp_namp, entry.sp_nam)
    self.assertIsInstance(entry.sp_pwdp, str)
    self.assertEqual(entry.sp_pwdp, entry[1])
    self.assertEqual(entry.sp_pwdp, entry.sp_pwd)
    self.assertIsInstance(entry.sp_lstchg, int)
    self.assertEqual(entry.sp_lstchg, entry[2])
    self.assertIsInstance(entry.sp_min, int)
    self.assertEqual(entry.sp_min, entry[3])
    self.assertIsInstance(entry.sp_max, int)
    self.assertEqual(entry.sp_max, entry[4])
    self.assertIsInstance(entry.sp_warn, int)
    self.assertEqual(entry.sp_warn, entry[5])
    self.assertIsInstance(entry.sp_inact, int)
    self.assertEqual(entry.sp_inact, entry[6])
    self.assertIsInstance(entry.sp_expire, int)
    self.assertEqual(entry.sp_expire, entry[7])
    self.assertIsInstance(entry.sp_flag, int)
    self.assertEqual(entry.sp_flag, entry[8])
    with self.assertRaises(KeyError) as cx:
        spwd.getspnam('invalid user name')
    self.assertEqual(str(cx.exception), "'getspnam(): name not found'")
    self.assertRaises(TypeError, spwd.getspnam)
    self.assertRaises(TypeError, spwd.getspnam, 0)
    self.assertRaises(TypeError, spwd.getspnam, random_name, 0)
    try:
        bytes_name = os.fsencode(random_name)
    except UnicodeEncodeError:
        pass
    else:
        self.assertRaises(TypeError, spwd.getspnam, bytes_name)
