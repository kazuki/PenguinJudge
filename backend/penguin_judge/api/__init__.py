from typing import Any, List, Sequence, Tuple

from fastapi import FastAPI
from fastapi.routing import APIRoute

from .auth import router as auth_router
from .contests import router as contests_router
from .environments import router as env_router
from .user import router as user_router
from .users import router as users_router

ROUTES: Sequence[Tuple[str, Any, List[str]]] = (
    ('/auth', auth_router, ['auth']),
    ('/user', user_router, ['auth']),
    ('/users', users_router, ['users']),
    ('/environments', env_router, ['environments']),
    ('/contests', contests_router, ['contests']),
)

app = FastAPI()
for prefix, router, tags in ROUTES:
    app.include_router(router, prefix=prefix, tags=tags)

# configure "operation_id" from python function name
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
