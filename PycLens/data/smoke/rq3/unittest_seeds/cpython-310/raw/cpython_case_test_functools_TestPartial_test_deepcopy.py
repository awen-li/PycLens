# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_deepcopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.partial(signature, ['asdf'], bar=[True])
    f.attr = []
    f_copy = copy.deepcopy(f)
    self.assertEqual(signature(f_copy), signature(f))
    self.assertIsNot(f_copy.attr, f.attr)
    self.assertIsNot(f_copy.args, f.args)
    self.assertIsNot(f_copy.args[0], f.args[0])
    self.assertIsNot(f_copy.keywords, f.keywords)
    self.assertIsNot(f_copy.keywords['bar'], f.keywords['bar'])
