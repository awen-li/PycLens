# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, self.client.sendcmd, 'echo 40\r\n0')
    self.assertRaises(ValueError, self.client.sendcmd, 'echo 40\n0')
    self.assertRaises(ValueError, self.client.sendcmd, 'echo 40\r0')
    self.assertRaises(ftplib.error_temp, self.client.sendcmd, 'echo 400')
    self.assertRaises(ftplib.error_temp, self.client.sendcmd, 'echo 499')
    self.assertRaises(ftplib.error_perm, self.client.sendcmd, 'echo 500')
    self.assertRaises(ftplib.error_perm, self.client.sendcmd, 'echo 599')
    self.assertRaises(ftplib.error_proto, self.client.sendcmd, 'echo 999')
