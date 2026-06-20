# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: TimerTests_test_init_immutable_default_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    timer1 = threading.Timer(0.01, self._callback_spy)
    timer1.start()
    self.callback_event.wait()
    timer1.args.append('blah')
    timer1.kwargs['foo'] = 'bar'
    self.callback_event.clear()
    timer2 = threading.Timer(0.01, self._callback_spy)
    timer2.start()
    self.callback_event.wait()
    self.assertEqual(len(self.callback_args), 2)
    self.assertEqual(self.callback_args, [((), {}), ((), {})])
    timer1.join()
    timer2.join()
