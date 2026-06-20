# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: FileCookieJarTests_test_constructor_with_other_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass
    for type_ in (int, float, A):
        with self.subTest(filename=type_):
            with self.assertRaises(TypeError):
                instance = type_()
                c = LWPCookieJar(filename=instance)
