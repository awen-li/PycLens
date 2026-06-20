# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pp = pprint.PrettyPrinter()
    pp = pprint.PrettyPrinter(indent=4, width=40, depth=5, stream=io.StringIO(), compact=True)
    pp = pprint.PrettyPrinter(4, 40, 5, io.StringIO())
    pp = pprint.PrettyPrinter(sort_dicts=False)
    with self.assertRaises(TypeError):
        pp = pprint.PrettyPrinter(4, 40, 5, io.StringIO(), True)
    self.assertRaises(ValueError, pprint.PrettyPrinter, indent=-1)
    self.assertRaises(ValueError, pprint.PrettyPrinter, depth=0)
    self.assertRaises(ValueError, pprint.PrettyPrinter, depth=-1)
    self.assertRaises(ValueError, pprint.PrettyPrinter, width=0)
