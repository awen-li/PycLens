# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: InterruptMainTests_test_interrupt_main_subthread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def call_interrupt():
        _thread.interrupt_main()
    t = threading.Thread(target=call_interrupt)
    with self.assertRaises(KeyboardInterrupt):
        t.start()
        t.join()
    t.join()
