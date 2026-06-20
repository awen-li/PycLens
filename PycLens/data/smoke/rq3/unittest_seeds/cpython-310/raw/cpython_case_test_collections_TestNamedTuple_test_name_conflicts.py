# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_name_conflicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = namedtuple('T', 'itemgetter property self cls tuple')
    t = T(1, 2, 3, 4, 5)
    self.assertEqual(t, (1, 2, 3, 4, 5))
    newt = t._replace(itemgetter=10, property=20, self=30, cls=40, tuple=50)
    self.assertEqual(newt, (10, 20, 30, 40, 50))
    words = {'Alias', 'At', 'AttributeError', 'Build', 'Bypass', 'Create', 'Encountered', 'Expected', 'Field', 'For', 'Got', 'Helper', 'IronPython', 'Jython', 'KeyError', 'Make', 'Modify', 'Note', 'OrderedDict', 'Point', 'Return', 'Returns', 'Type', 'TypeError', 'Used', 'Validate', 'ValueError', 'Variables', 'a', 'accessible', 'add', 'added', 'all', 'also', 'an', 'arg_list', 'args', 'arguments', 'automatically', 'be', 'build', 'builtins', 'but', 'by', 'cannot', 'class_namespace', 'classmethod', 'cls', 'collections', 'convert', 'copy', 'created', 'creation', 'd', 'debugging', 'defined', 'dict', 'dictionary', 'doc', 'docstring', 'docstrings', 'duplicate', 'effect', 'either', 'enumerate', 'environments', 'error', 'example', 'exec', 'f', 'f_globals', 'field', 'field_names', 'fields', 'formatted', 'frame', 'function', 'functions', 'generate', 'get', 'getter', 'got', 'greater', 'has', 'help', 'identifiers', 'index', 'indexable', 'instance', 'instantiate', 'interning', 'introspection', 'isidentifier', 'isinstance', 'itemgetter', 'iterable', 'join', 'keyword', 'keywords', 'kwds', 'len', 'like', 'list', 'map', 'maps', 'message', 'metadata', 'method', 'methods', 'module', 'module_name', 'must', 'name', 'named', 'namedtuple', 'namedtuple_', 'names', 'namespace', 'needs', 'new', 'nicely', 'num_fields', 'number', 'object', 'of', 'operator', 'option', 'p', 'particular', 'pickle', 'pickling', 'plain', 'pop', 'positional', 'property', 'r', 'regular', 'rename', 'replace', 'replacing', 'repr', 'repr_fmt', 'representation', 'result', 'reuse_itemgetter', 's', 'seen', 'self', 'sequence', 'set', 'side', 'specified', 'split', 'start', 'startswith', 'step', 'str', 'string', 'strings', 'subclass', 'sys', 'targets', 'than', 'the', 'their', 'this', 'to', 'tuple', 'tuple_new', 'type', 'typename', 'underscore', 'unexpected', 'unpack', 'up', 'use', 'used', 'user', 'valid', 'values', 'variable', 'verbose', 'where', 'which', 'work', 'x', 'y', 'z', 'zip'}
    T = namedtuple('T', words)
    values = tuple(range(len(words)))
    t = T(*values)
    self.assertEqual(t, values)
    t = T(**dict(zip(T._fields, values)))
    self.assertEqual(t, values)
    t = T._make(values)
    self.assertEqual(t, values)
    repr(t)
    self.assertEqual(t._asdict(), dict(zip(T._fields, values)))
    t = T._make(values)
    newvalues = tuple((v * 10 for v in values))
    newt = t._replace(**dict(zip(T._fields, newvalues)))
    self.assertEqual(newt, newvalues)
    self.assertEqual(T._fields, tuple(words))
    self.assertEqual(t.__getnewargs__(), values)
