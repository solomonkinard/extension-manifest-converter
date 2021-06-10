# Copyright 2021 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import Modifier
from . import Logger

class ContentSecurityPolicyModifier(Modifier):
  def _mv2(self):
    pass

  def _mv3(self):
    candidate = {}
    manifest = self.wrapper.manifest
    key = 'content_security_policy'
    if key in manifest:
      value = manifest[key]
      candidate["extension_pages"] = value
    if "sandbox" in manifest and key in manifest["sandbox"]:
      candidate["sandbox"] = manifest["sandbox"]
    if candidate:
      Logger().log("Changing CSP (content_security_policy) in manifest.json")
      Logger().log("Valid CSP directives for {script,object,worker}-src are {self,none,localhost,127.0.0.1}.")

    self.wrapper.manifest[key] = candidate
    self.writeManifest()
