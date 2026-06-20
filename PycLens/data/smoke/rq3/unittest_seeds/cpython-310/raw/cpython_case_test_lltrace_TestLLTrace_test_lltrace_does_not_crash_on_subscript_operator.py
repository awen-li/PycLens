# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lltrace.py
# case: TestLLTrace_test_lltrace_does_not_crash_on_subscript_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'w', encoding='utf-8') as fd:
        self.addCleanup(os_helper.unlink, os_helper.TESTFN)
        fd.write(textwrap.dedent("            import code\n\n            console = code.InteractiveConsole()\n            console.push('__ltrace__ = 1')\n            console.push('a = [1, 2, 3]')\n            console.push('a[0] = 1')\n            print('unreachable if bug exists')\n            "))
        assert_python_ok(os_helper.TESTFN)
