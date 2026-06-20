# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test__use_vfork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(subprocess._USE_VFORK)
    with mock.patch.object(subprocess, '_USE_VFORK', False):
        self.assertEqual(self.run_python('pass').returncode, 0, msg='False _USE_VFORK failed')

    class RaisingBool:

        def __bool__(self):
            raise RuntimeError('force PyObject_IsTrue to return -1')
    with mock.patch.object(subprocess, '_USE_VFORK', RaisingBool()):
        self.assertEqual(self.run_python('pass').returncode, 0, msg='odd bool()-error _USE_VFORK failed')
        del subprocess._USE_VFORK
        self.assertEqual(self.run_python('pass').returncode, 0, msg='lack of a _USE_VFORK attribute failed')
