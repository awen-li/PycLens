# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_function_stop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(state=[0]):
        i = state[0]
        if i == 10:
            raise StopIteration
        state[0] = i + 1
        return i
    self.check_iterator(iter(spam, 20), list(range(10)), pickle=False)
