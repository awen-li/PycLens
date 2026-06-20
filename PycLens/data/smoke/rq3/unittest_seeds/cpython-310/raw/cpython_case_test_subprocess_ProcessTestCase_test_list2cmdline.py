# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_list2cmdline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(subprocess.list2cmdline(['a b c', 'd', 'e']), '"a b c" d e')
    self.assertEqual(subprocess.list2cmdline(['ab"c', '\\', 'd']), 'ab\\"c \\ d')
    self.assertEqual(subprocess.list2cmdline(['ab"c', ' \\', 'd']), 'ab\\"c " \\\\" d')
    self.assertEqual(subprocess.list2cmdline(['a\\\\\\b', 'de fg', 'h']), 'a\\\\\\b "de fg" h')
    self.assertEqual(subprocess.list2cmdline(['a\\"b', 'c', 'd']), 'a\\\\\\"b c d')
    self.assertEqual(subprocess.list2cmdline(['a\\\\b c', 'd', 'e']), '"a\\\\b c" d e')
    self.assertEqual(subprocess.list2cmdline(['a\\\\b\\ c', 'd', 'e']), '"a\\\\b\\ c" d e')
    self.assertEqual(subprocess.list2cmdline(['ab', '']), 'ab ""')
