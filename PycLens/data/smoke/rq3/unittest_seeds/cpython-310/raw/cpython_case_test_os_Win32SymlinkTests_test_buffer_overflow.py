# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_buffer_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    segment = 'X' * 27
    path = os.path.join(*[segment] * 10)
    test_cases = [('\\' + path, segment), (segment, path), (path[:180], path[:180])]
    for (src, dest) in test_cases:
        try:
            os.symlink(src, dest)
        except FileNotFoundError:
            pass
        else:
            try:
                os.remove(dest)
            except OSError:
                pass
        try:
            os.symlink(os.fsencode(src), os.fsencode(dest))
        except FileNotFoundError:
            pass
        else:
            try:
                os.remove(dest)
            except OSError:
                pass
