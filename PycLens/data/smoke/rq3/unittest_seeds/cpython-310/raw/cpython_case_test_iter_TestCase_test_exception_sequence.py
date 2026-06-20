# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_exception_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySequenceClass(SequenceClass):

        def __getitem__(self, i):
            if i == 10:
                raise RuntimeError
            return SequenceClass.__getitem__(self, i)
    res = []
    try:
        for x in MySequenceClass(20):
            res.append(x)
    except RuntimeError:
        self.assertEqual(res, list(range(10)))
    else:
        self.fail('should have raised RuntimeError')
