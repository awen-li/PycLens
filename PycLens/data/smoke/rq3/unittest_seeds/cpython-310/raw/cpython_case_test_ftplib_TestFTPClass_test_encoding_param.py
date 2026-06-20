# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_encoding_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ['latin-1', 'utf-8']
    for encoding in encodings:
        with self.subTest(encoding=encoding):
            self.tearDown()
            self.setUp(encoding=encoding)
            self.assertEqual(encoding, self.client.encoding)
            self.test_retrbinary()
            self.test_storbinary()
            self.test_retrlines()
            new_dir = self.client.mkd('/non-ascii dir ®')
            self.check_data(new_dir, '/non-ascii dir ®')
    client = ftplib.FTP(timeout=TIMEOUT)
    self.assertEqual(DEFAULT_ENCODING, client.encoding)
