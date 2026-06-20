# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_threadsafe_wait

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(12)'])
    self.assertEqual(proc.returncode, None)
    results = []

    def kill_proc_timer_thread():
        results.append(('thread-start-poll-result', proc.poll()))
        proc.kill()
        proc.wait()
        results.append(('thread-after-kill-and-wait', proc.returncode))
        proc.wait()
        results.append(('thread-after-second-wait', proc.returncode))
    t = threading.Timer(0.2, kill_proc_timer_thread)
    t.start()
    if mswindows:
        expected_errorcode = 1
    else:
        expected_errorcode = -9
    proc.wait(timeout=support.SHORT_TIMEOUT)
    self.assertEqual(proc.returncode, expected_errorcode, msg='unexpected result in wait from main thread')
    proc.wait()
    self.assertEqual(proc.returncode, expected_errorcode, msg='unexpected result in second main wait.')
    t.join()
    self.assertEqual([('thread-start-poll-result', None), ('thread-after-kill-and-wait', expected_errorcode), ('thread-after-second-wait', expected_errorcode)], results)
