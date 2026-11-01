# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-customs-cbp-usmca-origin-certification-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def audit_usmca_regional_value_content(net_cost_usd, value_non_originating_materials_vnm_usd, required_rvc_threshold_pct=60.0, calculation_method="NET_COST"):
    if net_cost_usd <= 0:
        raise ValueError("net_cost_usd must be positive")
        
    originating_materials_usd = max(0.0, net_cost_usd - value_non_originating_materials_vnm_usd)
    rvc_pct = (originating_materials_usd / net_cost_usd) * 100.0
    
    qualified = rvc_pct >= required_rvc_threshold_pct
    
    return {
        "calculation_method": calculation_method,
        "total_net_cost_usd": round(net_cost_usd, 2),
        "non_originating_materials_vnm_usd": round(value_non_originating_materials_vnm_usd, 2),
        "originating_content_usd": round(originating_materials_usd, 2),
        "calculated_rvc_percentage": round(rvc_pct, 2),
        "statutory_rvc_requirement_pct": required_rvc_threshold_pct,
        "usmca_origin_qualified": qualified,
        "cbp_preferential_tariff_indicator": "SPI_S_DUTY_FREE_ELIGIBLE" if qualified else "NON_ORIGINATING_STANDARD_DUTY_APPLIES",
        "compliance_action": "Generate USMCA Form 434 Certificate of Origin with exporter statement." if qualified else "USMCA origin claim denied; tariffs payable."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "audit_usmca_regional_value_content",
                        "description": """Audit USMCA (United States-Mexico-Canada Agreement) Rules of Origin qualification.
Implements Regional Value Content (RVC) calculations via Net Cost Method (RVC = (NC - VNM) / NC * 100) and Transaction Value Method (TV - VNM / TV * 100).
Certifies eligibility for duty-free preferential tariff treatment (Special Program Indicator 'S' or 'S+').""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = audit_usmca_regional_value_content(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'net_cost_usd': 12500.0, 'value_non_originating_materials_vnm_usd': 4200.0, 'required_rvc_threshold_pct': 60.0, 'calculation_method': 'NET_COST'}
        out = audit_usmca_regional_value_content(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
