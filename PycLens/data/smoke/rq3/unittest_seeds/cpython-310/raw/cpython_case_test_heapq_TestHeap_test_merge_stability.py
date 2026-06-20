# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_merge_stability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Int(int):
        pass
    inputs = [[], [], [], []]
    for i in range(20000):
        stream = random.randrange(4)
        x = random.randrange(500)
        obj = Int(x)
        obj.pair = (x, stream)
        inputs[stream].append(obj)
    for stream in inputs:
        stream.sort()
    result = [i.pair for i in self.module.merge(*inputs)]
    self.assertEqual(result, sorted(result))
