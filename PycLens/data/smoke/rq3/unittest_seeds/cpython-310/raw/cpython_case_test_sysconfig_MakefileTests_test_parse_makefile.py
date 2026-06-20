# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: MakefileTests_test_parse_makefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(unlink, TESTFN)
    with open(TESTFN, 'w') as makefile:
        print('var1=a$(VAR2)', file=makefile)
        print('VAR2=b$(var3)', file=makefile)
        print('var3=42', file=makefile)
        print('var4=$/invalid', file=makefile)
        print('var5=dollar$$5', file=makefile)
        print('var6=${var3}/lib/python3.5/config-$(VAR2)$(var5)-x86_64-linux-gnu', file=makefile)
    vars = sysconfig._parse_makefile(TESTFN)
    self.assertEqual(vars, {'var1': 'ab42', 'VAR2': 'b42', 'var3': 42, 'var4': '$/invalid', 'var5': 'dollar$5', 'var6': '42/lib/python3.5/config-b42dollar$5-x86_64-linux-gnu'})
