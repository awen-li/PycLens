# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir_of_gen_alias = set(dir(list[int]))
    self.assertTrue(dir_of_gen_alias.issuperset(dir(list)))
    for generic_alias_property in ('__origin__', '__args__', '__parameters__'):
        self.assertIn(generic_alias_property, dir_of_gen_alias)
