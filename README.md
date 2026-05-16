# 网聚 · Tennis Hub

基于 FastAPI + Jinja2 的网球赛事数据平台 Demo（PC 端优先，可后期迁移小程序/H5/App）。

## 技术栈

- **后端**：FastAPI + Uvicorn
- **模板**：Jinja2
- **前端**：原生 HTML / CSS / JS（无框架依赖）
- **数据**：内置 mock 数据（位于 `app/data/mock_data.py`）

## 设计风格

清淡色调 + 网球元素：草地绿 `#7CB342` / 红土橙 `#E07856` / 网球黄 `#D4E157` / 硬地蓝 `#4FC3F7`，奶米白底色 `#FAFAF7`。

## 启动方式

```bash
conda activate fastapi
uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

打开 http://127.0.0.1:8765

## 路由

| 路由 | 说明 |
|---|---|
| `/` | 首页（直播比分、今日赛程、大赛入口、最新资讯） |
| `/schedule` | 赛程列表，支持 WTA/ATP × 状态筛选 |
| `/draws?tour_id=1` | 动态签表（罗马 1/4→半决→决赛） |
| `/match/{id}` | 比赛详情（实时比分、文字直播、技术统计、交手记录） |
| `/players` | 球员列表，按排名 + 巡回赛筛选 |
| `/player/{id}` | 球员主页（红土/硬地/草地胜率、近期走势、相关比赛） |
| `/rankings?tour=WTA` | WTA / ATP 实时排名榜 |
| `/news` / `/news/{id}` | 资讯中心 + 详情 |
| `/api/live` | JSON API（实时比分轮询） |

## 目录

```
tennis-hub/
├── app/
│   ├── main.py            # FastAPI 路由
│   └── data/mock_data.py  # 假数据
├── static/css/style.css   # 主题样式
├── templates/             # Jinja2 模板
│   ├── base.html, _macros.html
│   ├── home.html schedule.html draws.html
│   ├── match_detail.html
│   ├── players.html player_detail.html
│   ├── rankings.html
│   └── news.html news_detail.html
└── README.md
```

## 后续迁移

后端接口（`/api/*` 与 mock_data 结构）可直接复用至：
- 微信小程序（前端重写视图层）
- H5 / Vue / React 应用
- 接入真实数据源时只需替换 `mock_data.py`
