# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_get_traces_intern_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def allocate_bytes2(size):
        return allocate_bytes(size)

    def allocate_bytes3(size):
        return allocate_bytes2(size)

    def allocate_bytes4(size):
        return allocate_bytes3(size)
    tracemalloc.stop()
    tracemalloc.start(4)
    obj_size = 123
    (obj1, obj1_traceback) = allocate_bytes4(obj_size)
    (obj2, obj2_traceback) = allocate_bytes4(obj_size)
    traces = tracemalloc._get_traces()
    obj1_traceback._frames = tuple(reversed(obj1_traceback._frames))
    obj2_traceback._frames = tuple(reversed(obj2_traceback._frames))
    trace1 = self.find_trace(traces, obj1_traceback)
    trace2 = self.find_trace(traces, obj2_traceback)
    (domain1, size1, traceback1, length1) = trace1
    (domain2, size2, traceback2, length2) = trace2
    self.assertIs(traceback2, traceback1)
