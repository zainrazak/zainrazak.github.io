"""
app.py — Flask web UI for the recruiter outreach pipeline.

Usage:
    python app.py
    Then open http://localhost:5000 in your browser.
"""

import json
import queue
import threading

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

_queues: dict[str, queue.Queue] = {}


def _emit(q: queue.Queue, event: str, data: dict):
    q.put(f"event: {event}\ndata: {json.dumps(data)}\n\n")


def _run_pipeline(run_id: str, url: str):
    q = _queues[run_id]
    result: dict = {}

    try:
        _emit(q, "step", {"step": 1, "status": "running", "label": "Parsing job posting..."})
        from modules.job_parser import parse_job
        job_data = parse_job(url)
        result["job"] = job_data
        _emit(q, "step", {"step": 1, "status": "done", "label": "Job parsed", "data": job_data})

        _emit(q, "step", {"step": 2, "status": "pending", "label": "Contact finder (Phase 3 — coming soon)"})
        _emit(q, "step", {"step": 3, "status": "pending", "label": "Email verifier (Phase 4 — coming soon)"})
        _emit(q, "step", {"step": 4, "status": "pending", "label": "Sheets logger (Phase 5 — coming soon)"})
        _emit(q, "step", {"step": 5, "status": "pending", "label": "Email drafter (Phase 6 — coming soon)"})

        _emit(q, "done", {"result": result})

    except Exception as e:
        _emit(q, "error", {"message": str(e)})
    finally:
        q.put(None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run():
    url = request.json.get("url", "").strip()
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    import uuid
    run_id = str(uuid.uuid4())
    _queues[run_id] = queue.Queue()
    threading.Thread(target=_run_pipeline, args=(run_id, url), daemon=True).start()
    return jsonify({"run_id": run_id})


@app.route("/stream/<run_id>")
def stream(run_id: str):
    q = _queues.get(run_id)
    if not q:
        return Response("data: {}\n\n", mimetype="text/event-stream")

    def generate():
        while True:
            msg = q.get()
            if msg is None:
                break
            yield msg
        _queues.pop(run_id, None)

    return Response(generate(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
