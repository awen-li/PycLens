# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_order_of_insertion_does_not_matter_between_groups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def get_groups(ts):
        ts.prepare()
        while ts.is_active():
            nodes = ts.get_ready()
            ts.done(*nodes)
            yield set(nodes)
    ts = graphlib.TopologicalSorter()
    ts.add(3, 2, 1)
    ts.add(1, 0)
    ts.add(4, 5)
    ts.add(6, 7)
    ts.add(4, 7)
    ts2 = graphlib.TopologicalSorter()
    ts2.add(1, 0)
    ts2.add(3, 2, 1)
    ts2.add(4, 7)
    ts2.add(6, 7)
    ts2.add(4, 5)
    self.assertEqual(list(get_groups(ts)), list(get_groups(ts2)))
