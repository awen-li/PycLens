# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: TrivialTests_test___all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for module in ('request', 'response', 'parse', 'error', 'robotparser'):
        context = {}
        exec('from urllib.%s import *' % module, context)
        del context['__builtins__']
        if module == 'request' and os.name == 'nt':
            (u, p) = (context.pop('url2pathname'), context.pop('pathname2url'))
            self.assertEqual(u.__module__, 'nturl2path')
            self.assertEqual(p.__module__, 'nturl2path')
        for (k, v) in context.items():
            self.assertEqual(v.__module__, 'urllib.%s' % module, "%r is exposed in 'urllib.%s' but defined in %r" % (k, module, v.__module__))
