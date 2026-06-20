# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_regular_templates_with_non_letters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = Template('$_wh0_ likes ${_w_h_a_t_} for ${mea1}')
    d = dict(_wh0_='tim', _w_h_a_t_='ham', mea1='dinner')
    self.assertEqual(s.substitute(d), 'tim likes ham for dinner')
