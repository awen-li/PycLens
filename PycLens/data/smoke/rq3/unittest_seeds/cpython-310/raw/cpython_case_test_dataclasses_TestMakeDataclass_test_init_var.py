# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_init_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def post_init(self, y):
        self.x *= y
    C = make_dataclass('C', [('x', int), ('y', InitVar[int])], namespace={'__post_init__': post_init})
    c = C(2, 3)
    self.assertEqual(vars(c), {'x': 6})
    self.assertEqual(len(fields(c)), 1)
