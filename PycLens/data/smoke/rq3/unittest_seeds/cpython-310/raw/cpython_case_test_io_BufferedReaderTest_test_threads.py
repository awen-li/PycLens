# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        N = 1000
        l = list(range(256)) * N
        random.shuffle(l)
        s = bytes(bytearray(l))
        with self.open(os_helper.TESTFN, 'wb') as f:
            f.write(s)
        with self.open(os_helper.TESTFN, self.read_mode, buffering=0) as raw:
            bufio = self.tp(raw, 8)
            errors = []
            results = []

            def f():
                try:
                    for n in cycle([1, 19]):
                        s = bufio.read(n)
                        if not s:
                            break
                        results.append(s)
                except Exception as e:
                    errors.append(e)
                    raise
            threads = [threading.Thread(target=f) for x in range(20)]
            with threading_helper.start_threads(threads):
                time.sleep(0.02)
            self.assertFalse(errors, 'the following exceptions were caught: %r' % errors)
            s = b''.join(results)
            for i in range(256):
                c = bytes(bytearray([i]))
                self.assertEqual(s.count(c), N)
    finally:
        os_helper.unlink(os_helper.TESTFN)
