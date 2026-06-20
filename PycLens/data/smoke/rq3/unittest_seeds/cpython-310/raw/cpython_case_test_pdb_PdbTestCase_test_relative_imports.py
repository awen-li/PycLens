# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_relative_imports

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.module_name = 't_main'
    os_helper.rmtree(self.module_name)
    main_file = self.module_name + '/__main__.py'
    init_file = self.module_name + '/__init__.py'
    module_file = self.module_name + '/module.py'
    self.addCleanup(os_helper.rmtree, self.module_name)
    os.mkdir(self.module_name)
    with open(init_file, 'w') as f:
        f.write(textwrap.dedent('\n                top_var = "VAR from top"\n            '))
    with open(main_file, 'w') as f:
        f.write(textwrap.dedent("\n                from . import top_var\n                from .module import var\n                from . import module\n                pass # We'll stop here and print the vars\n            "))
    with open(module_file, 'w') as f:
        f.write(textwrap.dedent('\n                var = "VAR from module"\n                var2 = "second var"\n            '))
    commands = '\n            b 5\n            c\n            p top_var\n            p var\n            p module.var2\n            quit\n        '
    (stdout, _) = self._run_pdb(['-m', self.module_name], commands)
    self.assertTrue(any(('VAR from module' in l for l in stdout.splitlines())), stdout)
    self.assertTrue(any(('VAR from top' in l for l in stdout.splitlines())))
    self.assertTrue(any(('second var' in l for l in stdout.splitlines())))
