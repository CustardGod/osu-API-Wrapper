import osu


class Game:

    def __init__(self, data):
        self.game_id = data['game_id']
        self.start_time = data['start_time']
        self.end_time = data['end_time']
        self.beatmap_id = data['beatmap_id']
        self.play_mode = osu.Modes(int(data['play_mode']))
        self.match_type = data['match_type']
        self.scoring_type = data['scoring_type']
        self.team_type = data['team_type']
        self.mods = data['mods']
        self.scores = data['scores']
        self.slot = data['slot']
        self.team = data['team']
        self.user_id = data['user_id']
        self.score = data['score']
        self.maxcombo = data['maxcombo']
        self.rank = data['rank']
        self.count300 = data['count300']
        self.count100 = data['count100']
        self.count50 = data['count50']
        self.countmiss = data['countmiss']
        self.countgeki = data['countgeki']
        self.countkatu = data['countkatu']
        self.perfect = data['perfect']
        self.passed = data['pass']

    def __repr__(self):
        return '<osu.Game game_id={0.game_id} beatmap_id={0.beatmap_id}>'.format(self)
