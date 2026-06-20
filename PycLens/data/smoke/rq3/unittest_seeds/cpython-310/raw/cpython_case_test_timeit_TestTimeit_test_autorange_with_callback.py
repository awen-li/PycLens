# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_autorange_with_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def callback(a, b):
        print('{} {:.3f}'.format(a, b))
    with captured_stdout() as s:
        (num_loops, time_taken) = self.autorange(callback=callback)
    self.assertEqual(num_loops, 500)
    self.assertEqual(time_taken, 500 / 1024)
    expected = '1 0.001\n2 0.002\n5 0.005\n10 0.010\n20 0.020\n50 0.049\n100 0.098\n200 0.195\n500 0.488\n'
    self.assertEqual(s.getvalue(), expected)
