import sys

__appname__ = "labelme"

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
__version__ = "4.5.6"

QT4 = "4"
QT5 = "5"

PY2 = sys.version[0] == "2"
PY3 = sys.version[0] == "3"
del sys

