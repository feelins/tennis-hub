"""Mock tennis data — players, tournaments, matches, rankings, news.
Data sourced/inspired from public tennis sites (WTA/ATP, Flashscore-style) for demo only.
"""
from datetime import datetime, timedelta

NOW = datetime.now()

PLAYERS = [
    {"id": 1, "name_cn": "伊加·斯瓦泰克", "name_en": "Iga Swiatek", "country": "波兰", "flag": "🇵🇱",
     "hand": "右手", "birth": "2001-05-31", "current_rank": 2, "highest_rank": 1, "career_title": 24,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=IS&backgroundColor=7CB342",
     "win_clay": 0.88, "win_hard": 0.79, "win_grass": 0.71, "recent": "WWWLWWWLWW"},
    {"id": 2, "name_cn": "阿丽娜·萨巴伦卡", "name_en": "Aryna Sabalenka", "country": "白俄罗斯", "flag": "🇧🇾",
     "hand": "右手", "birth": "1998-05-05", "current_rank": 1, "highest_rank": 1, "career_title": 18,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=AS&backgroundColor=E07856",
     "win_clay": 0.71, "win_hard": 0.82, "win_grass": 0.68, "recent": "WWWWLWWWWW"},
    {"id": 3, "name_cn": "可可·高芙", "name_en": "Coco Gauff", "country": "美国", "flag": "🇺🇸",
     "hand": "右手", "birth": "2004-03-13", "current_rank": 3, "highest_rank": 2, "career_title": 10,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=CG&backgroundColor=D4E157",
     "win_clay": 0.74, "win_hard": 0.78, "win_grass": 0.72, "recent": "WLWWWWLWWW"},
    {"id": 4, "name_cn": "叶莲娜·莱巴金娜", "name_en": "Elena Rybakina", "country": "哈萨克斯坦", "flag": "🇰🇿",
     "hand": "右手", "birth": "1999-06-17", "current_rank": 4, "highest_rank": 3, "career_title": 8,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=ER&backgroundColor=A5D6A7",
     "win_clay": 0.66, "win_hard": 0.77, "win_grass": 0.81, "recent": "WWLWWWWLWW"},
    {"id": 5, "name_cn": "杰西卡·佩古拉", "name_en": "Jessica Pegula", "country": "美国", "flag": "🇺🇸",
     "hand": "右手", "birth": "1994-02-24", "current_rank": 5, "highest_rank": 3, "career_title": 5,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=JP&backgroundColor=FFD54F",
     "win_clay": 0.65, "win_hard": 0.74, "win_grass": 0.62, "recent": "WWWLWWLWWW"},
    {"id": 6, "name_cn": "米拉·安德烈耶娃", "name_en": "Mirra Andreeva", "country": "俄罗斯", "flag": "🇷🇺",
     "hand": "右手", "birth": "2007-04-29", "current_rank": 6, "highest_rank": 5, "career_title": 3,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=MA&backgroundColor=81C784",
     "win_clay": 0.72, "win_hard": 0.69, "win_grass": 0.60, "recent": "WWWWWLWWLW"},
    {"id": 7, "name_cn": "耶莲娜·奥斯塔彭科", "name_en": "Jelena Ostapenko", "country": "拉脱维亚", "flag": "🇱🇻",
     "hand": "右手", "birth": "1997-06-08", "current_rank": 11, "highest_rank": 5, "career_title": 8,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=JO&backgroundColor=F48FB1",
     "win_clay": 0.69, "win_hard": 0.62, "win_grass": 0.58, "recent": "WLWWLWWWLW"},
    {"id": 8, "name_cn": "埃琳娜·斯维托丽娜", "name_en": "Elina Svitolina", "country": "乌克兰", "flag": "🇺🇦",
     "hand": "右手", "birth": "1994-09-12", "current_rank": 14, "highest_rank": 3, "career_title": 17,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=ES&backgroundColor=64B5F6",
     "win_clay": 0.71, "win_hard": 0.68, "win_grass": 0.66, "recent": "LWWWLWWWWL"},
    {"id": 9, "name_cn": "索拉娜·科斯蒂亚", "name_en": "Sorana Cirstea", "country": "罗马尼亚", "flag": "🇷🇴",
     "hand": "右手", "birth": "1990-04-07", "current_rank": 32, "highest_rank": 21, "career_title": 1,
     "tour": "WTA", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=SC&backgroundColor=BA68C8",
     "win_clay": 0.61, "win_hard": 0.55, "win_grass": 0.50, "recent": "LWLWWLWLWW"},
    # ATP
    {"id": 10, "name_cn": "扬尼克·辛纳", "name_en": "Jannik Sinner", "country": "意大利", "flag": "🇮🇹",
     "hand": "右手", "birth": "2001-08-16", "current_rank": 1, "highest_rank": 1, "career_title": 19,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=JS&backgroundColor=EF6C00",
     "win_clay": 0.78, "win_hard": 0.86, "win_grass": 0.74, "recent": "WWWWWWLWWW"},
    {"id": 11, "name_cn": "卡洛斯·阿尔卡拉斯", "name_en": "Carlos Alcaraz", "country": "西班牙", "flag": "🇪🇸",
     "hand": "右手", "birth": "2003-05-05", "current_rank": 2, "highest_rank": 1, "career_title": 17,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=CA&backgroundColor=FFA726",
     "win_clay": 0.84, "win_hard": 0.81, "win_grass": 0.83, "recent": "WLWWWWWWLW"},
    {"id": 12, "name_cn": "亚历山大·兹维列夫", "name_en": "Alexander Zverev", "country": "德国", "flag": "🇩🇪",
     "hand": "右手", "birth": "1997-04-20", "current_rank": 3, "highest_rank": 2, "career_title": 23,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=AZ&backgroundColor=42A5F5",
     "win_clay": 0.74, "win_hard": 0.76, "win_grass": 0.65, "recent": "WWWLWWWWLW"},
    {"id": 13, "name_cn": "丹尼尔·梅德韦杰夫", "name_en": "Daniil Medvedev", "country": "俄罗斯", "flag": "🇷🇺",
     "hand": "右手", "birth": "1996-02-11", "current_rank": 5, "highest_rank": 1, "career_title": 20,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=DM&backgroundColor=78909C",
     "win_clay": 0.55, "win_hard": 0.79, "win_grass": 0.62, "recent": "LWWLWWWLWW"},
    {"id": 14, "name_cn": "诺瓦克·德约科维奇", "name_en": "Novak Djokovic", "country": "塞尔维亚", "flag": "🇷🇸",
     "hand": "右手", "birth": "1987-05-22", "current_rank": 6, "highest_rank": 1, "career_title": 99,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=ND&backgroundColor=2E7D32",
     "win_clay": 0.82, "win_hard": 0.85, "win_grass": 0.86, "recent": "WWLWWWWWLW"},
    {"id": 15, "name_cn": "泰勒·弗里茨", "name_en": "Taylor Fritz", "country": "美国", "flag": "🇺🇸",
     "hand": "右手", "birth": "1997-10-28", "current_rank": 4, "highest_rank": 4, "career_title": 9,
     "tour": "ATP", "avatar": "https://api.dicebear.com/7.x/initials/svg?seed=TF&backgroundColor=AB47BC",
     "win_clay": 0.58, "win_hard": 0.72, "win_grass": 0.71, "recent": "WWLWWLWWWW"},
]

