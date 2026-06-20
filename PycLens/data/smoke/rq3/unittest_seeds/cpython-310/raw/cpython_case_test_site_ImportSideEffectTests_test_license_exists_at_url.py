# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_license_exists_at_url

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = license._Printer__data.split()[1]
    req = urllib.request.Request(url, method='HEAD')
    self.addCleanup(urllib.request.urlcleanup)
    try:
        with socket_helper.transient_internet(url):
            with urllib.request.urlopen(req) as data:
                code = data.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    self.assertEqual(code, 200, msg="Can't find " + url)
