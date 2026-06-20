# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_match_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test:

        def __init__(self, test_id):
            self.test_id = test_id

        def id(self):
            return self.test_id
    test_access = Test('test.test_os.FileTests.test_access')
    test_chdir = Test('test.test_os.Win32ErrorTests.test_chdir')
    with support.swap_attr(support, '_match_test_func', None):
        support.set_match_tests([])
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(None, None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests([test_access.id()], None)
        self.assertTrue(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
        support.set_match_tests(['test_os'], None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(['test_*'], None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(['filetests'], None)
        self.assertFalse(support.match_test(test_access))
        support.set_match_tests(['FileTests'], None)
        self.assertTrue(support.match_test(test_access))
        support.set_match_tests(['*test_os.*.test_*'], None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests([test_access.id(), test_chdir.id()], None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(['test_access', 'DONTMATCH'], None)
        self.assertTrue(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
    with support.swap_attr(support, '_match_test_func', None):
        support.set_match_tests(ignore_patterns=[])
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(None, None)
        self.assertTrue(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(None, [test_access.id()])
        self.assertFalse(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
        support.set_match_tests(None, ['test_os'])
        self.assertFalse(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
        support.set_match_tests(None, ['test_*'])
        self.assertFalse(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
        support.set_match_tests(None, ['filetests'])
        self.assertTrue(support.match_test(test_access))
        support.set_match_tests(None, ['FileTests'])
        self.assertFalse(support.match_test(test_access))
        support.set_match_tests(None, ['*test_os.*.test_*'])
        self.assertFalse(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
        support.set_match_tests(None, [test_access.id(), test_chdir.id()])
        self.assertFalse(support.match_test(test_access))
        self.assertFalse(support.match_test(test_chdir))
        support.set_match_tests(None, ['test_access', 'DONTMATCH'])
        self.assertFalse(support.match_test(test_access))
        self.assertTrue(support.match_test(test_chdir))
