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
from google.cloud.datalabeling_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.data_labeling_service import (
    DataLabelingServiceAsyncClient,
    DataLabelingServiceClient,
)
from .types.annotation import (
    Annotation,
    AnnotationMetadata,
    AnnotationSentiment,
    AnnotationSource,
    AnnotationType,
    AnnotationValue,
    BoundingPoly,
    ImageBoundingPolyAnnotation,
    ImageClassificationAnnotation,
    ImagePolylineAnnotation,
    ImageSegmentationAnnotation,
    NormalizedBoundingPoly,
    NormalizedPolyline,
    NormalizedVertex,
    ObjectTrackingFrame,
    OperatorMetadata,
    Polyline,
    SequentialSegment,
    TextClassificationAnnotation,
    TextEntityExtractionAnnotation,
    TimeSegment,
    Vertex,
    VideoClassificationAnnotation,
    VideoEventAnnotation,
    VideoObjectTrackingAnnotation,
)
from .types.annotation_spec_set import AnnotationSpec, AnnotationSpecSet
from .types.data_labeling_service import (
    CreateAnnotationSpecSetRequest,
    CreateDatasetRequest,
    CreateEvaluationJobRequest,
    CreateInstructionRequest,
    DeleteAnnotatedDatasetRequest,
    DeleteAnnotationSpecSetRequest,
    DeleteDatasetRequest,
    DeleteEvaluationJobRequest,
    DeleteInstructionRequest,
    ExportDataRequest,
    GetAnnotatedDatasetRequest,
    GetAnnotationSpecSetRequest,
    GetDataItemRequest,
    GetDatasetRequest,
    GetEvaluationJobRequest,
    GetEvaluationRequest,
    GetExampleRequest,
    GetInstructionRequest,
    ImportDataRequest,
    LabelImageRequest,
    LabelTextRequest,
    LabelVideoRequest,
    ListAnnotatedDatasetsRequest,
    ListAnnotatedDatasetsResponse,
    ListAnnotationSpecSetsRequest,
    ListAnnotationSpecSetsResponse,
    ListDataItemsRequest,
    ListDataItemsResponse,
    ListDatasetsRequest,
    ListDatasetsResponse,
    ListEvaluationJobsRequest,
    ListEvaluationJobsResponse,
    ListExamplesRequest,
    ListExamplesResponse,
    ListInstructionsRequest,
    ListInstructionsResponse,
    PauseEvaluationJobRequest,
    ResumeEvaluationJobRequest,
    SearchEvaluationsRequest,
    SearchEvaluationsResponse,
    SearchExampleComparisonsRequest,
    SearchExampleComparisonsResponse,
    UpdateEvaluationJobRequest,
)
from .types.data_payloads import ImagePayload, TextPayload, VideoPayload, VideoThumbnail
from .types.dataset import (
    AnnotatedDataset,
    AnnotatedDatasetMetadata,
    BigQuerySource,
    ClassificationMetadata,
    DataItem,
    Dataset,
    DataType,
    Example,
    GcsDestination,
    GcsFolderDestination,
    GcsSource,
    InputConfig,
    LabelStats,
    OutputConfig,
    TextMetadata,
)
from .types.evaluation import (
    BoundingBoxEvaluationOptions,
    ClassificationMetrics,
    ConfusionMatrix,
    Evaluation,
    EvaluationConfig,
    EvaluationMetrics,
    ObjectDetectionMetrics,
    PrCurve,
)
from .types.evaluation_job import (
    Attempt,
    EvaluationJob,
    EvaluationJobAlertConfig,
    EvaluationJobConfig,
)
from .types.human_annotation_config import (
    BoundingPolyConfig,
    EventConfig,
    HumanAnnotationConfig,
    ImageClassificationConfig,
    ObjectDetectionConfig,
    ObjectTrackingConfig,
    PolylineConfig,
    SegmentationConfig,
    SentimentConfig,
    StringAggregationType,
    TextClassificationConfig,
    TextEntityExtractionConfig,
    VideoClassificationConfig,
)
from .types.instruction import CsvInstruction, Instruction, PdfInstruction
from .types.operations import (
    CreateInstructionMetadata,
    ExportDataOperationMetadata,
    ExportDataOperationResponse,
    ImportDataOperationMetadata,
    ImportDataOperationResponse,
    LabelImageBoundingBoxOperationMetadata,
    LabelImageBoundingPolyOperationMetadata,
    LabelImageClassificationOperationMetadata,
    LabelImageOrientedBoundingBoxOperationMetadata,
    LabelImagePolylineOperationMetadata,
    LabelImageSegmentationOperationMetadata,
    LabelOperationMetadata,
    LabelTextClassificationOperationMetadata,
    LabelTextEntityExtractionOperationMetadata,
    LabelVideoClassificationOperationMetadata,
    LabelVideoEventOperationMetadata,
    LabelVideoObjectDetectionOperationMetadata,
    LabelVideoObjectTrackingOperationMetadata,
)

