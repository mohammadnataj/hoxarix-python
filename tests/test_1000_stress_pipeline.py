import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from hoxarix import Client


REQUESTS = 1000
WORKERS = 50


client = Client(
    api_key="YOUR_API_KEY",
    base_url="http://127.0.0.1:8000",
    timeout=30
)


messages = [
    "Analyze AI governance policy",
    "Remember enterprise context",
    "Explain runtime memory system",
    "Check security policy",
    "Process financial AI request",
    "Evaluate agent trust state",
    "Explain decision trace",
    "Run enterprise workflow"
]


def execute(i):

    msg = messages[i % len(messages)]

    start = time.time()

    try:
        result = client.runtime.run(
            agent_id=f"load-test-{i}",
            input=msg
        )

        latency = time.time() - start

        return {
            "success": result.get("success"),
            "latency": latency,
            "memory": result["result"]["memory_count"]
        }

    except Exception as e:

        return {
            "success": False,
            "latency": 0,
            "error": str(e)
        }


def main():

    print("\n========== HOXARIX 1000 LOAD TEST ==========")
    print("Requests:", REQUESTS)
    print("Workers:", WORKERS)

    start = time.time()

    results = []

    with ThreadPoolExecutor(
        max_workers=WORKERS
    ) as executor:

        futures = [
            executor.submit(execute, i)
            for i in range(REQUESTS)
        ]

        for future in as_completed(futures):
            results.append(future.result())


    total = time.time() - start

    success = [
        r for r in results
        if r.get("success")
    ]

    failed = REQUESTS - len(success)

    latencies = [
        r["latency"]
        for r in success
    ]

    avg_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0
    )

    max_latency = (
        max(latencies)
        if latencies else 0
    )


    memory_max = max(
        [
            r.get("memory",0)
            for r in success
        ]
    )


    print("\n========== REPORT ==========")
    print("Total Requests:", REQUESTS)
    print("Successful:", len(success))
    print("Failed:", failed)
    print("Total Time:", round(total,3),"sec")
    print("Average Latency:", round(avg_latency,4),"sec")
    print("Max Latency:", round(max_latency,4),"sec")
    print(
        "Throughput:",
        round(REQUESTS/total,2),
        "req/sec"
    )
    print("Max Memory Count:", memory_max)
    print("============================")


if __name__ == "__main__":
    main()
