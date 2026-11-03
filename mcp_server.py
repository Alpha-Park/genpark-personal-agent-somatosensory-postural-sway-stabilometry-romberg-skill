"""
MCP Server for Somatosensory Postural Sway & Center of Pressure (COP) Stabilometry.
Exposes tools for static balance, Romberg ratio, and sensory ataxia differentiation.
"""

import json
from typing import Dict, Any, Optional
from client import PosturalSwayStabilometryClient


def handle_evaluate_stabilometry(params: Dict[str, Any]) -> Dict[str, Any]:
    sway_area_eyes_open_mm2 = float(params.get("sway_area_eyes_open_mm2", 120.0))
    sway_area_eyes_closed_mm2 = float(params.get("sway_area_eyes_closed_mm2", 210.0))
    sway_velocity_eyes_open_mm_s = float(params.get("sway_velocity_eyes_open_mm_s", 8.5))
    sway_velocity_eyes_closed_mm_s = float(params.get("sway_velocity_eyes_closed_mm_s", 12.0))
    rms_ap_eyes_closed_mm = float(params.get("rms_ap_eyes_closed_mm", 4.2))
    rms_ml_eyes_closed_mm = float(params.get("rms_ml_eyes_closed_mm", 3.1))
    trial_duration_seconds = float(params.get("trial_duration_seconds", 30.0))

    client = PosturalSwayStabilometryClient()
    return client.evaluate_stabilometry(
        sway_area_eyes_open_mm2=sway_area_eyes_open_mm2,
        sway_area_eyes_closed_mm2=sway_area_eyes_closed_mm2,
        sway_velocity_eyes_open_mm_s=sway_velocity_eyes_open_mm_s,
        sway_velocity_eyes_closed_mm_s=sway_velocity_eyes_closed_mm_s,
        rms_ap_eyes_closed_mm=rms_ap_eyes_closed_mm,
        rms_ml_eyes_closed_mm=rms_ml_eyes_closed_mm,
        trial_duration_seconds=trial_duration_seconds
    )


TOOLS = {
    "evaluate_stabilometry": {
        "description": "Calculates force platform 95% confidence ellipse sway area, mean velocity, and Romberg Quotient (Area_EC / Area_EO) for sensory ataxia diagnosis.",
        "parameters": {
            "type": "object",
            "properties": {
                "sway_area_eyes_open_mm2": {
                    "type": "number",
                    "description": "95% confidence ellipse sway area with eyes open in mm2 (e.g. 120.0)."
                },
                "sway_area_eyes_closed_mm2": {
                    "type": "number",
                    "description": "95% confidence ellipse sway area with eyes closed in mm2 (e.g. 210.0)."
                },
                "sway_velocity_eyes_open_mm_s": {
                    "type": "number",
                    "description": "Mean center of pressure sway velocity eyes open in mm/s (e.g. 8.5)."
                },
                "sway_velocity_eyes_closed_mm_s": {
                    "type": "number",
                    "description": "Mean center of pressure sway velocity eyes closed in mm/s (e.g. 12.0)."
                },
                "rms_ap_eyes_closed_mm": {
                    "type": "number",
                    "description": "Anteroposterior root-mean-square displacement in mm, default 4.2."
                },
                "rms_ml_eyes_closed_mm": {
                    "type": "number",
                    "description": "Mediolateral root-mean-square displacement in mm, default 3.1."
                },
                "trial_duration_seconds": {
                    "type": "number",
                    "description": "Duration of recording trial in seconds, default 30.0."
                }
            },
            "required": ["sway_area_eyes_open_mm2", "sway_area_eyes_closed_mm2", "sway_velocity_eyes_open_mm_s", "sway_velocity_eyes_closed_mm_s"]
        },
        "handler": handle_evaluate_stabilometry
    }
}


def process_request(request_str: str) -> str:
    try:
        req = json.loads(request_str)
        method = req.get("method")
        req_id = req.get("id")

        if method == "tools/list":
            tools_list = [
                {
                    "name": name,
                    "description": spec["description"],
                    "inputSchema": spec["parameters"]
                }
                for name, spec in TOOLS.items()
            ]
            return json.dumps({"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools_list}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            if tool_name not in TOOLS:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}
                })

            result = TOOLS[tool_name]["handler"](args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }
            })

        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32600, "message": f"Unsupported method '{method}'"}
            })

    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })


if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        if line.strip():
            print(process_request(line))
            sys.stdout.flush()
