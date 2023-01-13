# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "11628395"))
    API_HASH = os.getenv("API_HASH", "31a92babd97bd2a9c20907f516011f14")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5573121186:AAGpKaTW9C8b4vpQuPQbGkiNo9BR4t5DjAw")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "Movie Search Bot 🔍")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOMEBu4rufSwSOIor-YKW_DB9Q0MwThWfPLzAsmDpaP0dhh_8-mfNKt4VSUdOofTX8JtD09r8a4uhFLuWmItAL9m1_94xFBuZuozLPu0qlt51vnWl88L1N6_Hz9Iw_-ztFAdQ1pbJS6e-55ZKWTAJhX4VKZF7uBiZqDK5BhYmocYiLh0JJDsb0l8n59cytC2fQKvJMBawj01i_BAiWx2iXUivpM7dB931_6mcGVDdduvQ6L9BZ-mljnoWgiHFgJPOpJ0og_T24yLzZQXpVJtBpWuAf2oClzZ2-R82Le_Vp8-o_nDY3qAvduHH0mLooQmg8BY5P30NsPDOYIlTMaapy-iXy0w=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001875734327"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "HDFilmz4U_Searchbot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "1316494209"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Light Yagami")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "HDFilmsArea")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME", "HDFilmz4U")
    START_MSG = os.getenv("START_MSG", '''<b>👋Hi Buddy</b>⚡️\n\nWelcome to <b><u>Movies & Series Search Bot</u></b>🤗\n\n<i>I can give you direct mdisk & Vivdisk movies🎬 link🔗 to download. So simply send me the names.</i>''')
    START_PHOTO = os.getenv("START_PHOTO", "https://graph.org/file/ce69fe31b78cc88788035.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", '''<b>👋Hi Buddy</b>⚡️\n\nWelcome to <b><u>Movies & Series Search Bot</u></b>🤗\n\n<i>I can give you direct mdisk & Vivdisk movies🎬 link🔗 to download. So simply send me the names.</i>''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001840171626")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://lightyagm99:Lokesh666@cluster0.cbfutjd.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001566505151"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", "10"))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "HDFilmsArea")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "300"))
    MDISK_API = os.getenv("MDISK_API", "True")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''If you want to use this bot in your group then contact Me @Anime_Lover0_0''')
    ABOUT_HELP_TEXT = os.getenv("", '''''')