PLAYER_BY_ID = {p["id"]: p for p in PLAYERS}

TOURNAMENTS = [
    {"id": 1, "name": "WTA 罗马大师赛", "name_en": "Internazionali BNL d'Italia",
     "tour": "WTA", "court": "红土", "level": "WTA 1000",
     "start": "2025-05-06", "end": "2025-05-19", "location": "意大利·罗马",
     "prize": "$5,395,025", "banner_color": "#E07856"},
    {"id": 2, "name": "法国网球公开赛", "name_en": "Roland Garros",
     "tour": "WTA/ATP", "court": "红土", "level": "大满贯",
     "start": "2025-05-25", "end": "2025-06-08", "location": "法国·巴黎",
     "prize": "€53,478,000", "banner_color": "#C65A3D"},
    {"id": 3, "name": "WTA 马德里公开赛", "name_en": "Madrid Open",
     "tour": "WTA", "court": "红土", "level": "WTA 1000",
     "start": "2025-04-22", "end": "2025-05-04", "location": "西班牙·马德里",
     "prize": "$8,963,700", "banner_color": "#D97548"},
    {"id": 4, "name": "温布尔登网球锦标赛", "name_en": "The Championships, Wimbledon",
     "tour": "WTA/ATP", "court": "草地", "level": "大满贯",
     "start": "2025-06-30", "end": "2025-07-13", "location": "英国·伦敦",
     "prize": "£50,000,000", "banner_color": "#7CB342"},
    {"id": 5, "name": "美国网球公开赛", "name_en": "US Open",
     "tour": "WTA/ATP", "court": "硬地", "level": "大满贯",
     "start": "2025-08-25", "end": "2025-09-07", "location": "美国·纽约",
     "prize": "$75,000,000", "banner_color": "#3F51B5"},
    {"id": 6, "name": "ATP 蒙特卡洛大师赛", "name_en": "Monte-Carlo Masters",
     "tour": "ATP", "court": "红土", "level": "ATP 1000",
     "start": "2025-04-06", "end": "2025-04-13", "location": "摩纳哥·蒙特卡洛",
     "prize": "€6,128,940", "banner_color": "#E07856"},
]

