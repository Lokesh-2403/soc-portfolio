\# Task 9: Defensive Detection Rule Test Results



\## 1. Objective



Test a Sigma rule that detects Windows failed-logon events and identify false positives, missed attack events, and possible improvements.



\## 2. Dataset



The dataset contains 266 synthetic authentication events.



| Metric                   | Count |

| ------------------------ | ----: |

| Total events             |   266 |

| Attack-labelled events   |    47 |

| Benign-labelled events   |   219 |

| Failed logons (4625)     |   114 |

| Successful logons (4624) |   152 |



Scenarios include normal logons, mistyped passwords, shared VPN IPs, service-account failures, lockout activity, loud password spraying, and low-and-slow password spraying.



\## 3. Test Method



The rule condition was evaluated against the CSV data: events with `event\_id = 4625` were counted as alerts, and all other events were counted as non-alerts. Results were compared with the dataset's `label` field.



The Sigma rule was also validated using `sigma check`. It reported zero errors, condition errors, and validation issues.



\## 4. Measured Results



| Result               | Count |

| -------------------- | ----: |

| True positives       |    45 |

| False positives      |    69 |

| Missed attack events |     2 |

| True negatives       |   150 |

| Total alerts         |   114 |



\### Performance Metrics



| Metric              | Result |

| ------------------- | -----: |

| Precision           | 39.47% |

| Recall              | 95.74% |

| Accuracy            | 73.31% |

| False-positive rate | 31.51% |



Calculations use the synthetic dataset's labels as the reference.



\## 5. Scenario Findings



\- \*\*Normal logons:\*\* 120 benign events did not trigger alerts.

\- \*\*Mistyped passwords:\*\* 18 benign events triggered alerts.

\- \*\*Service-account failures:\*\* 24 benign events triggered alerts.

\- \*\*Shared VPN IP:\*\* 19 benign events triggered alerts, while 30 did not.

\- \*\*Lockout activity:\*\* 8 benign events triggered alerts.

\- \*\*Loud password spraying:\*\* 25 attack-labelled events triggered alerts; 1 was missed.

\- \*\*Low-and-slow password spraying:\*\* 20 attack-labelled events triggered alerts; 1 was missed.



\## 6. False Positives and Missed Cases



The rule generates false positives because ordinary failed logons can result from mistyped passwords, service-account problems, and shared VPN activity.



Two attack-labelled events were missed because their event IDs did not match the rule's failed-logon condition. This shows that the rule does not identify every attack-related event in the dataset.



\## 7. Recommended Improvement



Keep the failed-logon rule as a basic alert. Add a separate correlation rule that looks for repeated failures across multiple user accounts from the same source IP within a defined time window. Test the correlation logic against loud and low-and-slow password spraying.



\## 8. Conclusion



The rule detected 45 of 47 attack-labelled events, but 69 benign events also triggered alerts. Its measured recall was high, while its precision was low.



The rule is useful as a baseline for authentication monitoring, but it needs additional correlation logic and testing to identify password spraying more accurately.



\*\*Limitations:\*\* These results come from synthetic data and a direct simulation of the rule's `4625` condition. The Sigma rule was syntax-validated but was not executed in a live SIEM. Results may differ with real Windows security logs.



All data is synthetic and used for defensive cybersecurity practice.



