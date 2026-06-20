# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2net.py
# case: OtherNetworkTests_test_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTFN = os_helper.TESTFN
    f = open(TESTFN, 'w')
    try:
        f.write('hi there\n')
        f.close()
        urls = ['file:' + sanepathname2url(os.path.abspath(TESTFN)), ('file:///nonsensename/etc/passwd', None, urllib.error.URLError)]
        self._test_urls(urls, self._extra_handlers(), retry=True)
    finally:
        os.remove(TESTFN)
    self.assertRaises(ValueError, urllib.request.urlopen, './relative_path/to/file')
