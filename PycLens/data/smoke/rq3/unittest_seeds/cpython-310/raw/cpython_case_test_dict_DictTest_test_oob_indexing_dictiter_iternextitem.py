# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_oob_indexing_dictiter_iternextitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(int):

        def __del__(self):
            d.clear()
    d = {i: X(i) for i in range(8)}

    def iter_and_mutate():
        for result in d.items():
            if result[0] == 2:
                d[2] = None
    self.assertRaises(RuntimeError, iter_and_mutate)
