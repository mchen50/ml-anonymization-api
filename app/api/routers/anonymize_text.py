import spacy

from copy import deepcopy
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
from app.api.models.request import UserRequestIn
from app.api.models.response import EntitiesOut


def load_models() -> dict[str, spacy.Language]:
    """
    load the models and put them in a dictionary

    Returns:
        dict: loaded models
    """
    models = {
        "en_sm": spacy.load("en_core_web_sm"),
    }
    print("models loaded")
    return models


models = load_models()

router = APIRouter(
    prefix="/anonymize",
    tags=["anonymize"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=EntitiesOut)
async def anonymize_text(user_request: UserRequestIn):
    text = user_request.text
    try:
        model = match_model_from_request(user_request=user_request)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An error occured when matching model from request: {str(e)}",
        )

    doc = model(text)

    entities = [
        {
            "start": ent.start_char,
            "end": ent.end_char,
            "type": ent.label_,
            "text": ent.text,
        }
        for ent in doc.ents
    ]

    anonymized_text = anonymize_text_with_entities(text, entities)
    return EntitiesOut(entities=entities, anonymized_text=anonymized_text)


def match_model_from_request(user_request: UserRequestIn) -> spacy.language:
    language = user_request.model_language
    model_size = user_request.model_size

    model_key = language + "_" + model_size

    if model_key not in models:
        raise Exception(f"Failed to find model with {model_key}.")

    return models[model_key]


def anonymize_text_with_entities(text: str, entities: List[Dict[str, Any]]) -> str:
    anonymized_text = list(deepcopy(text))

    for entity in entities:
        start = entity["start"]
        end = entity["end"]
        anonymized_text[start:end] = "X" * (end - start)

    anonymized_text = "".join(anonymized_text)
    return anonymized_text
