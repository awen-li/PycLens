# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_eval_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actions = []

    def make_decorator(tag):
        actions.append('makedec' + tag)

        def decorate(func):
            actions.append('calldec' + tag)
            return func
        return decorate

    class NameLookupTracer(object):

        def __init__(self, index):
            self.index = index

        def __getattr__(self, fname):
            if fname == 'make_decorator':
                (opname, res) = ('evalname', make_decorator)
            elif fname == 'arg':
                (opname, res) = ('evalargs', str(self.index))
            else:
                assert False, 'Unknown attrname %s' % fname
            actions.append('%s%d' % (opname, self.index))
            return res
    (c1, c2, c3) = map(NameLookupTracer, [1, 2, 3])
    expected_actions = ['evalname1', 'evalargs1', 'makedec1', 'evalname2', 'evalargs2', 'makedec2', 'evalname3', 'evalargs3', 'makedec3', 'calldec3', 'calldec2', 'calldec1']
    actions = []

    @c1.make_decorator(c1.arg)
    @c2.make_decorator(c2.arg)
    @c3.make_decorator(c3.arg)
    def foo():
        return 42
    self.assertEqual(foo(), 42)
    self.assertEqual(actions, expected_actions)
    actions = []

    def bar():
        return 42
    bar = c1.make_decorator(c1.arg)(c2.make_decorator(c2.arg)(c3.make_decorator(c3.arg)(bar)))
    self.assertEqual(bar(), 42)
    self.assertEqual(actions, expected_actions)
