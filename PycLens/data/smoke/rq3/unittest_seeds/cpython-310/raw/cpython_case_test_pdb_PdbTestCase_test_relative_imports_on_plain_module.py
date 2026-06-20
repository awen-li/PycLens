# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_relative_imports_on_plain_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.module_name = 't_main'
    os_helper.rmtree(self.module_name)
    main_file = self.module_name + '/runme.py'
    init_file = self.module_name + '/__init__.py'
    module_file = self.module_name + '/module.py'
    self.addCleanup(os_helper.rmtree, self.module_name)
    os.mkdir(self.module_name)
    with open(init_file, 'w') as f:
        f.write(textwrap.dedent('\n                top_var = "VAR from top"\n            '))
    with open(main_file, 'w') as f:
        f.write(textwrap.dedent("\n                from . import module\n                pass # We'll stop here and print the vars\n            "))
    with open(module_file, 'w') as f:
        f.write(textwrap.dedent('\n                var = "VAR from module"\n            '))
    commands = '\n            b 3\n            c\n            p module.var\n            quit\n        '
    (stdout, _) = self._run_pdb(['-m', self.module_name + '.runme'], commands)
    self.assertTrue(any(('VAR from module' in l for l in stdout.splitlines())), stdout)
