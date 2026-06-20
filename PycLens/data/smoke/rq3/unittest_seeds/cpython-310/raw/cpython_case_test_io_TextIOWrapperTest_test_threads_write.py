# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_threads_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    event = threading.Event()
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8', buffering=1) as f:

        def run(n):
            text = 'Thread%03d\n' % n
            event.wait()
            f.write(text)
        threads = [threading.Thread(target=run, args=(x,)) for x in range(20)]
        with threading_helper.start_threads(threads, event.set):
            time.sleep(0.02)
    with self.open(os_helper.TESTFN, encoding='utf-8') as f:
        content = f.read()
        for n in range(20):
            self.assertEqual(content.count('Thread%03d\n' % n), 1)
