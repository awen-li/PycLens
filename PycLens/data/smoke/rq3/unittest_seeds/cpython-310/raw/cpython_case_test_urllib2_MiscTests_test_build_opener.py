# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: MiscTests_test_build_opener

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyHTTPHandler(urllib.request.HTTPHandler):
        pass

    class FooHandler(urllib.request.BaseHandler):

        def foo_open(self):
            pass

    class BarHandler(urllib.request.BaseHandler):

        def bar_open(self):
            pass
    build_opener = urllib.request.build_opener
    o = build_opener(FooHandler, BarHandler)
    self.opener_has_handler(o, FooHandler)
    self.opener_has_handler(o, BarHandler)
    o = build_opener(FooHandler, BarHandler())
    self.opener_has_handler(o, FooHandler)
    self.opener_has_handler(o, BarHandler)
    o = build_opener(MyHTTPHandler)
    self.opener_has_handler(o, MyHTTPHandler)
    o = build_opener()
    self.opener_has_handler(o, urllib.request.HTTPHandler)
    o = build_opener(urllib.request.HTTPHandler)
    self.opener_has_handler(o, urllib.request.HTTPHandler)
    o = build_opener(urllib.request.HTTPHandler())
    self.opener_has_handler(o, urllib.request.HTTPHandler)

    class MyOtherHTTPHandler(urllib.request.HTTPHandler):
        pass
    o = build_opener(MyHTTPHandler, MyOtherHTTPHandler)
    self.opener_has_handler(o, MyHTTPHandler)
    self.opener_has_handler(o, MyOtherHTTPHandler)
