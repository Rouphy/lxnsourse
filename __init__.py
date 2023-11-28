# Ctrl+Shift+F10以运行
# Ctrl+/以多行注释
# Ctrl+Alt+L以美化代码
# Help下拉菜单以重置licence
# 现在，开始你的表演吧！
from io import BytesIO

from .api import song_info, fdc_or_qq
from .image import song_image

from nonebot import on_command, on_regex
from nonebot.params import CommandArg, EventMessage
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Message, MessageSegment

info = on_command("lxinfo")


@info.handle()
async def _(event: Event, args: Message = CommandArg()):
    arg = args.extract_plain_text()
    id = int(arg)
    qq = event.get_user_id()
    song = song_info(fdc_or_qq(qq), id)
    # song_image(song, id).show()
    #await info.finish(MessageSegment.image(song_image(song, id)))
    
    img = song_image(song, id)
    bio = BytesIO()
    img.save(bio, "JPEG")
    img = MessageSegment.image(bio)
    await info.finish(img)
    