import pycuda.driver as cuda

# Initialize CUDA
cuda.init()

from pycuda.tools import make_default_context
global context
context = make_default_context()
device = context.get_device()

def _finish_up():
    global context
    print "pycuda.autoinit: _finish_up()"
    print "pycuda.autoinit: context.pop()"
    context.pop()
    context = None

    from pycuda.tools import clear_context_caches
    print "pycuda.autoinit: clear_context_caches()"
    clear_context_caches()

import atexit
atexit.register(_finish_up)
