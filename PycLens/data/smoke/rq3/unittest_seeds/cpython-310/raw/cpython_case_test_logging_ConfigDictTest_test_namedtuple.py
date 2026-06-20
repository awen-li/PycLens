# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_namedtuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from collections import namedtuple

    class MyHandler(logging.StreamHandler):

        def __init__(self, resource, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.resource: namedtuple = resource

        def emit(self, record):
            record.msg += f' {self.resource.type}'
            return super().emit(record)
    Resource = namedtuple('Resource', ['type', 'labels'])
    resource = Resource(type='my_type', labels=['a'])
    config = {'version': 1, 'handlers': {'myhandler': {'()': MyHandler, 'resource': resource}}, 'root': {'level': 'INFO', 'handlers': ['myhandler']}}
    with support.captured_stderr() as stderr:
        self.apply_config(config)
        logging.info('some log')
    self.assertEqual(stderr.getvalue(), 'some log my_type\n')
