# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestModule_test_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    pid = os.fork()
    if pid == 0:
        try:
            val = random.getrandbits(128)
            with open(w, 'w') as f:
                f.write(str(val))
        finally:
            os._exit(0)
    else:
        os.close(w)
        val = random.getrandbits(128)
        with open(r, 'r') as f:
            child_val = eval(f.read())
        self.assertNotEqual(val, child_val)
        support.wait_process(pid, exitcode=0)
