# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_close_connection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handle_one_request():
        self.handler.close_connection = next(close_values)
    self.handler.handle_one_request = handle_one_request
    close_values = iter((True,))
    self.handler.handle()
    self.assertRaises(StopIteration, next, close_values)
    close_values = iter((False, False, True))
    self.handler.handle()
    self.assertRaises(StopIteration, next, close_values)
