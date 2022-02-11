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
# Snippet for AnalyzeContent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_generated_dialogflow_v2_Participants_AnalyzeContent_async]
from google.cloud import dialogflow_v2


async def sample_analyze_content():
    # Create a client
    client = dialogflow_v2.ParticipantsAsyncClient()

    # Initialize request argument(s)
    text_input = dialogflow_v2.TextInput()
    text_input.text = "text_value"
    text_input.language_code = "language_code_value"

    request = dialogflow_v2.AnalyzeContentRequest(
        text_input=text_input,
        participant="participant_value",
    )

    # Make the request
    response = await client.analyze_content(request=request)

    # Handle the response
    print(response)

# [END dialogflow_generated_dialogflow_v2_Participants_AnalyzeContent_async]
