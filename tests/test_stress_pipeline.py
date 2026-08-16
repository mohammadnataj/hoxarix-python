import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from hoxarix import Client


client = Client(
    api_key="hooshix-dev-key",
    base_url="http://127.0.0.1:8000",
    timeout=30
)


TOTAL_REQUESTS = 100
WORKERS = 20


messages = [
    "Explain AI governance",
    "How does memory system work?",
    "Analyze enterprise AI architecture",
    "Explain agent trust model",
    "Test explainability engine",
    "Evaluate policy decision",
    "Simulate enterprise workload",
]


def send_request(index):

    start = time.time()

    result = client.runtime.run(
        agent_id=f"stress-agent-{index % 10}",
        input=messages[index % len(messages)]
    )

    elapsed = time.time() - start


    return {
        "id": index,
        "success": result["success"],
        "memory": result["result"]["memory_count"],
        "trace": len(result["result"]["trace"]),
        "time": elapsed
    }



def test_hoxarix_full_pipeline_stress():

    results = []

    start = time.time()


    with ThreadPoolExecutor(
        max_workers=WORKERS
    ) as executor:


        futures = [
            executor.submit(
                send_request,
                i
            )
            for i in range(TOTAL_REQUESTS)
        ]


        for future in as_completed(futures):
            results.append(
                future.result()
            )


    total_time = time.time() - start


    success_count = sum(
        1 for r in results
        if r["success"]
    )


    avg_time = sum(
        r["time"]
        for r in results
    ) / len(results)


    max_memory = max(
        r["memory"]
        for r in results
    )


    print("\n========== HOXARIX STRESS REPORT ==========")

    print(
        "Requests:",
        TOTAL_REQUESTS
    )

    print(
        "Workers:",
        WORKERS
    )

    print(
        "Successful:",
        success_count
    )

    print(
        "Failed:",
        TOTAL_REQUESTS-success_count
    )

    print(
        "Total time:",
        round(total_time,3),
        "sec"
    )

    print(
        "Average latency:",
        round(avg_time,3),
        "sec"
    )

    print(
        "Max memory count:",
        max_memory
    )

    print(
        "=========================================="
    )


    assert success_count == TOTAL_REQUESTS
