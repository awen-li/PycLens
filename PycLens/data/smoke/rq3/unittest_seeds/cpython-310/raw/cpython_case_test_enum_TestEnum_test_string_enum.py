# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_string_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SkillLevel(str, Enum):
        master = 'what is the sound of one hand clapping?'
        journeyman = 'why did the chicken cross the road?'
        apprentice = 'knock, knock!'
    self.assertEqual(SkillLevel.apprentice, 'knock, knock!')
