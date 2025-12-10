import requests
from django.shortcuts import render

def commercial_data(request):
    url = "https://erp.wttint.com/api/method/wtt_module.wtt_module.page.commercial_bid_dashb.commercial_bid_dashb.get_commercial_bid_totals_revisions"

    response = requests.get(url)
    data = response.json()

    # Extract suppliers
    suppliers = data["message"]["suppliers"]
    overall_total = data["message"]["overall_total"]

    return render(request, "dashboard/commercial.html", {
        "suppliers": suppliers,
        "overall_total": overall_total
    })
