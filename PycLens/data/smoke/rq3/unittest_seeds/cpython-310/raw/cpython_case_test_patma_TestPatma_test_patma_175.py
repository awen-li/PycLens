# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_175

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def http_error(status):
        match status:
            case 400:
                return 'Bad request'
            case 401 | 403 | 404:
                return 'Not allowed'
            case 418:
                return "I'm a teapot"
    self.assertEqual(http_error(400), 'Bad request')
    self.assertEqual(http_error(401), 'Not allowed')
    self.assertEqual(http_error(403), 'Not allowed')
    self.assertEqual(http_error(404), 'Not allowed')
    self.assertEqual(http_error(418), "I'm a teapot")
    self.assertIs(http_error(123), None)
    self.assertIs(http_error('400'), None)
    self.assertIs(http_error(401 | 403 | 404), None)
