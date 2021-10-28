"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("4472818"))
API_HASH = getenv("fe5f0e7c21f255af922ba4d3b2c74967")
BOT_TOKEN = getenv("2057960481:AAEPQhcVoEbKB8N9T76UCk2ptclPOa6YYzY")
SESSION_STRING = getenv("AQBFs6QtRfrIFtIBNIaaLUCVosucjzbUQ4O2JYSaZCbe78a2pP-sbOCgbRRnbMyP97qdjtleXPOp7UMegypw5bQN2ReQH8IwgingB75oHI09-kTEMZKVAcI4F7EigGCTc-db9yJizPw9Sw5HmS0CAek1VNzK3KPC9diEzAVlRlOg0aOPmk-Rad46TBuWmMIntvRogmk-fWPJ5uTHD1hdWqPKTr4PsBd8cwjgix43wfNukOn2gn0LpDb1S5jJePgckWY4VefbVnjzKLo1FJgBT0vUImZOhvTc5-G1IhLI_2HoNh-blPn2e4MXXUQ3ZP82IKa9qTeY4h5jD9I-HskA-6D_ewnIUAA")
SUPPORT_GROUP = getenv("KumikoSetsuko")
UPDATES_CHANNEL = getenv("KumikoSetsuko")
ASSISTANT_NAME = getenv("@Adams_A10")
SUDO_USERS = list(map(int, getenv("1759889581").split()))
REPLY_MESSAGE = getenv("This is mine")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
