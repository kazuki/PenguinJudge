from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
import sqlalchemy as sa

router = APIRouter()


@router.get('')
async def list_submissions(contest_id: str) -> Any:
    raise NotImplementedError


@router.post('')
async def post_submission(contest_id: str) -> Any:
    raise NotImplementedError


@router.get('/{submission_id}')
async def get_submission(contest_id: str, submission_id: str) -> Any:
    raise NotImplementedError
