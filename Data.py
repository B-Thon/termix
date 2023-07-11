from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("انشاء جلسة", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجوع", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(

                "𝗦𝗘𝗖𝗨𝗥𝗘 𝗕𝗧𝗛𝗢𝗡", url="https://t.me/BThon"
            )
        ],
        [
            InlineKeyboardButton(" - طريقة الاستخدام؟ . ", callback_data="help"),
            InlineKeyboardButton(" - حول البوت . ", callback_data="about"),
        ],
        [InlineKeyboardButton("𝗗𝗘𝗩", url="https://t.me/a_t_9")],
    ]

    START = """  - اهلا {} 
اهلاً بك في {}
بوت يساعدك في استخراج كود تيليثون او كود بايروجرام
𝗗𝗘𝗩 :- @a_t_9
    """
    
    HELP = """
  - طريقة الاستخدام؟ . 
  
/about - حول البوت
/help - مساعدة
/start - بدء الاستخراج
/repo - اعطاء ريبو البوت
/generate - استخراج الجلسات 
/cancel - الغاء الاستخراج 
/restart - ترسيت اليوت
"""
    
    # About Message
    ABOUT = """
حول البوت 
بوت استخراج كود تيليثون وبايروجرام مقدم من @a_t_9

قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/BThon)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
𝗗𝗘𝗩 : @a_t_9
    """
    
    # Repo Message
    REPO = """
انا بوت وظيفتي اساعدك باستخراج كود بايروجرام و تيليثون

𝗗𝗘𝗩𝗦 : [بـلاك](https://t.me/a_t_9)
السورس [𝗦𝗘𝗖𝗨𝗥𝗘 𝗕𝗧𝗛𝗢𝗡](https://t.me/BThon)
   """
