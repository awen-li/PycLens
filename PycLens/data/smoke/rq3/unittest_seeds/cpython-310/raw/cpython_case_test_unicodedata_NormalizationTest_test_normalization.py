# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: NormalizationTest_test_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TESTDATAFILE = 'NormalizationTest.txt'
    TESTDATAURL = f'http://www.pythontest.net/unicode/{unicodedata.unidata_version}/{TESTDATAFILE}'
    try:
        testdata = open_urlresource(TESTDATAURL, encoding='utf-8', check=self.check_version)
    except PermissionError:
        self.skipTest(f'Permission error when downloading {TESTDATAURL} into the test data directory')
    except (OSError, HTTPException) as exc:
        self.skipTest(f'Failed to download {TESTDATAURL}: {exc}')
    with testdata:
        self.run_normalization_tests(testdata)
