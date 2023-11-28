class Song:
    """
    歌曲成绩类，包含歌曲id，名称，成绩表，dx分数表，fc/fs表
    """
    id = 0
    song_name = ''
    type = ''
    # level_value = []
    achievements = [None, None, None, None, None]
    rate = ['', '', '', '', '']
    fc = [0, 0, 0, 0, 0]
    fs = [0, 0, 0, 0, 0]
    dx_rating = [None, None, None, None, None]
    dx_score = [0, 0, 0, 0, 0]

    def __init__(self):
        self.id = 0
        self.song_name = ''
        self.type = ''
        # level_value = []
        self.achievements = [None, None, None, None, None]
        self.rate = ['', '', '', '', '']
        self.fc = [0, 0, 0, 0, 0]
        self.fs = [0, 0, 0, 0, 0]
        self.dx_rating = [None, None, None, None, None]
        self.dx_score = [0, 0, 0, 0, 0]

    def inst(self, jsonlog):
        for i in jsonlog:
            self.id = i['id']
            self.song_name = i['song_name']
            self.type = i['type']
            if i['level_index'] in range(5):
                self.id = i['id']
                self.achievements[i['level_index']] = i['achievements']
                self.rate[i['level_index']] = i['rate']
                self.fc[i['level_index']] = i['fc']
                self.fs[i['level_index']] = i['fs']
                self.dx_rating[i['level_index']] = i['dx_rating']
                self.dx_score[i['level_index']] = i['dx_score']
