# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_ident_of_no_threading_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNotNone(threading.current_thread().ident)

    def f():
        ident.append(threading.current_thread().ident)
        done.set()
    done = threading.Event()
    ident = []
    with threading_helper.wait_threads_exit():
        tid = _thread.start_new_thread(f, ())
        done.wait()
        self.assertEqual(ident[0], tid)
    del threading._active[ident[0]]
