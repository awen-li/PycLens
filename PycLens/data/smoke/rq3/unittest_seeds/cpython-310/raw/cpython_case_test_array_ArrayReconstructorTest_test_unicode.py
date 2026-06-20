# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: ArrayReconstructorTest_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    teststr = 'Bonne Journée 𠌊𠍇'
    testcases = ((UTF16_LE, 'UTF-16-LE'), (UTF16_BE, 'UTF-16-BE'), (UTF32_LE, 'UTF-32-LE'), (UTF32_BE, 'UTF-32-BE'))
    for testcase in testcases:
        (mformat_code, encoding) = testcase
        a = array.array('u', teststr)
        b = array_reconstructor(array.array, 'u', mformat_code, teststr.encode(encoding))
        self.assertEqual(a, b, msg='{0!r} != {1!r}; testcase={2!r}'.format(a, b, testcase))
