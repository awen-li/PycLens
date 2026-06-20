# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: MiscTests_test_ncurses_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v = curses.ncurses_version
    if verbose:
        print(f'ncurses_version = {curses.ncurses_version}', flush=True)
    self.assertIsInstance(v[:], tuple)
    self.assertEqual(len(v), 3)
    self.assertIsInstance(v[0], int)
    self.assertIsInstance(v[1], int)
    self.assertIsInstance(v[2], int)
    self.assertIsInstance(v.major, int)
    self.assertIsInstance(v.minor, int)
    self.assertIsInstance(v.patch, int)
    self.assertEqual(v[0], v.major)
    self.assertEqual(v[1], v.minor)
    self.assertEqual(v[2], v.patch)
    self.assertGreaterEqual(v.major, 0)
    self.assertGreaterEqual(v.minor, 0)
    self.assertGreaterEqual(v.patch, 0)
