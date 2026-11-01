# genpark-agentic-commerce-customs-cbp-usmca-origin-certification-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

USMCA / CUSMA / T-MEC Regional Value Content (RVC net cost method) and tariff shift rule-of-origin certification auditor.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `audit_usmca_regional_value_content`
- **Category**: `agentic_commerce`

### Method Documentation
Audit USMCA (United States-Mexico-Canada Agreement) Rules of Origin qualification.
Implements Regional Value Content (RVC) calculations via Net Cost Method (RVC = (NC - VNM) / NC * 100) and Transaction Value Method (TV - VNM / TV * 100).
Certifies eligibility for duty-free preferential tariff treatment (Special Program Indicator 'S' or 'S+').

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "audit_usmca_regional_value_content",
    "arguments": {
    "net_cost_usd": 12500.0,
    "value_non_originating_materials_vnm_usd": 4200.0,
    "required_rvc_threshold_pct": 60.0,
    "calculation_method": "NET_COST"
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
