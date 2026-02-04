def audit_zero_trust(baseline_set, current_log_list):

      baseline = set(baseline_set)
      log_list = set(current_log_list)

      authorized = baseline & log_list
      alerts = log_list - baseline
      inactive = baseline - log_list

      return authorized, alerts, inactive