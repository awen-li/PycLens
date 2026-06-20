# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syslog.py
# case: Test_test_syslog_threaded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start = threading.Event()
    stop = False

    def opener():
        start.wait(10)
        i = 1
        while not stop:
            syslog.openlog(f'python-test-{i}')
            i += 1

    def logger():
        start.wait(10)
        while not stop:
            syslog.syslog('test message from python test_syslog')
    orig_si = sys.getswitchinterval()
    support.setswitchinterval(1e-09)
    try:
        threads = [threading.Thread(target=opener)]
        threads += [threading.Thread(target=logger) for k in range(10)]
        with threading_helper.start_threads(threads):
            start.set()
            time.sleep(0.1)
            stop = True
    finally:
        sys.setswitchinterval(orig_si)
