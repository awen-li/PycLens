# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_dir_with_added_behavior

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test(Enum):
        this = 'that'
        these = 'those'

        def wowser(self):
            return "Wowser! I'm %s!" % self.name
    self.assertEqual(set(dir(Test)), set(['__class__', '__doc__', '__members__', '__module__', 'this', 'these']))
    self.assertEqual(set(dir(Test.this)), set(['__class__', '__doc__', '__module__', 'name', 'value', 'wowser']))
