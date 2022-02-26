# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for GetUserFeedback
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataqna


# [START dataqna_v1alpha_generated_QuestionService_GetUserFeedback_sync]
from google.cloud import dataqna_v1alpha


def sample_get_user_feedback():
    # Create a client
    client = dataqna_v1alpha.QuestionServiceClient()

    # Initialize request argument(s)
    request = dataqna_v1alpha.GetUserFeedbackRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_user_feedback(request=request)

    # Handle the response
    print(response)

# [END dataqna_v1alpha_generated_QuestionService_GetUserFeedback_sync]
