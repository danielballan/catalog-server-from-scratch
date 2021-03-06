from dataclasses import dataclass
from typing import Dict, Tuple

from .array import ArrayStructure


@dataclass
class VariableStructure:
    dims: Tuple[str]
    data: ArrayStructure
    attrs: Dict  # TODO Use JSONSerializableDict
    # TODO Variables also have `encoding`. Do we want to carry that as well?

    @classmethod
    def from_json(cls, structure):
        return cls(
            dims=structure["dims"],
            data=ArrayStructure.from_json(structure["data"]),
            attrs=structure["attrs"],
        )


@dataclass
class DataArrayStructure:
    variable: VariableStructure
    coords: Dict[str, VariableStructure]
    name: str

    @classmethod
    def from_json(cls, structure):
        return cls(
            variable=VariableStructure.from_json(structure["variable"]),
            coords={
                key: VariableStructure.from_json(value)
                for key, value in structure["coords"].items()
            },
            name=structure["name"],
        )


@dataclass
class DatasetStructure:
    data_vars: Dict[str, DataArrayStructure]
    coords: Dict[str, VariableStructure]
    attrs: Dict  # TODO Use JSONSerializableDict

    @classmethod
    def from_json(cls, structure):
        return cls(
            data_vars={
                key: DataArrayStructure.from_json(value)
                for key, value in structure["data_vars"].items()
            },
            coords={
                key: VariableStructure.from_json(value)
                for key, value in structure["coords"].items()
            },
            attrs=structure["attrs"],
        )


# TODO Also support zarr for encoding.
