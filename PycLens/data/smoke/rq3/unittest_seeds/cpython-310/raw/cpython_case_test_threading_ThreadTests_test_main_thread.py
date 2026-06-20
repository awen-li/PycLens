# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_main_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    main = threading.main_thread()
    self.assertEqual(main.name, 'MainThread')
    self.assertEqual(main.ident, threading.current_thread().ident)
    self.assertEqual(main.ident, threading.get_ident())

    def f():
        self.assertNotEqual(threading.main_thread().ident, threading.current_thread().ident)
    th = threading.Thread(target=f)
    th.start()
    th.join()
