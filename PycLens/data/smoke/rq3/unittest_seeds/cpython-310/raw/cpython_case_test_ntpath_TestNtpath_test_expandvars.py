# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_expandvars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        env['foo'] = 'bar'
        env['{foo'] = 'baz1'
        env['{foo}'] = 'baz2'
        tester('ntpath.expandvars("foo")', 'foo')
        tester('ntpath.expandvars("$foo bar")', 'bar bar')
        tester('ntpath.expandvars("${foo}bar")', 'barbar')
        tester('ntpath.expandvars("$[foo]bar")', '$[foo]bar')
        tester('ntpath.expandvars("$bar bar")', '$bar bar')
        tester('ntpath.expandvars("$?bar")', '$?bar')
        tester('ntpath.expandvars("$foo}bar")', 'bar}bar')
        tester('ntpath.expandvars("${foo")', '${foo')
        tester('ntpath.expandvars("${{foo}}")', 'baz1}')
        tester('ntpath.expandvars("$foo$foo")', 'barbar')
        tester('ntpath.expandvars("$bar$bar")', '$bar$bar')
        tester('ntpath.expandvars("%foo% bar")', 'bar bar')
        tester('ntpath.expandvars("%foo%bar")', 'barbar')
        tester('ntpath.expandvars("%foo%%foo%")', 'barbar')
        tester('ntpath.expandvars("%%foo%%foo%foo%")', '%foo%foobar')
        tester('ntpath.expandvars("%?bar%")', '%?bar%')
        tester('ntpath.expandvars("%foo%%bar")', 'bar%bar')
        tester('ntpath.expandvars("\'%foo%\'%bar")', "'%foo%'%bar")
        tester('ntpath.expandvars("bar\'%foo%")', "bar'%foo%")
