# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_various_ops_small_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if verbose:
        print('with 256 KiB thread stack size...')
    try:
        threading.stack_size(262144)
    except _thread.error:
        raise unittest.SkipTest('platform does not support changing thread stack size')
    self.test_various_ops()
    threading.stack_size(0)
