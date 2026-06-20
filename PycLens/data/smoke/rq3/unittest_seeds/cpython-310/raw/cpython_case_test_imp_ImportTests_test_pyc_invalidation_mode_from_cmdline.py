# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_pyc_invalidation_mode_from_cmdline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = [([], 'default'), (['--check-hash-based-pycs', 'default'], 'default'), (['--check-hash-based-pycs', 'always'], 'always'), (['--check-hash-based-pycs', 'never'], 'never')]
    for (interp_args, expected) in cases:
        args = interp_args + ['-c', 'import _imp; print(_imp.check_hash_based_pycs)']
        res = script_helper.assert_python_ok(*args)
        self.assertEqual(res.out.strip().decode('utf-8'), expected)
