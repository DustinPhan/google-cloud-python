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
# Snippet for ListSettings
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-resource-settings


# [START resourcesettings_generated_resourcesettings_v1_ResourceSettingsService_ListSettings_async]
from google.cloud import resourcesettings_v1


async def sample_list_settings():
    # Create a client
    client = resourcesettings_v1.ResourceSettingsServiceAsyncClient()

    # Initialize request argument(s)
    request = resourcesettings_v1.ListSettingsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_settings(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END resourcesettings_generated_resourcesettings_v1_ResourceSettingsService_ListSettings_async]