__all__ = (
    "DataLabelingServiceAsyncClient",
    "AnnotatedDataset",
    "AnnotatedDatasetMetadata",
    "Annotation",
    "AnnotationMetadata",
    "AnnotationSentiment",
    "AnnotationSource",
    "AnnotationSpec",
    "AnnotationSpecSet",
    "AnnotationType",
    "AnnotationValue",
    "Attempt",
    "BigQuerySource",
    "BoundingBoxEvaluationOptions",
    "BoundingPoly",
    "BoundingPolyConfig",
    "ClassificationMetadata",
    "ClassificationMetrics",
    "ConfusionMatrix",
    "CreateAnnotationSpecSetRequest",
    "CreateDatasetRequest",
    "CreateEvaluationJobRequest",
    "CreateInstructionMetadata",
    "CreateInstructionRequest",
    "CsvInstruction",
    "DataItem",
    "DataLabelingServiceClient",
    "DataType",
    "Dataset",
    "DeleteAnnotatedDatasetRequest",
    "DeleteAnnotationSpecSetRequest",
    "DeleteDatasetRequest",
    "DeleteEvaluationJobRequest",
    "DeleteInstructionRequest",
    "Evaluation",
    "EvaluationConfig",
    "EvaluationJob",
    "EvaluationJobAlertConfig",
    "EvaluationJobConfig",
    "EvaluationMetrics",
    "EventConfig",
    "Example",
    "ExportDataOperationMetadata",
    "ExportDataOperationResponse",
    "ExportDataRequest",
    "GcsDestination",
    "GcsFolderDestination",
    "GcsSource",
    "GetAnnotatedDatasetRequest",
    "GetAnnotationSpecSetRequest",
    "GetDataItemRequest",
    "GetDatasetRequest",
    "GetEvaluationJobRequest",
    "GetEvaluationRequest",
    "GetExampleRequest",
    "GetInstructionRequest",
    "HumanAnnotationConfig",
    "ImageBoundingPolyAnnotation",
    "ImageClassificationAnnotation",
    "ImageClassificationConfig",
    "ImagePayload",
    "ImagePolylineAnnotation",
    "ImageSegmentationAnnotation",
    "ImportDataOperationMetadata",
    "ImportDataOperationResponse",
    "ImportDataRequest",
    "InputConfig",
    "Instruction",
    "LabelImageBoundingBoxOperationMetadata",
    "LabelImageBoundingPolyOperationMetadata",
    "LabelImageClassificationOperationMetadata",
    "LabelImageOrientedBoundingBoxOperationMetadata",
    "LabelImagePolylineOperationMetadata",
    "LabelImageRequest",
    "LabelImageSegmentationOperationMetadata",
    "LabelOperationMetadata",
    "LabelStats",
    "LabelTextClassificationOperationMetadata",
    "LabelTextEntityExtractionOperationMetadata",
    "LabelTextRequest",
    "LabelVideoClassificationOperationMetadata",
    "LabelVideoEventOperationMetadata",
    "LabelVideoObjectDetectionOperationMetadata",
    "LabelVideoObjectTrackingOperationMetadata",
    "LabelVideoRequest",
    "ListAnnotatedDatasetsRequest",
    "ListAnnotatedDatasetsResponse",
    "ListAnnotationSpecSetsRequest",
    "ListAnnotationSpecSetsResponse",
    "ListDataItemsRequest",
    "ListDataItemsResponse",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListEvaluationJobsRequest",
    "ListEvaluationJobsResponse",
    "ListExamplesRequest",
    "ListExamplesResponse",
    "ListInstructionsRequest",
    "ListInstructionsResponse",
    "NormalizedBoundingPoly",
    "NormalizedPolyline",
    "NormalizedVertex",
    "ObjectDetectionConfig",
    "ObjectDetectionMetrics",
    "ObjectTrackingConfig",
    "ObjectTrackingFrame",
    "OperatorMetadata",
    "OutputConfig",
    "PauseEvaluationJobRequest",
    "PdfInstruction",
    "Polyline",
    "PolylineConfig",
    "PrCurve",
    "ResumeEvaluationJobRequest",
    "SearchEvaluationsRequest",
    "SearchEvaluationsResponse",
    "SearchExampleComparisonsRequest",
    "SearchExampleComparisonsResponse",
    "SegmentationConfig",
    "SentimentConfig",
    "SequentialSegment",
    "StringAggregationType",
    "TextClassificationAnnotation",
    "TextClassificationConfig",
    "TextEntityExtractionAnnotation",
    "TextEntityExtractionConfig",
    "TextMetadata",
    "TextPayload",
    "TimeSegment",
    "UpdateEvaluationJobRequest",
    "Vertex",
    "VideoClassificationAnnotation",
    "VideoClassificationConfig",
    "VideoEventAnnotation",
    "VideoObjectTrackingAnnotation",
    "VideoPayload",
    "VideoThumbnail",
)
