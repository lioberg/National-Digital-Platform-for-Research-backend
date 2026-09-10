import urllib.request
import json

def test_endpoints():
    print("Testing GET /api/health...")
    with urllib.request.urlopen("http://localhost:8000/api/health") as res:
        print("Health response:", res.read().decode()[:150])

    print("\nTesting GET /api/land-parcels...")
    with urllib.request.urlopen("http://localhost:8000/api/land-parcels") as res:
        data = json.loads(res.read().decode())
        print(f"Loaded {data.get('total')} parcels. Sample parcel ID: {data['features'][0]['properties']['id']}")

    print("\nTesting POST /api/semantic-search...")
    req_body = json.dumps({"query": "compensation under RFCTLARR Act 2013", "top_k": 2}).encode('utf-8')
    req = urllib.request.Request(
        "http://localhost:8000/api/semantic-search",
        data=req_body,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as res:
        search_res = json.loads(res.read().decode())
        print("Top match title:", search_res['results'][0]['document']['title'])
        print("Similarity score:", search_res['results'][0]['similarity_score'])
        print("AI Synthesis snippet:", search_res['ai_synthesis'][:120])

    print("\nTesting GET /api/acquisition/summary...")
    with urllib.request.urlopen("http://localhost:8000/api/acquisition/summary") as res:
        print("Acquisition summary:", res.read().decode())

    print("\nAll backend endpoints verified successfully!")

if __name__ == "__main__":
    test_endpoints()
