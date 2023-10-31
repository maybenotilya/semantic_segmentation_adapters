# Copyright (c) 2022, Ilya Syresenkov, Kirill Ivanov and Anastasiia Kornilova
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

import numpy as np

from abc import ABC, abstractmethod


class AdapterBase(ABC):
    """Adapter accepts image as numpy array and returns mask as image in numpy array"""

    def process(self, image):
        # image - RGB
        image = self._transform_image(image)
        model = self._build_model()
        raw_predictions = self._process(model, image)
        predictions = self._postprocess_predictions(raw_predictions)
        return predictions

    @abstractmethod
    def _transform_image(self, image: np.ndarray):
        pass

    @abstractmethod
    def _process(self, model, image):
        pass

    @abstractmethod
    def _build_model(self):
        pass

    @abstractmethod
    def _postprocess_predictions(self, raw_predictions):
        pass
