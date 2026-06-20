# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_stop_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySequenceClass(SequenceClass):

        def __getitem__(self, i):
            if i == 10:
                raise StopIteration
            return SequenceClass.__getitem__(self, i)
    self.check_for_loop(MySequenceClass(20), list(range(10)), pickle=False)
