from aiohttp import web
import aiohttp_jinja2
import jinja2
from middlewares import setup_middlewares
from settings import config, BASE_DIR
from routes import setup_routes
from db import pg_context

import sys, asyncio

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))
setup_routes(app)
setup_middlewares(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)