# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "CustomTuningModel",
    },
)


class CustomTuningModel(proto.Message):
    r"""Metadata that describes a custom tuned model.

    Attributes:
        name (str):
            Required. The fully qualified resource name of the model.

            Format:
            ``projects/{project_number}/locations/{location}/collections/{collection}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}``
            model must be an alpha-numerical string with limit of 40
            characters.
        display_name (str):
            The display name of the model.
        model_version (int):
            The version of the model.
        model_state (google.cloud.discoveryengine_v1beta.types.CustomTuningModel.ModelState):
            The state that the model is in (e.g.``TRAINING`` or
            ``TRAINING_FAILED``).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp the Model was created at.
        training_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp the model training was initiated.
    """

    class ModelState(proto.Enum):
        r"""The state of the model.

        Values:
            MODEL_STATE_UNSPECIFIED (0):
                Default value.
            TRAINING_PAUSED (1):
                The model is in a paused training state.
            TRAINING (2):
                The model is currently training.
            TRAINING_COMPLETE (3):
                The model has successfully completed
                training.
            READY_FOR_SERVING (4):
                The model is ready for serving.
            TRAINING_FAILED (5):
                The model training failed.
        """
        MODEL_STATE_UNSPECIFIED = 0
        TRAINING_PAUSED = 1
        TRAINING = 2
        TRAINING_COMPLETE = 3
        READY_FOR_SERVING = 4
        TRAINING_FAILED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    model_version: int = proto.Field(
        proto.INT64,
        number=3,
    )
    model_state: ModelState = proto.Field(
        proto.ENUM,
        number=4,
        enum=ModelState,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    training_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
