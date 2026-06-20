# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_getsitepackages

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    site.PREFIXES = ['xoxo']
    dirs = site.getsitepackages()
    if os.sep == '/':
        if sys.platlibdir != 'lib':
            self.assertEqual(len(dirs), 2)
            wanted = os.path.join('xoxo', sys.platlibdir, 'python%d.%d' % sys.version_info[:2], 'site-packages')
            self.assertEqual(dirs[0], wanted)
        else:
            self.assertEqual(len(dirs), 1)
        wanted = os.path.join('xoxo', 'lib', 'python%d.%d' % sys.version_info[:2], 'site-packages')
        self.assertEqual(dirs[-1], wanted)
    else:
        self.assertEqual(len(dirs), 2)
        self.assertEqual(dirs[0], 'xoxo')
        wanted = os.path.join('xoxo', 'lib', 'site-packages')
        self.assertEqual(dirs[1], wanted)
