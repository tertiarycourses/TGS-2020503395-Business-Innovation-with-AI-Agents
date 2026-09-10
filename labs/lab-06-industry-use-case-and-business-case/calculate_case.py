import csv
from pathlib import Path
rows={r['item']:float(r['amount_sgd']) for r in csv.DictReader((Path(__file__).parent/'cost-benefit.csv').open())}
net=rows['gross_benefit']-sum(v for k,v in rows.items() if k!='gross_benefit')
print({'net_benefit_sgd':net,'benefit_cost_ratio':round(rows['gross_benefit']/(rows['build_cost']+rows['run_cost']+rows['human_review_cost']+rows['expected_failure_loss']),2)})
