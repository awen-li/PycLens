# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_tee_concurrent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start = threading.Event()
    finish = threading.Event()

    class I:

        def __iter__(self):
            return self

        def __next__(self):
            start.set()
            finish.wait()
    (a, b) = tee(I())
    thread = threading.Thread(target=next, args=[a])
    thread.start()
    try:
        start.wait()
        with self.assertRaisesRegex(RuntimeError, 'tee'):
            next(b)
    finally:
        finish.set()
        thread.join()
