from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.data.mock_data import (
    PLAYERS, PLAYER_BY_ID, TOURNAMENTS, TOURNAMENT_BY_ID,
    MATCHES, NEWS, NEWS_BY_ID, enrich_match, build_bracket,
)

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="Tennis Hub — 网聚")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def base_ctx(request: Request, active: str = ""):
    return {"request": request, "active": active}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    enriched = [enrich_match(m) for m in MATCHES]
    live = [m for m in enriched if m["status"] == "进行中"]
    upcoming = [m for m in enriched if m["status"] == "未开始" and m["player1"] and m["player2"]][:4]
    recent_finished = [m for m in enriched if m["status"] == "已结束"][-4:]
    ctx = base_ctx(request, "home")
    ctx.update({
        "live_matches": live,
        "upcoming_matches": upcoming,
        "recent_finished": recent_finished,
        "featured_tournaments": TOURNAMENTS[:4],
        "latest_news": NEWS[:3],
    })
    return templates.TemplateResponse(request, "home.html", ctx)


@app.get("/schedule", response_class=HTMLResponse)
async def schedule(request: Request, tour: str = "ALL", status: str = "ALL"):
    enriched = [enrich_match(m) for m in MATCHES if m["p1"] and m["p2"]]
    if tour != "ALL":
        enriched = [m for m in enriched if m["tournament"] and tour in m["tournament"]["tour"]]
    if status != "ALL":
        enriched = [m for m in enriched if m["status"] == status]
    enriched.sort(key=lambda m: m["start_time"])
    ctx = base_ctx(request, "schedule")
    ctx.update({"matches": enriched, "tour": tour, "status": status})
    return templates.TemplateResponse(request, "schedule.html", ctx)


@app.get("/draws", response_class=HTMLResponse)
async def draws(request: Request, tour_id: int = 1):
    bracket = build_bracket(tour_id)
    ctx = base_ctx(request, "draws")
    ctx.update({"bracket": bracket, "tournaments": TOURNAMENTS, "current_id": tour_id})
    return templates.TemplateResponse(request, "draws.html", ctx)


@app.get("/match/{match_id}", response_class=HTMLResponse)
async def match_detail(request: Request, match_id: int):
    m = next((x for x in MATCHES if x["id"] == match_id), None)
    if not m:
        return HTMLResponse("Match not found", status_code=404)
    match = enrich_match(m)
    # mock technical stats
    stats = {
        "first_serve_pct": (68, 62),
        "first_serve_win": (78, 65),
        "second_serve_win": (55, 48),
        "aces": (8, 3),
        "double_faults": (2, 5),
        "break_points": ("4/7", "1/3"),
        "total_points": (98, 81),
    }
    commentary = [
        {"time": "第二盘 第5局", "text": "破发！强势底线对拉后赢得制胜分"},
        {"time": "第二盘 第4局", "text": "ACE！外角发球时速 188 km/h"},
        {"time": "第二盘 第3局", "text": "网前小球处理精彩，赢得鼓掌"},
        {"time": "第一盘 第10局", "text": "6-3 拿下首盘"},
        {"time": "第一盘 第7局", "text": "关键破发点保发成功"},
    ]
    ctx = base_ctx(request, "")
    ctx.update({"match": match, "stats": stats, "commentary": commentary})
    return templates.TemplateResponse(request, "match_detail.html", ctx)


@app.get("/players", response_class=HTMLResponse)
async def players(request: Request, tour: str = "ALL"):
    pl = PLAYERS
    if tour != "ALL":
        pl = [p for p in PLAYERS if p["tour"] == tour]
    pl = sorted(pl, key=lambda p: p["current_rank"])
    ctx = base_ctx(request, "players")
    ctx.update({"players": pl, "tour": tour})
    return templates.TemplateResponse(request, "players.html", ctx)


@app.get("/player/{player_id}", response_class=HTMLResponse)
async def player_detail(request: Request, player_id: int):
    p = PLAYER_BY_ID.get(player_id)
    if not p:
        return HTMLResponse("Player not found", status_code=404)
    # Find matches involving this player
    player_matches = [enrich_match(m) for m in MATCHES if m["p1"] == player_id or m["p2"] == player_id]
    ctx = base_ctx(request, "players")
    ctx.update({"player": p, "matches": player_matches})
    return templates.TemplateResponse(request, "player_detail.html", ctx)


@app.get("/rankings", response_class=HTMLResponse)
async def rankings(request: Request, tour: str = "WTA"):
    pl = sorted([p for p in PLAYERS if p["tour"] == tour], key=lambda p: p["current_rank"])
    ctx = base_ctx(request, "rankings")
    ctx.update({"players": pl, "tour": tour})
    return templates.TemplateResponse(request, "rankings.html", ctx)


@app.get("/news", response_class=HTMLResponse)
async def news(request: Request, category: str = "ALL"):
    items = NEWS if category == "ALL" else [n for n in NEWS if n["category"] == category]
    categories = ["ALL", "赛事战报", "球员动态", "前瞻分析", "短视频"]
    ctx = base_ctx(request, "news")
    ctx.update({"news_list": items, "category": category, "categories": categories})
    return templates.TemplateResponse(request, "news.html", ctx)


@app.get("/news/{news_id}", response_class=HTMLResponse)
async def news_detail(request: Request, news_id: int):
    n = NEWS_BY_ID.get(news_id)
    if not n:
        return HTMLResponse("News not found", status_code=404)
    ctx = base_ctx(request, "news")
    ctx.update({"item": n, "related": [x for x in NEWS if x["id"] != news_id][:3]})
    return templates.TemplateResponse(request, "news_detail.html", ctx)


# JSON API for live score polling
@app.get("/api/live")
async def api_live():
    enriched = [enrich_match(m) for m in MATCHES if m["status"] == "进行中"]
    return {"count": len(enriched), "matches": [
        {
            "id": m["id"],
            "score": m["score"],
            "live": m.get("live", {}),
            "p1": m["player1"]["name_cn"] if m["player1"] else "",
            "p2": m["player2"]["name_cn"] if m["player2"] else "",
        } for m in enriched
    ]}
