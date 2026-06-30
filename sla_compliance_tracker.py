# SLA Compliance Tracking and Alerting
# Real-time monitoring of ticket SLA compliance by priority

class SLAComplianceTracker:
    def __init__(self):
        self.sla_thresholds = {
            "P1": 120,    # 2 hours
            "P2": 480,    # 8 hours (target 92%)
            "P3": 1440,   # 24 hours
            "P4": 2880    # 48 hours
        }
        self.alert_threshold = 0.92
    
    def track_compliance(self, tickets):
        '''Track SLA compliance by priority level'''
        compliance_metrics = {}
        for priority in self.sla_thresholds:
            compliant = self._check_priority_compliance(tickets, priority)
            compliance_metrics[priority] = compliant
        return compliance_metrics
    
    def _check_priority_compliance(self, tickets, priority):
        '''Check compliance for specific priority'''
        priority_tickets = [t for t in tickets if t['priority'] == priority]
        if not priority_tickets:
            return 1.0
        
        compliant_count = sum(1 for t in priority_tickets if t['response_time'] <= self.sla_thresholds[priority])
        return compliant_count / len(priority_tickets)
    
    def trigger_alert(self, priority, compliance_rate):
        '''Alert when SLA compliance drops below threshold'''
        if compliance_rate < self.alert_threshold:
            return {
                "alert_level": "CRITICAL",
                "priority": priority,
                "compliance": compliance_rate,
                "message": f"P{priority} SLA compliance at {compliance_rate:.1%} (target {self.alert_threshold:.1%})"
            }
        return None

# Dashboard integration
if __name__ == "__main__":
    tracker = SLAComplianceTracker()
    print("SLA Compliance Tracker initialized")
    print("Monitoring: P1 (2h), P2 (8h), P3 (24h), P4 (48h)")
