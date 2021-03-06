import pkg_resources
import sys

if sys.version_info.major < 3:
    raise EnvironmentError("Python 3 is required")

from web3.account import Account  # noqa: E402
from web3.main import Web3  # noqa: E402
from web3.providers.rpc import (  # noqa: E402
    HTTPProvider,
)
from web3.providers.tester import (  # noqa: E402
    TestRPCProvider,
    EthereumTesterProvider,
)
from web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "TestRPCProvider",
    "EthereumTesterProvider",
    "Account",
]
