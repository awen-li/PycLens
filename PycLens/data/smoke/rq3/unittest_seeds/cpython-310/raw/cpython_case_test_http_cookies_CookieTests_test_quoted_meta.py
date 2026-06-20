# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_quoted_meta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    C.load('Customer="WILE_E_COYOTE"; Version="1"; Path="/acme"')
    self.assertEqual(C['Customer'].value, 'WILE_E_COYOTE')
    self.assertEqual(C['Customer']['version'], '1')
    self.assertEqual(C['Customer']['path'], '/acme')
    self.assertEqual(C.output(['path']), 'Set-Cookie: Customer="WILE_E_COYOTE"; Path=/acme')
    self.assertEqual(C.js_output(), '\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "Customer=\\"WILE_E_COYOTE\\"; Path=/acme; Version=1";\n        // end hiding -->\n        </script>\n        ')
    self.assertEqual(C.js_output(['path']), '\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "Customer=\\"WILE_E_COYOTE\\"; Path=/acme";\n        // end hiding -->\n        </script>\n        ')
