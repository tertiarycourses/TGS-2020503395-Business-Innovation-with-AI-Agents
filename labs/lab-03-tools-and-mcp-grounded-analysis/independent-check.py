import csv, statistics
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parent/'mock-tickets.csv').open()))
print({'count':len(rows),'median':statistics.median(int(r['resolution_minutes']) for r in rows),'breach_rate':sum(r['sla_breached']=='yes' for r in rows)/len(rows)})
