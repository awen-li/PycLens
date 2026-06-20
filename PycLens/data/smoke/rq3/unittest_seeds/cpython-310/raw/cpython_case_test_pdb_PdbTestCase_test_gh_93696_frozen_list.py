# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_gh_93696_frozen_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    frozen_src = '\n        def func():\n            x = "Sentinel string for gh-93696"\n            print(x)\n        '
    host_program = '\n        import os\n        import sys\n\n        def _create_fake_frozen_module():\n            with open(\'gh93696.py\') as f:\n                src = f.read()\n\n            # this function has a co_filename as if it were in a frozen module\n            dummy_mod = compile(src, "<frozen gh93696>", "exec")\n            func_code = dummy_mod.co_consts[0]\n\n            mod = type(sys)("gh93696")\n            mod.func = type(lambda: None)(func_code, mod.__dict__)\n            mod.__file__ = \'gh93696.py\'\n\n            return mod\n\n        mod = _create_fake_frozen_module()\n        mod.func()\n        '
    commands = '\n            break 20\n            continue\n            step\n            list\n            quit\n        '
    with open('gh93696.py', 'w') as f:
        f.write(textwrap.dedent(frozen_src))
    with open('gh93696_host.py', 'w') as f:
        f.write(textwrap.dedent(host_program))
    self.addCleanup(os_helper.unlink, 'gh93696.py')
    self.addCleanup(os_helper.unlink, 'gh93696_host.py')
    (stdout, stderr) = self._run_pdb(['gh93696_host.py'], commands)
    self.assertIn('x = "Sentinel string for gh-93696"', stdout, 'Sentinel statement not found')
