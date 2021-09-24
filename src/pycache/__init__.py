import sys

from .cache import *
from .lru import *

if sys.version_info[:2] >= (3, 6):
    from importlib.metadata import (PackageNotFoundError,  # pragma: no cover
                                    version)
else:
    from importlib_metadata import (PackageNotFoundError,  # pragma: no cover
                                    version)

try:
    dist_name = "pycache"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
