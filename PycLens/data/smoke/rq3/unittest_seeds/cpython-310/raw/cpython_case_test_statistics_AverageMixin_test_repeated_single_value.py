# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: AverageMixin_test_repeated_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in self.prepare_values_for_repeated_single_test():
        for count in (2, 5, 10, 20):
            with self.subTest(x=x, count=count):
                data = [x] * count
                self.assertEqual(self.func(data), x)
