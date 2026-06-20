# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_dir_on_sub_with_behavior_on_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SuperEnum(Enum):

        def invisible(self):
            return 'did you see me?'

    class SubEnum(SuperEnum):
        sample = 5
    self.assertEqual(set(dir(SubEnum.sample)), set(['__class__', '__doc__', '__module__', 'name', 'value', 'invisible']))
