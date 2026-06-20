# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_dump_ext_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "\n            import faulthandler\n            import sys\n            # Don't filter stdlib module names\n            sys.stdlib_module_names = frozenset()\n            faulthandler.enable()\n            faulthandler._sigsegv()\n            "
    (stderr, exitcode) = self.get_output(code)
    stderr = '\n'.join(stderr)
    match = re.search('^Extension modules:(.*) \\(total: [0-9]+\\)$', stderr, re.MULTILINE)
    if not match:
        self.fail(f"Cannot find 'Extension modules:' in {stderr!r}")
    modules = set(match.group(1).strip().split(', '))
    for name in ('sys', 'faulthandler'):
        self.assertIn(name, modules)
