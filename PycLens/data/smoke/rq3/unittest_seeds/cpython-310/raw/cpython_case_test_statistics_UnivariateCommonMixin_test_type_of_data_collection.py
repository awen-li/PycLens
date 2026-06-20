# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_type_of_data_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyList(list):
        pass

    class MyTuple(tuple):
        pass

    def generator(data):
        return (obj for obj in data)
    data = self.prepare_data()
    expected = self.func(data)
    for kind in (list, tuple, iter, MyList, MyTuple, generator):
        result = self.func(kind(data))
        self.assertEqual(result, expected)
