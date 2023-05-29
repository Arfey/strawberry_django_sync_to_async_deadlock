from asgiref.sync import sync_to_async
import strawberry
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field
    async def with_deadlock(self, info: Info) -> str:
        return await sync_to_async(lambda: 'with_deadlock', thread_sensitive=True)()

    @strawberry.field
    async def without_deadlock(self, info: Info) -> str:
        return await sync_to_async(lambda: 'without_deadlock', thread_sensitive=False)()

    @strawberry.field
    async def without_deadlock_v2(self, info: Info) -> str:
        return 'without_deadlock_v2'


schema = strawberry.Schema(Query)
