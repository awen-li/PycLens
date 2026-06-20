# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_commonprefix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    commonprefix = self.pathmodule.commonprefix
    self.assertEqual(commonprefix([]), '')
    self.assertEqual(commonprefix(['/home/swenson/spam', '/home/swen/spam']), '/home/swen')
    self.assertEqual(commonprefix(['/home/swen/spam', '/home/swen/eggs']), '/home/swen/')
    self.assertEqual(commonprefix(['/home/swen/spam', '/home/swen/spam']), '/home/swen/spam')
    self.assertEqual(commonprefix(['home:swenson:spam', 'home:swen:spam']), 'home:swen')
    self.assertEqual(commonprefix([':home:swen:spam', ':home:swen:eggs']), ':home:swen:')
    self.assertEqual(commonprefix([':home:swen:spam', ':home:swen:spam']), ':home:swen:spam')
    self.assertEqual(commonprefix([b'/home/swenson/spam', b'/home/swen/spam']), b'/home/swen')
    self.assertEqual(commonprefix([b'/home/swen/spam', b'/home/swen/eggs']), b'/home/swen/')
    self.assertEqual(commonprefix([b'/home/swen/spam', b'/home/swen/spam']), b'/home/swen/spam')
    self.assertEqual(commonprefix([b'home:swenson:spam', b'home:swen:spam']), b'home:swen')
    self.assertEqual(commonprefix([b':home:swen:spam', b':home:swen:eggs']), b':home:swen:')
    self.assertEqual(commonprefix([b':home:swen:spam', b':home:swen:spam']), b':home:swen:spam')
    testlist = ['', 'abc', 'Xbcd', 'Xb', 'XY', 'abcd', 'aXc', 'abd', 'ab', 'aX', 'abcX']
    for s1 in testlist:
        for s2 in testlist:
            p = commonprefix([s1, s2])
            self.assertTrue(s1.startswith(p))
            self.assertTrue(s2.startswith(p))
            if s1 != s2:
                n = len(p)
                self.assertNotEqual(s1[n:n + 1], s2[n:n + 1])
