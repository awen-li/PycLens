# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_expandvars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expandvars = self.pathmodule.expandvars
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        env['foo'] = 'bar'
        env['{foo'] = 'baz1'
        env['{foo}'] = 'baz2'
        self.assertEqual(expandvars('foo'), 'foo')
        self.assertEqual(expandvars('$foo bar'), 'bar bar')
        self.assertEqual(expandvars('${foo}bar'), 'barbar')
        self.assertEqual(expandvars('$[foo]bar'), '$[foo]bar')
        self.assertEqual(expandvars('$bar bar'), '$bar bar')
        self.assertEqual(expandvars('$?bar'), '$?bar')
        self.assertEqual(expandvars('$foo}bar'), 'bar}bar')
        self.assertEqual(expandvars('${foo'), '${foo')
        self.assertEqual(expandvars('${{foo}}'), 'baz1}')
        self.assertEqual(expandvars('$foo$foo'), 'barbar')
        self.assertEqual(expandvars('$bar$bar'), '$bar$bar')
        self.assertEqual(expandvars(b'foo'), b'foo')
        self.assertEqual(expandvars(b'$foo bar'), b'bar bar')
        self.assertEqual(expandvars(b'${foo}bar'), b'barbar')
        self.assertEqual(expandvars(b'$[foo]bar'), b'$[foo]bar')
        self.assertEqual(expandvars(b'$bar bar'), b'$bar bar')
        self.assertEqual(expandvars(b'$?bar'), b'$?bar')
        self.assertEqual(expandvars(b'$foo}bar'), b'bar}bar')
        self.assertEqual(expandvars(b'${foo'), b'${foo')
        self.assertEqual(expandvars(b'${{foo}}'), b'baz1}')
        self.assertEqual(expandvars(b'$foo$foo'), b'barbar')
        self.assertEqual(expandvars(b'$bar$bar'), b'$bar$bar')
