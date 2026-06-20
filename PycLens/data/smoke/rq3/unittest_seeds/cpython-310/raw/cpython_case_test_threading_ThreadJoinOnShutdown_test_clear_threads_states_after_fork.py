# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadJoinOnShutdown_test_clear_threads_states_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    threads = []
    for i in range(16):
        t = threading.Thread(target=lambda : time.sleep(0.3))
        threads.append(t)
        t.start()
    pid = os.fork()
    if pid == 0:
        if len(sys._current_frames()) == 1:
            os._exit(51)
        else:
            os._exit(52)
    else:
        support.wait_process(pid, exitcode=51)
    for t in threads:
        t.join()
