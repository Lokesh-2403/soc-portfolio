\# Task 9: Defensive Detection Rule Test Results



\## 1. Objective



Test a Sigma rule that detects Windows failed-logon events and identify its false positives, missed cases, and possible improvements.



\## 2. Dataset



The test dataset contains 266 synthetic authentication events.



| Event type | Count |

|---|---:|

| Successful logons (4624) | 152 |

| Failed logons (4625) | 114 |

| Benign-labelled events | 219 |

| Attack-labelled events | 47 |

| \*\*Total events\*\* | \*\*266\*\* |



Scenarios include normal logons, mistyped passwords, shared VPN IPs, service-account failures, lockout activity, loud password spraying, and low-and-slow password spraying.



\## 3. Test Cases



| Test case | Expected rule behaviour |

|---|---|

| Successful logon (4624) | No alert |

| Failed logon (4625) | Alert |

| Mistyped password | Alert; may be a false positive |

| Shared VPN IP with failed logons | Alert for each matching failure |

| Service-account authentication failure | Alert; may be a false positive |

| Loud password spraying | Matching failed logons alert, but the rule does not identify the overall spraying pattern |

| Low-and-slow password spraying | Matching failed logons alert, but the overall pattern may not be recognized |



\## 4. Results and Limitations



The Sigma rule passed validation with zero errors, zero condition errors, and zero validation issues.



The dataset contains 114 failed-logon events and 152 successful-logon events. Based on the rule condition, failed-logon events match the rule, while successful-logon events do not.



These counts describe the dataset and rule condition; they are not a measured precision or recall score. The rule has not yet been evaluated against each labelled event to calculate confirmed false positives and missed attacks.



\### Potential False Positives



\- Users entering incorrect passwords.

\- Shared VPN or NAT addresses generating failures from multiple users.

\- Service accounts using expired or incorrect credentials.



\### Detection Gaps



The rule detects individual failed logons rather than identifying repeated failures across multiple accounts or a time window. Therefore, it cannot independently confirm password spraying.



\## 5. Recommended Improvement



Keep the failed-logon rule as a basic alert and add a separate correlation rule that detects repeated failures across multiple user accounts from the same source IP within a defined time window. Test the correlation rule against both loud and low-and-slow spraying scenarios.



\## 6. Conclusion



The current rule is a valid baseline for detecting Windows failed-logon events. It is useful for basic authentication monitoring, but additional correlation and testing are needed to identify password spraying reliably.



All logs used in this assessment are synthetic and intended for defensive cybersecurity practice.



