from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
import sqlalchemy as sa

router = APIRouter()


@router.get('')
async def list_rankings(contest_id: str) -> Any:
    raise NotImplementedError
