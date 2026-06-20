# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test___future__.py
# case: FutureTest_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for feature in features:
        value = getattr(__future__, feature)
        optional = value.getOptionalRelease()
        mandatory = value.getMandatoryRelease()
        a = self.assertTrue
        e = self.assertEqual

        def check(t, name):
            a(isinstance(t, tuple), "%s isn't tuple" % name)
            e(len(t), 5, "%s isn't 5-tuple" % name)
            (major, minor, micro, level, serial) = t
            a(isinstance(major, int), "%s major isn't int" % name)
            a(isinstance(minor, int), "%s minor isn't int" % name)
            a(isinstance(micro, int), "%s micro isn't int" % name)
            a(isinstance(level, str), "%s level isn't string" % name)
            a(level in GOOD_SERIALS, '%s level string has unknown value' % name)
            a(isinstance(serial, int), "%s serial isn't int" % name)
        check(optional, 'optional')
        if mandatory is not None:
            check(mandatory, 'mandatory')
            a(optional < mandatory, 'optional not less than mandatory, and mandatory not None')
        a(hasattr(value, 'compiler_flag'), 'feature is missing a .compiler_flag attr')
        compile('', '<test>', 'exec', value.compiler_flag)
        a(isinstance(getattr(value, 'compiler_flag'), int), ".compiler_flag isn't int")
