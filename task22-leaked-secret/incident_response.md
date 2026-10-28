\# Task 22: Exposed API Credential Incident Response



\## Scenario



A developer accidentally published a configuration file containing a possible API credential in a public repository. The file was deleted five minutes later.



Deleting the file does not guarantee that the credential is safe. It may remain in Git history, forks, caches, or copies, and someone may have accessed it during those five minutes.



\## 1. Immediate Response



1\. \*\*Revoke or rotate the credential:\*\* Contact the credential owner or service administrator and invalidate the exposed credential. Generate a replacement if the application still requires it.

2\. \*\*Secure the repository:\*\* Remove the exposed secret from the current files and Git history where appropriate. Restrict repository access temporarily if necessary.

3\. \*\*Check for misuse:\*\* Review available API audit logs for unexpected requests, unfamiliar IP addresses, unusual usage, or suspicious activity during and after the exposure.

4\. \*\*Verify recovery:\*\* Confirm that the old credential no longer works and that legitimate applications use the replacement successfully.



\## 2. Investigation



\- Identify the credential type, affected service, and permissions.

\- Determine when the file became public and when it was removed.

\- Check Git history, forks, and other accessible copies for continued exposure.

\- Review available service logs for evidence of unauthorized use.

\- Record the timeline, findings, actions taken, and any remaining uncertainty.



\## 3. Prevention



\- Store credentials in environment variables or a secrets manager instead of configuration files committed to Git.

\- Enable secret scanning and repository push protection where available.

\- Use least-privilege permissions and credential expiration or rotation.

\- Add sensitive configuration files to `.gitignore`, while recognizing that this does not remove files already tracked by Git.

\- Establish a clear procedure for reporting and responding to exposed credentials.



\## Conclusion



The highest priority is to invalidate the exposed credential, not merely delete the file. Investigation should determine whether misuse occurred, while preventive controls reduce the risk of future accidental exposure.



\*\*Assessment:\*\* Task 22 — Secret Exposure Response  

\*\*Purpose:\*\* Defensive incident response and prevention.



