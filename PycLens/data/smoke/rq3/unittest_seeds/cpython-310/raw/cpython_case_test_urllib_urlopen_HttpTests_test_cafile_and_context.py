# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_cafile_and_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = ssl.create_default_context()
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        with self.assertRaises(ValueError):
            urllib.request.urlopen('https://localhost', cafile='/nonexistent/path', context=context)
