# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_flufl_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Fluflnum(Enum):

        def __int__(self):
            return int(self.value)

    class MailManOptions(Fluflnum):
        option1 = 1
        option2 = 2
        option3 = 3
    self.assertEqual(int(MailManOptions.option1), 1)
