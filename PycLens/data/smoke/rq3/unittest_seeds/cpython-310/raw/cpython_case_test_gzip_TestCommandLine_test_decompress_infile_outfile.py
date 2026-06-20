# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_decompress_infile_outfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gzipname = os.path.join(TEMPDIR, 'testgzip.gz')
    self.assertFalse(os.path.exists(gzipname))
    with gzip.open(gzipname, mode='wb') as fp:
        fp.write(self.data)
    (rc, out, err) = assert_python_ok('-m', 'gzip', '-d', gzipname)
    with open(os.path.join(TEMPDIR, 'testgzip'), 'rb') as gunziped:
        self.assertEqual(gunziped.read(), self.data)
    self.assertTrue(os.path.exists(gzipname))
    self.assertEqual(rc, 0)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')
