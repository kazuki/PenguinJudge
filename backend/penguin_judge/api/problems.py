from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
import sqlalchemy as sa

router = APIRouter()


@router.get('')
async def list_problems(contest_id: str) -> Any:
    raise NotImplementedError


@router.post('')
async def create_problem(contest_id: str) -> Any:
    raise NotImplementedError


@router.get('/{problem_id}')
async def get_problem(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError


@router.patch('/{problem_id}')
async def update_problem(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError


@router.delete('/{problem_id}')
async def delete_problem(contest_id: str, problem_id: str) -> Any:
    raise NotImplementedError
