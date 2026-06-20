# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_dir_on_sub_with_behavior_including_instance_dict_on_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SuperEnum(IntEnum):

        def __new__(cls, value, description=''):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.description = description
            return obj

    class SubEnum(SuperEnum):
        sample = 5
    self.assertTrue({'description'} <= set(dir(SubEnum.sample)))
