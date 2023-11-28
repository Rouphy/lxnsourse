from .song import Song
import requests
import json

# 设置API密钥和API请求URL

with open("./src/plugins/lxnsourse/config.json", "r") as f:
    i = json.loads(f.read())
    api_key = i['api_key']
base_url = 'https://maimai.lxns.net/api/v0/maimai/player/'
headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json',
}

'''一个该api接口的返回数据例：# print(response.content.decode("utf-8"))
{
"success": true, 
"code": 200, 
"data": {
    "name": "☆ＲＯＵＰＨＹ☆", 
    "rating": 14951, 
    "friend_code": 749274362297052,
    "trophy": {"name": "くらべられっ子", "color": "Gold"}, 
    "course_rank": 10,
    "class_rank": 5, 
    "star": 273,
    "icon_url": "https://maimai.wahlap.com/maimai-mobile/img/Icon/86aca2d93ab9d849.png",
    "rating_base_url": "https://maimai.wahlap.com/maimai-mobile/img/rating_base_platinum.png?ver=1.30",
    "course_rank_url": "https://maimai.wahlap.com/maimai-mobile/img/course/course_rank_10hvsSHd90.png",
    "class_rank_url": "https://maimai.wahlap.com/maimai-mobile/img/class/class_rank_s_05AJFCJjbq.png",
    "name_plate": {"id": 206201, "name": "オンゲキちほー4"},
    "frame": {"id": 209506, "name": "モ゜ルモ゜ル"},
    "upload_time": "2023-11-02T01:03:37Z"}
}
'''


def fdc_or_qq(n):
    """
    判断输入值是好友码还是qq号，如果是q号则转换成好友码，如果是好友码则返回原值
    :param n: number
    :return: friend_code 好友码 type:int
    """
    if len(str(n)) >= 11:
        return int(n)
    else:
        url = f'{base_url}qq/{n}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response = json.loads(response.content.decode("utf-8"))
            response = response['data']
            return response['friend_code']  # api提供的json表中好友码是int类型，不做处理
        else:
            print(f"好友码转换失败，状态码:{response.status_code}")


def song_info(friend_code, id):
    """
    用好友码查询单曲成绩
    :param friend_code: 好友码
    :param id: 乐曲id
    :return: 查询成功则返回Song类对象，否则打印错误码
    """
    url = f'{base_url}{friend_code}/bests'
    if id <= 10000:
        params = {
            'song_id': id,
            'song_type': 'standard'
        }
    else:
        params = {
            'song_id': id - 10000,
            'song_type': 'dx'
        }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response = json.loads(response.content.decode("utf-8"))
        response = response['data']
        # print(response)  # 测试用
        song = Song()
        song.inst(response)
        return song
    else:
        print(f"成绩查询失败，状态码：{response.status_code}")


def song_level(id):
    """
    通过id调用api查询定数并且返回一个列表
    :param id: int
    :return: level_value:list 定数表列表
    """
    level_value = []
    url = 'https://maimai.lxns.net/api/v0/maimai/song/list'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = json.loads(response.content.decode("utf-8"))
        # print(response)  # 测试用
        song_li = response['songs']
        if id <= 10000:  # 标准谱
            for song in song_li:
                if song['id'] == id:
                    difficulties = song['difficulties']
                    level = difficulties['standard']
                    for i in level:
                        level_value.append(i['level_value'])

        else:  # dx谱
            for song in song_li:
                if song['id'] == id - 10000:
                    difficulties = song['difficulties']
                    level = difficulties['dx']
                    for i in level:
                        level_value.append(i['level_value'])

        return level_value
    else:
        print(f"定数查询失败，状态码：{response.status_code}")


'''一个查询例的部分内容
jsn = {'songs': [
    {'id': 1575, 'title': '僕の和風本当上手', 'artist': 'ボス', 'genre': 'ゲームバラエティ', 'bpm': 120, 'version': 23001,
     'difficulties': {'standard': [], 'dx': [
         {'type': 'dx', 'difficulty': 0, 'level': '5', 'level_value': 5, 'note_designer': '', 'version': 23001},
         {'type': 'dx', 'difficulty': 1, 'level': '8', 'level_value': 8, 'note_designer': '', 'version': 23001},
         {'type': 'dx', 'difficulty': 2, 'level': '12', 'level_value': 12, 'note_designer': 'はっぴー', 'version': 23001},
         {'type': 'dx', 'difficulty': 3, 'level': '14', 'level_value': 14, 'note_designer': '僕の檸檬本当上手',
          'version': 23001}]}}, {'id': 1576, 'title': 'Cthugha', 'artist': 'USAO', 'genre': 'ゲームバラエティ', 'bpm': 213,
                                 'version': 23001, 'difficulties': {'standard': [], 'dx': [
            {'type': 'dx', 'difficulty': 0, 'level': '6', 'level_value': 6, 'note_designer': '', 'version': 23001},
            {'type': 'dx', 'difficulty': 1, 'level': '8+', 'level_value': 8.8, 'note_designer': '', 'version': 23001},
            {'type': 'dx', 'difficulty': 2, 'level': '12', 'level_value': 12.5, 'note_designer': '翠楼屋',
             'version': 23001},
            {'type': 'dx', 'difficulty': 3, 'level': '14', 'level_value': 14.3, 'note_designer': 'Jack',
             'version': 23001}]}}]
}
'''

# song_info(fdc_or_qq(1944287336), 11407)
# print(song_level(11407))
