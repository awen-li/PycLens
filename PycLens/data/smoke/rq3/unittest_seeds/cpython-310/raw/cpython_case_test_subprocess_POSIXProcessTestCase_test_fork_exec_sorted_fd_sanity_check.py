# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_fork_exec_sorted_fd_sanity_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _posixsubprocess

    class BadInt:
        first = True

        def __init__(self, value):
            self.value = value

        def __int__(self):
            if self.first:
                self.first = False
                return self.value
            raise ValueError
    gc_enabled = gc.isenabled()
    try:
        gc.enable()
        for fds_to_keep in ((-1, 2, 3, 4, 5), ('str', 4), (18, 23, 42, 2 ** 63), (5, 4), (6, 7, 7, 8), (BadInt(1), BadInt(2))):
            with self.assertRaises(ValueError, msg='fds_to_keep={}'.format(fds_to_keep)) as c:
                _posixsubprocess.fork_exec([b'false'], [b'false'], True, fds_to_keep, None, [b'env'], -1, -1, -1, -1, 1, 2, 3, 4, True, True, None, None, None, -1, None)
            self.assertIn('fds_to_keep', str(c.exception))
    finally:
        if not gc_enabled:
            gc.disable()
