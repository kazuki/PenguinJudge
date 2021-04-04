from contextlib import asynccontextmanager
from typing import AsyncIterator, Tuple

import aiormq

from penguin_judge import config

JUDGE_QUEUE_NAME = 'judge_queue'


@asynccontextmanager
async def connect_mq() -> AsyncIterator[Tuple[aiormq.Connection, aiormq.Channel]]:
    conn = await aiormq.connect(config.mq_url)
    try:
        ch = await conn.channel()
        try:
            yield conn, ch
        finally:
            await ch.close()
    finally:
        await conn.close()
