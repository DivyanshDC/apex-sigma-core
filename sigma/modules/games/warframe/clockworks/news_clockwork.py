# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2017  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio

from sigma.modules.games.warframe.commons.cycles.generic import send_to_channels
from sigma.modules.games.warframe.commons.parsers.news_parser import get_news_data, generate_news_embed


async def news_clockwork(ev):
    ev.bot.loop.create_task(news_cycler(ev))


async def news_cycler(ev):
    while ev.bot.is_ready():
        try:
            news = await get_news_data(ev.db)
            if news:
                response = generate_news_embed(news)
                await send_to_channels(ev, response, 'WarframeNewsChannel')
        except Exception:
            pass
        await asyncio.sleep(2)