TOURNAMENT_BY_ID = {t["id"]: t for t in TOURNAMENTS}

# Roma WTA QF — based on PRD example
MATCHES = [
    # Roma QF (finished)
    {"id": 101, "tour_id": 1, "round": "1/4决赛", "p1": 9, "p2": 7,
     "start_time": (NOW - timedelta(days=2, hours=4)).strftime("%Y-%m-%d %H:%M"),
     "status": "已结束", "score": "2-1 (6-3, 4-6, 6-2)", "winner": 7, "court": "中央球场"},
    {"id": 102, "tour_id": 1, "round": "1/4决赛", "p1": 3, "p2": 6,
     "start_time": (NOW - timedelta(days=2, hours=2)).strftime("%Y-%m-%d %H:%M"),
     "status": "已结束", "score": "2-0 (6-4, 6-3)", "winner": 6, "court": "中央球场"},
    {"id": 103, "tour_id": 1, "round": "1/4决赛", "p1": 5, "p2": 1,
     "start_time": (NOW - timedelta(days=1, hours=4)).strftime("%Y-%m-%d %H:%M"),
     "status": "已结束", "score": "2-1 (6-4, 4-6, 7-5)", "winner": 1, "court": "中央球场"},
    {"id": 104, "tour_id": 1, "round": "1/4决赛", "p1": 8, "p2": 4,
     "start_time": (NOW - timedelta(days=1, hours=2)).strftime("%Y-%m-%d %H:%M"),
     "status": "已结束", "score": "2-0 (7-5, 6-2)", "winner": 4, "court": "1号球场"},
    # Roma SF (one in progress, one upcoming)
    {"id": 105, "tour_id": 1, "round": "半决赛", "p1": 7, "p2": 6,
     "start_time": NOW.strftime("%Y-%m-%d %H:%M"),
     "status": "进行中", "score": "1-0 (6-3, 3-2)", "winner": None,
     "live": {"set1": "6-3", "set2": "3-2", "set3": "", "game": "30-15"}, "court": "中央球场"},
    {"id": 106, "tour_id": 1, "round": "半决赛", "p1": 1, "p2": 4,
     "start_time": (NOW + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M"),
     "status": "未开始", "score": "", "winner": None, "court": "中央球场"},
    # Other Roma
    {"id": 107, "tour_id": 1, "round": "决赛", "p1": None, "p2": None,
     "start_time": (NOW + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
     "status": "未开始", "score": "", "winner": None, "court": "中央球场"},
    # ATP Monte-Carlo (示例)
    {"id": 201, "tour_id": 6, "round": "半决赛", "p1": 11, "p2": 12,
     "start_time": (NOW + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M"),
     "status": "未开始", "score": "", "winner": None, "court": "中央球场"},
    {"id": 202, "tour_id": 6, "round": "半决赛", "p1": 10, "p2": 14,
     "start_time": (NOW + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M"),
     "status": "未开始", "score": "", "winner": None, "court": "中央球场"},
    # Today various
    {"id": 203, "tour_id": 3, "round": "决赛", "p1": 2, "p2": 3,
     "start_time": (NOW - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"),
     "status": "进行中", "score": "1-1 (6-3, 4-6)", "winner": None,
     "live": {"set1": "6-3", "set2": "4-6", "set3": "2-1", "game": "15-30"}, "court": "中央球场"},
]


def enrich_match(m):
    """Attach player + tournament objects."""
    out = dict(m)
    out["player1"] = PLAYER_BY_ID.get(m["p1"]) if m["p1"] else None
    out["player2"] = PLAYER_BY_ID.get(m["p2"]) if m["p2"] else None
    out["winner_player"] = PLAYER_BY_ID.get(m["winner"]) if m.get("winner") else None
    out["tournament"] = TOURNAMENT_BY_ID.get(m["tour_id"])
    return out


NEWS = [
    {"id": 1, "title": "斯瓦泰克再夺罗马冠军 红土战绩傲视群芳",
     "category": "赛事战报", "cover": "https://picsum.photos/seed/tennis1/800/450",
     "summary": "伊加·斯瓦泰克在罗马大师赛决赛中连下两盘击败对手，蝉联冠军，本赛季红土赛季胜率高达 88%。",
     "author": "网聚资讯", "create_time": "2025-05-19 22:30",
     "content": "在罗马大师赛决赛中，世界第二伊加·斯瓦泰克展现出统治级的红土表现，以 6-2、6-3 的悬殊比分横扫对手，成功卫冕罗马冠军。这是她个人第 24 个 WTA 单打冠军，也进一步巩固了她在红土之王的地位。整场比赛斯瓦泰克的一发得分率达到了 78%，破发成功率超过 60%，展现了极高的竞技状态。"},
    {"id": 2, "title": "辛纳法网前接受采访：信心满满冲击全满贯",
     "category": "球员动态", "cover": "https://picsum.photos/seed/tennis2/800/450",
     "summary": "世界第一扬尼克·辛纳在罗马进行红土训练期间接受意大利媒体采访，表示对即将到来的法网信心十足。",
     "author": "网聚资讯", "create_time": "2025-05-18 14:20",
     "content": "辛纳近期状态正佳，他在采访中表示：'红土是一个需要更多耐心的场地，我已经做好了充分准备。'本赛季辛纳的红土胜率达到 78%，并在法网赛前的训练中显得非常从容。"},
    {"id": 3, "title": "前瞻：法网首日大战将上演 阿尔卡拉斯首战球迷期待",
     "category": "前瞻分析", "cover": "https://picsum.photos/seed/tennis3/800/450",
     "summary": "卫冕冠军阿尔卡拉斯将在法网首日登场，对阵一位资格赛突围的年轻球员。",
     "author": "网聚资讯", "create_time": "2025-05-24 09:00",
     "content": "阿尔卡拉斯本赛季红土胜率高达 84%，并在马德里站夺冠。罗兰加洛斯的红土更加缓慢，对他全面的击球技术非常友好。"},
    {"id": 4, "title": "高芙红土赛季崛起 连续三站打入八强",
     "category": "球员动态", "cover": "https://picsum.photos/seed/tennis4/800/450",
     "summary": "美国小将可可·高芙在马德里、罗马连续打入八强，红土实力受到关注。",
     "author": "网聚资讯", "create_time": "2025-05-15 18:45",
     "content": "过去一直被认为不擅长红土的可可·高芙今年完成蜕变，红土胜率提升至 74%，反手底线攻击更加稳定。"},
    {"id": 5, "title": "德约科维奇：还有更多冠军等着我",
     "category": "球员动态", "cover": "https://picsum.photos/seed/tennis5/800/450",
     "summary": "37 岁的德约科维奇在采访中表示自己依然有动力争夺更多大满贯冠军。",
     "author": "网聚资讯", "create_time": "2025-05-12 11:00",
     "content": "德约科维奇职业生涯已斩获 99 个 ATP 冠军，他坦言：'数字不重要，重要的是我对网球的热爱。'"},
    {"id": 6, "title": "短视频精选：本周十佳击球",
     "category": "短视频", "cover": "https://picsum.photos/seed/tennis6/800/450",
     "summary": "汇集本周 ATP/WTA 巡回赛中最精彩的十次击球，从大角度反手到网前妙手。",
     "author": "网聚视频", "create_time": "2025-05-18 20:00",
     "content": "精彩集锦回顾，包括阿尔卡拉斯的反手直线穿越、辛纳的爆发正手、斯瓦泰克的网前救球。"},
]

NEWS_BY_ID = {n["id"]: n for n in NEWS}


# Bracket data (Roma WTA — 8 → 4 → 2 → 1)
def build_bracket(tour_id: int = 1):
    """Return bracket structure for a tournament."""
    matches = [m for m in MATCHES if m["tour_id"] == tour_id]
    rounds = {"1/4决赛": [], "半决赛": [], "决赛": []}
    for m in matches:
        if m["round"] in rounds:
            rounds[m["round"]].append(enrich_match(m))
    return {
        "tournament": TOURNAMENT_BY_ID.get(tour_id),
        "quarter": rounds["1/4决赛"],
        "semi": rounds["半决赛"],
        "final": rounds["决赛"],
    }
