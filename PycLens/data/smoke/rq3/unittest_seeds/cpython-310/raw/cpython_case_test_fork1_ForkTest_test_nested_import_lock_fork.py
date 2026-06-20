# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fork1.py
# case: ForkTest_test_nested_import_lock_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exitcode = 42

    def fork_with_import_lock(level):
        release = 0
        in_child = False
        try:
            try:
                for i in range(level):
                    imp.acquire_lock()
                    release += 1
                pid = os.fork()
                in_child = not pid
            finally:
                for i in range(release):
                    imp.release_lock()
        except RuntimeError:
            if in_child:
                if support.verbose > 1:
                    print('RuntimeError in child')
                os._exit(1)
            raise
        if in_child:
            os._exit(exitcode)
        self.wait_impl(pid, exitcode=exitcode)
    for level in range(5):
        fork_with_import_lock(level)
