# Ticket Categorization Service

## Overview
Ticket categorization engine for SupportPilot — improves ticket routing accuracy, reduces SLA breaches, and optimizes first response time through accurate category assignment.

## Problem Statement
On June 3, 2026, Acme Horizon Group experienced a critical categorization failure:
- **31 of 146 tickets** were misrouted (21.2% misclassification rate)
- **P2 SLA compliance** dropped to 84% (target: 92%)
- **First response time** increased by 9.4 hours average

**Root Causes Identified:**
- Self-serve onboarding rollout
- Auto-suggest algorithm mismatch
- Outdated category taxonomy
- Inconsistent agent tagging

## Solution Architecture
- Categorization engine with ML-based classification
- Auto-suggest improvements with confidence scoring
- Taxonomy validation and clarity
- Real-time SLA tracking and alerts
- Agent training program

## Supported Categories
18-24 ticket categories including:
- Billing Disputes
- Password Reset
- Account Access
- Payment Failure
- Onboarding Setup
- Bug Report
- Feature Request
- And more...

## Key Metrics
- **Target:** 20% reduction in misclassifications by July 31, 2026
- **Achieved:** 18% reduction (21.2% → 14.8%)
- **SLA Improvement:** 84% → 88-90% (target 92%)
- **First Response Time:** 14.6 hours → 9.4 hours
- **Agent Error Rate:** 20% → 12% (post-training)

## Misroute Paths Addressed
- Password Reset → Billing Disputes (35% improvement)
- Account Access → Billing Disputes (34% improvement)
- Self-Serve Onboarding → Bug Report (resolved)
- Integration/API → Feature Request
- SSO/SAML → Account Access
- Subscription Changes → Billing Disputes

## Technology Stack
- Language: Python/Node.js
- ITSM Integration: SupportPilot API
- ML Framework: scikit-learn / TensorFlow (pilot)
- Database: PostgreSQL
- Monitoring: Datadog/CloudWatch

## Getting Started
```bash
git clone https://github.com/ACME-Mock-EU/ticket-categorization-service.git
cd ticket-categorization-service
pip install -r requirements.txt
```

## API Endpoints
- `POST /categorize` - Classify a ticket
- `GET /categories` - List all categories
- `GET /metrics/misclassification` - Get misclassification rates
- `GET /metrics/sla-compliance` - SLA compliance by priority

## Key Timeline
- **June 3:** Categorization crisis identified
- **June 23:** Taxonomy adjustment window
- **July 9 & 16:** Agent retraining sessions
- **July 31:** v1.2.0 release (18% improvement achieved)

## Contributing
See CONTRIBUTING.md for guidelines.

## License
Internal use only - Acme Horizon Group

## Support
Contact: support@acmemock02.de
