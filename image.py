# Ctrl+Shift+F10以运行
# Ctrl+/以多行注释
# Ctrl+Alt+L以美化代码
# Help下拉菜单以重置licence
# 现在，开始你的表演吧！
import json

from PIL import Image, ImageDraw, ImageFont
from .song import Song
from .api import song_level
from pathlib import Path

'''测试用例
song = [
    {'id': 1407, 'song_name': 'くらべられっ子', 'level': 'dx', 'level_index': 0, 'achievements': 101, 'fc': 'app', 'fs': None,
     'dx_score': 305, 'dx_rating': 45.024, 'rate': 'sssp', 'type': 'dx', 'upload_time': '2023-11-02T01:03:41Z'},
    {'id': 1407, 'song_name': 'くらべられっ子', 'level': 'dx', 'level_index': 1, 'achievements': 101, 'fc': 'app', 'fs': None,
     'dx_score': 869, 'dx_rating': 157.584, 'rate': 'sssp', 'type': 'dx', 'upload_time': '2023-11-02T01:03:41Z'},
    {'id': 1407, 'song_name': 'くらべられっ子', 'level': 'dx', 'level_index': 2, 'achievements': 100.9285, 'fc': 'ap',
     'fs': None,
     'dx_score': 1077, 'dx_rating': 220.6176, 'rate': 'sssp', 'type': 'dx', 'upload_time': '2023-11-02T01:03:41Z'},
    {'id': 1407, 'song_name': 'くらべられっ子', 'level': 'dx', 'level_index': 3, 'achievements': 101, 'fc': 'app', 'fs': 'fsp',
     'dx_score': 1490, 'dx_rating': 258.888, 'rate': 'sssp', 'type': 'dx', 'upload_time': '2023-11-02T01:03:41Z'},
    {'id': 1407, 'song_name': 'くらべられっ子', 'level': 'dx', 'level_index': 4, 'achievements': 100.0796, 'fc': None,
     'fs': None,
     'dx_score': 1724, 'dx_rating': 281.0235168, 'rate': 'sss', 'type': 'dx', 'upload_time': '2023-11-02T01:03:41Z'}]
'''


# song = Song(song) # 测试用
# print(song.type)


def song_image(song, id):
    """
    通过歌曲类和id进行绘图
    :param song: Song类的实例对象
    :param id: str,int,歌曲id
    :return: im: Image图片
    """
    level = song_level(id)
    im = Image.new('RGBA', (1080, 960), 'white')
    '''
    BuildImage.new("RGBA", (1080, 960), "white").draw_text((340, 98), text=song.song_name,
                                                          fontsize=32,
                                                          weight='bold',
                                                          halign='left',
                                                          valign='top'
                                                          ).image.show()
    '''
    draw = ImageDraw.Draw(im)
    cmyk = ['#6FD33A', '#F9B607', '#FF7B8F', '#9E4FDE', '#E6E6FA']
    acc = ImageFont.truetype('UDDigiKyokashoN-B.ttc', 32)
    tt = ImageFont.truetype('UDDigiKyokashoN-B.ttc', 64)
    dx = ImageFont.truetype('ARLRDBD.TTF', 12)
    cover = Image.open(Path(f"./src/static/mai/cover/{str(id).zfill(5)}.png")).convert('RGBA')
    type_ui = Image.open(Path(f"./src/static/lx/pic/UI_UPE_Infoicon_{song.type}.png")).convert('RGBA')

    im.paste(cover, (120, 85))
    draw.text((340, 98), text=song.song_name, font=tt, stroke_width=1, fill='black')
    im.paste(type_ui, (340, 270), type_ui)
    draw.text((490, 270), text=f"ID {id}", font=acc, fill='black')

    # ui = place_rate(song.rate[0])
    # im.paste(ui, (380, 426), ui)  透明背景图的复制方法
    # im.show()

    for i in range(len(level)):
        draw.text((170, 426 + (i * 80)), text=acc_str(song.achievements, i), font=acc, fill=cmyk[i])
        draw.text((170, 460 + (i * 80)), text=rat_str(song.dx_rating, i), font=dx, fill=cmyk[i])

        ui = place_rate(song.rate[i])
        im.paste(ui, (380, 426 + (i * 80)), ui)
        f = place_fc(song.fc[i])
        im.paste(f, (520, 426 + (i * 80)), f)
        s = place_fc(song.fs[i])
        im.paste(s, (600, 426 + (i * 80)), s)
        draw.text((700, 426 + (i * 80)), text=f"DX:{song.dx_score[i]}" if song.dx_score[i] != 0 else '', font=acc,
                  fill=cmyk[i])
        draw.text((850, 426 + (i * 80)), text=f"定数: {level[i] + 0.0}", font=acc, fill=cmyk[i])

    # im.show() # 测试用
    return im.convert('RGB')


def acc_str(li, i):
    if li[i] is None:
        return "NOT PLAYED"
    else:
        return f"{str(li[i])}%"


def rat_str(li, i):
    if li[i] is None:
        return "NOT PLAYED"
    else:
        return f"RATING:{str(int(li[i]))}"


def dx_str(dx_score):
    dx_score = f"DX:{dx_score}" if dx_score != 0 else ''
    return dx_score


def place_rate(rank):
    """
    把评分等级（s,ss+等）字符串转换成图片形式返回出去
    :param rank: RateType,str
    :return:Image
    """
    rank = rank.upper()
    img = Image.open(Path(f"./src/static/lx/pic/UI_GAM_Rank_{rank}.png")).convert(
        'RGBA') if rank != '' else Image.new("RGBA", (0, 0))  # 三目表达式判断字符串是否为空
    return img


def place_fc(fstatus):
    """
    把ap,fc等字符串转换成图片形式返回出去
    :param fstatus: FullComboType,FullSyncType,str,NoneType
    :return: Image
    """
    if fstatus:
        fstatus = fstatus.upper()
        img = Image.open(Path(f"./src/static/lx/pic/UI_MSS_MBase_Icon_{fstatus}.png")).convert('RGBA')
        return img
    else:
        img = Image.open(Path(f"./src/static/lx/pic/UI_MSS_MBase_Icon_Blank.png")).convert('RGBA')
        return img


# song_image(song, 11407)   # 测试用
