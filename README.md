# Freight/Logistics Routing Platform — Full-Stack VRP + TMS

Full-stack freight routing: shipments (FTL/LTL/parcel), carriers, VRP/TSP with time windows, warehouses, fleet telematics, tracking, pricing, compliance.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (PostGIS mock) (sqlite fallback)
- **Frontend:** React 18 + Vite + Leaflet (routing map) + Chart.js
- **15 Apps:** shipments, carriers, routing, warehouses, fleet, orders, tracking, pricing, compliance, analytics, integrations, dispatch, documentation, frontend, api

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t freight-routing .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
celery -A freight worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **Shipments:** FTL/LTL/parcel/intermodal, BOL/POD, status `pending→dispatched→in_transit→delivered`
- **Routing:** VRP with capacity + time windows, Dijkstra/A* for road graph, TSP brute for <10 stops
- **Warehouses:** slotting, inventory, WMS picking
- **Fleet:** vehicles, telematics, fuel, maintenance
- **Tracking:** GPS, ETA via OSRM (mock), geofence
- **Pricing:** rates, surcharges, tariffs, accessorial
- **Compliance:** customs, ELD, HOS, DOT

## License
Proprietary — All rights reserved (Freight Labs).
