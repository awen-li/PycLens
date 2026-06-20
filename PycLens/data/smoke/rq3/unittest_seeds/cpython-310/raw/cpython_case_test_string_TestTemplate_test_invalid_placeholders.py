# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_invalid_placeholders

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raises = self.assertRaises
    s = Template('$who likes $')
    raises(ValueError, s.substitute, dict(who='tim'))
    s = Template('$who likes ${what)')
    raises(ValueError, s.substitute, dict(who='tim'))
    s = Template('$who likes $100')
    raises(ValueError, s.substitute, dict(who='tim'))
    s = Template('$who likes $ı')
    raises(ValueError, s.substitute, dict(who='tim'))
    s = Template('$who likes $İ')
    raises(ValueError, s.substitute, dict(who='tim'))
