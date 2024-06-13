# Copyright (c) Materials Virtual Lab
# Distributed under the terms of the BSD License.

"""Define abstract base classes."""
from __future__ import annotations

from ._data import BaseDataSource
from ._describer import BaseDescriber, DummyDescriber, SequentialDescriber, describer_type
from ._feature_batch import get_feature_batch
from ._mixin import TargetScalerMixin
from ._model import BaseModel, KerasModel, SKLModel, is_keras_model, is_sklearn_model

__all__ = [
    "BaseDataSource",
    "BaseDescriber",
    "SequentialDescriber",
    "DummyDescriber",
    "BaseModel",
    "KerasModel",
    "SKLModel",
    "get_feature_batch",
    "describer_type",
    "is_keras_model",
    "is_sklearn_model",
    "TargetScalerMixin",
]