from __future__ import annotations
import bentoml
import numpy as np
import bentoml.sklearn
from pydantic import BaseModel,Field


model = bentoml.sklearn.load_model("consommation_model:latest")


model_ref = bentoml.sklearn.get("consommation_model:latest")
feature_names = model_ref.custom_objects.get("feature_names", ["natural_gas_binary", "LargestPropertyUseTypeGFA", "PropertyGFATotal","electricity_binary","ENERGYSTARScore","building_age","NumberofFloors","PropertyGFABuilding"])


class BuildingData(BaseModel):
    natural_gas_binary: int = Field(..., description="0 = low gas use, 1 = high gas use", ge=0, le=1)
    LargestPropertyUseTypeGFA: float = Field(..., description="Electricity consumption in kBtu", gt=0)
    PropertyGFATotal: int = Field(..., description="total property surface", ge=0)
    electricity_binary: int = Field(..., description="0 = low electricity use, 1 = high electricity use", ge=0, le=1)
    PropertyGFABuilding: int = Field(..., description="property building surface", ge=0)
    ENERGYSTARScore: int = Field(..., description="energy score from 0 - 100", ge=0)
    building_age: int = Field(..., description="building age", ge=0)
    NumberofFloors: int = Field(..., description="number of floors", ge=0)

@bentoml.service(resources={"cpu": "2"}, traffic={"timeout": 10})
class EnergyConsumptionService:
    def __init__(self):
        self.model = model
        self.feature_names = feature_names

    @bentoml.api
    def predict(self, data: BuildingData):
        raw_features = [
            data.natural_gas_binary,
            data.LargestPropertyUseTypeGFA,
            data.PropertyGFATotal,
            data.electricity_binary,
            data.PropertyGFABuilding,
            data.ENERGYSTARScore,
            data.building_age,
            data.NumberofFloors
        ]

        data = np.array([raw_features]) 
        prediction_log = self.model.predict(data)
        prediction = np.expm1(prediction_log)

        return {
            "TotalGHGEmissions": float(prediction[0][0]),
            "SiteEnergyUse(kBtu)": float(prediction[0][1]),
        }
