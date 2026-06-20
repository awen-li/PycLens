# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue13183

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = '\n            from bar import bar\n\n            def foo():\n                bar()\n\n            def nope():\n                pass\n\n            def foobar():\n                foo()\n                nope()\n\n            foobar()\n        '
    commands = '\n            from bar import bar\n            break bar\n            continue\n            step\n            step\n            quit\n        '
    bar = '\n            def bar():\n                pass\n        '
    with open('bar.py', 'w') as f:
        f.write(textwrap.dedent(bar))
    self.addCleanup(os_helper.unlink, 'bar.py')
    (stdout, stderr) = self.run_pdb_script(script, commands)
    self.assertTrue(any(('main.py(5)foo()->None' in l for l in stdout.splitlines())), 'Fail to step into the caller after a return')
