# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_open_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaisesRegex(ValueError, 'negative file descriptor', ConIO, -1)
    with tempfile.TemporaryFile() as tmpfile:
        fd = tmpfile.fileno()
        self.assertRaisesRegex(ValueError, 'Cannot open (console|non-console file)', ConIO, fd)
    try:
        f = ConIO(0)
    except ValueError:
        pass
    else:
        self.assertTrue(f.readable())
        self.assertFalse(f.writable())
        self.assertEqual(0, f.fileno())
        f.close()
        f.close()
    try:
        f = ConIO(1, 'w')
    except ValueError:
        pass
    else:
        self.assertFalse(f.readable())
        self.assertTrue(f.writable())
        self.assertEqual(1, f.fileno())
        f.close()
        f.close()
    try:
        f = ConIO(2, 'w')
    except ValueError:
        pass
    else:
        self.assertFalse(f.readable())
        self.assertTrue(f.writable())
        self.assertEqual(2, f.fileno())
        f.close()
        f.close()
