# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_set_string_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[sect]\noption1{eq}foo\n'.format(eq=self.delimiters[0]))

    class mystr(str):
        pass
    cf.set('sect', 'option1', 'splat')
    cf.set('sect', 'option1', mystr('splat'))
    cf.set('sect', 'option2', 'splat')
    cf.set('sect', 'option2', mystr('splat'))
    cf.set('sect', 'option1', 'splat')
    cf.set('sect', 'option2', 'splat')
