# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_basic_from_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'Foo Bar': {'foo': 'bar1'}, 'Spacey Bar': {'foo': 'bar2'}, 'Spacey Bar From The Beginning': {'foo': 'bar3', 'baz': 'qwe'}, 'Commented Bar': {'foo': 'bar4', 'baz': 'qwe'}, 'Long Line': {'foo': 'this line is much, much longer than my editor\nlikes it.'}, 'Section\\with$weird%characters[\t': {}, 'Internationalized Stuff': {'foo[bg]': 'Bulgarian', 'foo': 'Default', 'foo[en]': 'English', 'foo[de]': 'Deutsch'}, 'Spaces': {'key with spaces': 'value', 'another with spaces': 'splat!'}, 'Types': {'int': 42, 'float': 0.44, 'boolean': False, 123: 'strange but acceptable'}, 'This One Has A ] In It': {'forks': 'spoons'}}
    if self.allow_no_value:
        config.update({'NoValue': {'option-without-value': None}})
    cf = self.newconfig()
    cf.read_dict(config)
    self.basic_test(cf)
    if self.strict:
        with self.assertRaises(configparser.DuplicateSectionError):
            cf.read_dict({'1': {'key': 'value'}, 1: {'key2': 'value2'}})
        with self.assertRaises(configparser.DuplicateOptionError):
            cf.read_dict({'Duplicate Options Here': {'option': 'with a value', 'OPTION': 'with another value'}})
    else:
        cf.read_dict({'section': {'key': 'value'}, 'SECTION': {'key2': 'value2'}})
        cf.read_dict({'Duplicate Options Here': {'option': 'with a value', 'OPTION': 'with another value'}})
