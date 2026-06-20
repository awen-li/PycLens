# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestVersion_test_no_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser = InterceptingOptionParser(usage=SUPPRESS_USAGE)
    self.assertParseFail(['--version'], 'no such option: --version')
