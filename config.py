from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "4cbb616dea66bf2b8ea81c6bc571a8ce")
      API_ID = int(getenv("API_ID", "25066187"))
      AS_COPY = True if getenv("AS_COPY", False) == "`{file_name}`" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "7340350818:AAH9wWKksCVTy3yy2VkiCywv4XpnFYB1Wz8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002223535946:-1002157794804").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
