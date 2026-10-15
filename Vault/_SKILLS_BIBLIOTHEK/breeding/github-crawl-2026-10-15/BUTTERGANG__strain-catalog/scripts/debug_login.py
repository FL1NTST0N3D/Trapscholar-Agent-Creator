"""Debug the login 500: run the exact login flow in-process."""
import asyncio, traceback, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

async def test_login_flow():
    from backend.database import async_session
    from backend.services.auth import create_session
    from backend.models.user import User
    from sqlalchemy import select

    async with async_session() as db:
        result = await db.execute(select(User).where(User.email == "dogfood@test.local"))
        user = result.scalar_one_or_none()
        print("user:", user.username if user else None)
        try:
            token = await create_session(db, user.id, ttl_hours=24)
            print("session created:", token[:12])
        except Exception:
            traceback.print_exc()

asyncio.run(test_login_flow())