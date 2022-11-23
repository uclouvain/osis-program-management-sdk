
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.mini_trainings_api import MiniTrainingsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_program_management_sdk.api.mini_trainings_api import MiniTrainingsApi
from osis_program_management_sdk.api.programme_api import ProgrammeApi
from osis_program_management_sdk.api.trainings_api import TrainingsApi
