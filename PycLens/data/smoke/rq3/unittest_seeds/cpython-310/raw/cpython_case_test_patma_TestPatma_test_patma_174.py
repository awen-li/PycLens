# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_174

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def http_error(status):
        match status:
            case 400:
                return 'Bad request'
            case 401:
                return 'Unauthorized'
            case 403:
                return 'Forbidden'
            case 404:
                return 'Not found'
            case 418:
                return "I'm a teapot"
            case _:
                return 'Something else'
    self.assertEqual(http_error(400), 'Bad request')
    self.assertEqual(http_error(401), 'Unauthorized')
    self.assertEqual(http_error(403), 'Forbidden')
    self.assertEqual(http_error(404), 'Not found')
    self.assertEqual(http_error(418), "I'm a teapot")
    self.assertEqual(http_error(123), 'Something else')
    self.assertEqual(http_error('400'), 'Something else')
    self.assertEqual(http_error(401 | 403 | 404), 'Something else')
