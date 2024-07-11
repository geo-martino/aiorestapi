from simple import *

# PART 1

from aiorequestful.cache.backend import SQLiteCache

cache = SQLiteCache.connect_with_in_memory_db()
request_handler = RequestHandler.create(cache=cache)

task = send_get_request(request_handler, url=api_url)
result = asyncio.run(task)

print(result)