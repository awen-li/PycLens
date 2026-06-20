# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TermsizeTests_test_stty_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        size = subprocess.check_output(['stty', 'size'], stderr=subprocess.DEVNULL, text=True).split()
    except (FileNotFoundError, subprocess.CalledProcessError, PermissionError):
        self.skipTest('stty invocation failed')
    expected = (int(size[1]), int(size[0]))
    try:
        actual = os.get_terminal_size(sys.__stdin__.fileno())
    except OSError as e:
        if sys.platform == 'win32' or e.errno in (errno.EINVAL, errno.ENOTTY):
            self.skipTest('failed to query terminal size')
        raise
    self.assertEqual(expected, actual)
