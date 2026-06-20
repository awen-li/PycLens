# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_compress_infile_outfile_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    local_testgzip = os.path.join(TEMPDIR, 'testgzip')
    gzipname = local_testgzip + '.gz'
    self.assertFalse(os.path.exists(gzipname))
    with open(local_testgzip, 'wb') as fp:
        fp.write(self.data)
    (rc, out, err) = assert_python_ok('-m', 'gzip', local_testgzip)
    self.assertTrue(os.path.exists(gzipname))
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')
