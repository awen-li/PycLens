# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: RawConfigParserTestCase_test_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_items_config([('default', '<default>'), ('getdefault', '|%(default)s|'), ('key', '|%(name)s|'), ('name', '%(value)s')])
