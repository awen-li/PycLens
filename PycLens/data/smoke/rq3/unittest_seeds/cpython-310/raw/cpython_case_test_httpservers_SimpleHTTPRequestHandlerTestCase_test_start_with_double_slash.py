# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPRequestHandlerTestCase_test_start_with_double_slash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = self.handler_1.translate_path('//filename')
    self.assertEqual(path, self.translated_1)
    path = self.handler_2.translate_path('//filename')
    self.assertEqual(path, self.translated_2)
    path = self.handler_3.translate_path('//filename')
    self.assertEqual(path, self.translated_3)
    path = self.handler_1.translate_path('//filename?foo=bar')
    self.assertEqual(path, self.translated_1)
    path = self.handler_2.translate_path('//filename?foo=bar')
    self.assertEqual(path, self.translated_2)
    path = self.handler_3.translate_path('//filename?foo=bar')
    self.assertEqual(path, self.translated_3)
