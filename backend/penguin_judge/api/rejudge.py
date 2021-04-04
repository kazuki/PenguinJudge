from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
import sqlalchemy as sa

router = APIRouter()


@router.post('')
async def rejudge(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError
