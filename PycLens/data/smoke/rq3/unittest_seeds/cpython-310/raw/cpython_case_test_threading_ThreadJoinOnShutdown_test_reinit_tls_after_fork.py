# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadJoinOnShutdown_test_reinit_tls_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def do_fork_and_wait():
        pid = os.fork()
        if pid > 0:
            support.wait_process(pid, exitcode=50)
        else:
            os._exit(50)
    threads = []
    for i in range(16):
        t = threading.Thread(target=do_fork_and_wait)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
