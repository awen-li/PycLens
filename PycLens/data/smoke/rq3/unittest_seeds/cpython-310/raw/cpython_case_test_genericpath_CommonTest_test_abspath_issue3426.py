# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_abspath_issue3426

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    abspath = self.pathmodule.abspath
    for path in ('', 'fuu', 'fùù', '/fuu', 'U:\\'):
        self.assertIsInstance(abspath(path), str)
    unicwd = 'çwð'
    try:
        os.fsencode(unicwd)
    except (AttributeError, UnicodeEncodeError):
        pass
    else:
        with os_helper.temp_cwd(unicwd):
            for path in ('', 'fuu', 'fùù', '/fuu', 'U:\\'):
                self.assertIsInstance(abspath(path), str)
