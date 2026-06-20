# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_track_subtypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyTuple(tuple):
        pass
    self.check_track_dynamic(MyTuple, True)
