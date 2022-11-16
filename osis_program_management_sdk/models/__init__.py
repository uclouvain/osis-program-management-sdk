# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_program_management_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_program_management_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_program_management_sdk.model.array_of_program_tree_prerequisites import ArrayOfProgramTreePrerequisites
from osis_program_management_sdk.model.error import Error
from osis_program_management_sdk.model.node_base import NodeBase
from osis_program_management_sdk.model.program_tree_prerequisites import ProgramTreePrerequisites
from osis_program_management_sdk.model.programme import Programme
