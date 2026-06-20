# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerAdapterTest_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Adapter(logging.LoggerAdapter):
        prefix = 'Adapter'

        def process(self, msg, kwargs):
            return (f'{self.prefix} {msg}', kwargs)
    msg = 'Adapters can be nested, yo.'
    adapter = Adapter(logger=self.logger, extra=None)
    adapter_adapter = Adapter(logger=adapter, extra=None)
    adapter_adapter.prefix = 'AdapterAdapter'
    self.assertEqual(repr(adapter), repr(adapter_adapter))
    adapter_adapter.log(logging.CRITICAL, msg, self.recording)
    self.assertEqual(len(self.recording.records), 1)
    record = self.recording.records[0]
    self.assertEqual(record.levelno, logging.CRITICAL)
    self.assertEqual(record.msg, f'Adapter AdapterAdapter {msg}')
    self.assertEqual(record.args, (self.recording,))
    orig_manager = adapter_adapter.manager
    self.assertIs(adapter.manager, orig_manager)
    self.assertIs(self.logger.manager, orig_manager)
    temp_manager = object()
    try:
        adapter_adapter.manager = temp_manager
        self.assertIs(adapter_adapter.manager, temp_manager)
        self.assertIs(adapter.manager, temp_manager)
        self.assertIs(self.logger.manager, temp_manager)
    finally:
        adapter_adapter.manager = orig_manager
    self.assertIs(adapter_adapter.manager, orig_manager)
    self.assertIs(adapter.manager, orig_manager)
    self.assertIs(self.logger.manager, orig_manager)
