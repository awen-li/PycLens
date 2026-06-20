# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_exception_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(state=[0]):
        i = state[0]
        state[0] = i + 1
        if i == 10:
            raise RuntimeError
        return i
    res = []
    try:
        for x in iter(spam, 20):
            res.append(x)
    except RuntimeError:
        self.assertEqual(res, list(range(10)))
    else:
        self.fail('should have raised RuntimeError')
