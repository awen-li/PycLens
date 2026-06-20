# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        N = 1000
        contents = bytes(range(256)) * N
        sizes = cycle([1, 19])
        n = 0
        queue = deque()
        while n < len(contents):
            size = next(sizes)
            queue.append(contents[n:n + size])
            n += size
        del contents
        with self.open(os_helper.TESTFN, self.write_mode, buffering=0) as raw:
            bufio = self.tp(raw, 8)
            errors = []

            def f():
                try:
                    while True:
                        try:
                            s = queue.popleft()
                        except IndexError:
                            return
                        bufio.write(s)
                except Exception as e:
                    errors.append(e)
                    raise
            threads = [threading.Thread(target=f) for x in range(20)]
            with threading_helper.start_threads(threads):
                time.sleep(0.02)
            self.assertFalse(errors, 'the following exceptions were caught: %r' % errors)
            bufio.close()
        with self.open(os_helper.TESTFN, 'rb') as f:
            s = f.read()
        for i in range(256):
            self.assertEqual(s.count(bytes([i])), N)
    finally:
        os_helper.unlink(os_helper.TESTFN)
