# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URLopener_Tests_test_urlopener_retrieve_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as tmpdir:
        (fd, tmpfile) = tempfile.mkstemp(dir=tmpdir)
        os.close(fd)
        fileurl = 'file:' + urllib.request.pathname2url(tmpfile)
        (filename, _) = urllib.request.URLopener().retrieve(fileurl)
        self.assertEqual(os.path.normcase(filename), os.path.normcase(tmpfile))
