# JPFun

**Japan leisure map** — ski, surf, dive & camp on one map (EN/KO).  
Domain: [jpfun.net](https://jpfun.net). MVP forked from OKSki / former oktrail scaffold.

## Local setup

```bash
cd /opt/work/jpfun
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # MAPS_API_KEY for map tiles
python3 script/seed_outdoor.py --force
python3 script/build_data.py
PORT=8081 python run.py   # http://localhost:8081
```

## IA

```text
/                 activity hub
/ski              ski map + region filters
/ski/hokkaido     ski × region (SEO)
/dive  (/scuba→)  scuba map
/surf /camp       same pattern
/item/<slug>      detail
```

## Seed data

- `script/outdoor_catalog.py` — leisure seeds
- `script/seed_outdoor.py` — writes `{id}_en.md` / `{id}_ko.md`

## Stack

Flask, Google Maps, markdown → JSON.
