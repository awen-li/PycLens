# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(signature, ['asdf'], bar=[True])
    f.attr = []
    f_copy = copy.copy(f)
    self.assertEqual(signature(f_copy), signature(f))
    self.assertIs(f_copy.attr, f.attr)
    self.assertIs(f_copy.args, f.args)
    self.assertIs(f_copy.keywords, f.keywords)
