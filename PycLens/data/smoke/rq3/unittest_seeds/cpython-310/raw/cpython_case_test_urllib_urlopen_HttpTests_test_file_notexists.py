# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_file_notexists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (fd, tmp_file) = tempfile.mkstemp()
    tmp_fileurl = 'file://localhost/' + tmp_file.replace(os.path.sep, '/')
    try:
        self.assertTrue(os.path.exists(tmp_file))
        with urlopen(tmp_fileurl) as fobj:
            self.assertTrue(fobj)
    finally:
        os.close(fd)
        os.unlink(tmp_file)
    self.assertFalse(os.path.exists(tmp_file))
    with self.assertRaises(urllib.error.URLError):
        urlopen(tmp_fileurl)
