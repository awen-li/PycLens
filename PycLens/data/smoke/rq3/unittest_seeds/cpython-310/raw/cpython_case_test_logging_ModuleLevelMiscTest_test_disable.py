# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_disable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_disable = logging.root.manager.disable
    self.assertEqual(old_disable, 0)
    self.addCleanup(logging.disable, old_disable)
    logging.disable(83)
    self.assertEqual(logging.root.manager.disable, 83)
    self.assertRaises(ValueError, logging.disable, 'doesnotexists')

    class _NotAnIntOrString:
        pass
    self.assertRaises(TypeError, logging.disable, _NotAnIntOrString())
    logging.disable('WARN')
    logging.disable()
    self.assertEqual(logging.root.manager.disable, logging.CRITICAL)
