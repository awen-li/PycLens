# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_force

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_string_io = io.StringIO()
    new_string_io = io.StringIO()
    old_handlers = [logging.StreamHandler(old_string_io)]
    new_handlers = [logging.StreamHandler(new_string_io)]
    logging.basicConfig(level=logging.WARNING, handlers=old_handlers)
    logging.warning('warn')
    logging.info('info')
    logging.debug('debug')
    self.assertEqual(len(logging.root.handlers), 1)
    logging.basicConfig(level=logging.INFO, handlers=new_handlers, force=True)
    logging.warning('warn')
    logging.info('info')
    logging.debug('debug')
    self.assertEqual(len(logging.root.handlers), 1)
    self.assertEqual(old_string_io.getvalue().strip(), 'WARNING:root:warn')
    self.assertEqual(new_string_io.getvalue().strip(), 'WARNING:root:warn\nINFO:root:info')
