from typing import Literal, Union

from typing_extensions import Annotated

from pydantic import BaseModel, Field



class City(BaseModel):
    pet_type: Literal['city']
    city_name: str


class Forecast(BaseModel):
    pet_type: Literal['forecast']
    dog_name: str


Pet = Annotated[Union[City, Forecast], Field(discriminator='pet_type')]

print(BaseModel.schema_json(Pet))