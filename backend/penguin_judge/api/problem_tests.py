from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
import sqlalchemy as sa

router = APIRouter()


@router.get('')
async def list_tests(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError


@router.put('')
async def upload_test_dataset(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError


@router.get('/{test_id}/in')
async def get_test_input_data(contest_id: str, problem_id: str, test_id: str) -> Any:
    raise NotImplementedError


@router.get('/{test_id}/out')
async def get_test_output_data(contest_id: str, problem_id: str, test_id: str) -> Any:
    raise NotImplementedError
