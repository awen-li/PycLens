import dis
import importlib.machinery
import marshal
import sys

path = sys.argv[1]
data = open(path, "rb").read()

code = None
try:
    code = importlib.machinery.SourcelessFileLoader("pybcsec_rq3_seed", path).get_code("pybcsec_rq3_seed")
except BaseException:
    for offset in (16, 12, 8):
        try:
            obj = marshal.loads(data[offset:])
        except BaseException:
            continue
        if hasattr(obj, "co_code"):
            code = obj
            break

if code is not None:
    list(dis.Bytecode(code))
    marshal.dumps(code)
    namespace = {"__name__": "pybcsec_rq3_seed"}
    exec(code, namespace, namespace)
    target = namespace.get("__pybcsec_seed__")
    if callable(target):
        result = target()
        close = getattr(result, "close", None)
        if hasattr(result, "__await__") and callable(close):
            close()
