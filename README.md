# CodeAlpha Secure Code Review



**Author:** Bilkisu Ishaq Muhammad  

**CodeAlpha Cyber Security Internship — Task 3**



## Project overview



I reviewed a deliberately vulnerable Python Flask login application,

identified four security weaknesses, implemented fixes, and tested

the updated application.



I combined manual code review, browser testing, database inspection,

and Bandit static analysis.



## Findings and fixes



| Finding | Fix |

|---|---|

| Dashboard accessible without login | Added a session check |

| SQL injection in login | Used a parameterized database query |

| Hardcoded session-signing secret | Generated a random secret at startup |

| Plaintext password storage | Stored password hashes and verified them with Werkzeug |



## Project files



\- `vulnerable/app.py` — original application for local security training

\- `fixed/app.py` — application with the four fixes

\- `reports/bandit\_before.txt` — initial scan results

\- `reports/bandit\_after.txt` — scan results after the fixes

\- `reports/Secure\_Code\_Review\_Report.docx` — detailed review report

\- `requirements.txt` — Python packages and versions

\- `.gitignore` — files excluded from Git tracking



## Setup on Windows



Use Python 3.13. Open Command Prompt inside the project folder.



Create and activate a virtual environment:



```bat

py -3.13 -m venv .venv313

.venv313\\Scripts\\activate

```



Install the required packages:



```bat

python -m pip install -r requirements.txt

```



## Run the corrected application



```bat

python fixed\\app.py

```



Open http://127.0.0.1:5000 in your browser.



Fictional practice credentials:



\- Username: `student`

\- Password: `Practice123!`



Press Ctrl + C in Command Prompt to stop the server.



The application creates its training database automatically.

Restarting the corrected application changes its signing key

and invalidates existing login sessions.



## Run the vulnerable version



For comparison in this local training exercise, stop the corrected

application first, then run:



```bat

python vulnerable\\app.py

```



Both versions use port 5000, so run only one at a time.



## Run Bandit



From the project folder:



```bat

python -m bandit -r vulnerable -f txt -o reports\\bandit\_before.txt

python -m bandit -r fixed -f txt -o reports\\bandit\_after.txt

```



These commands replace the corresponding report files.



## Test results



My final local tests confirmed that:



\- Logged-out visitors were redirected away from the dashboard.

\- The earlier SQL injection attempt was rejected.

\- Incorrect passwords were rejected.

\- Correct credentials opened the dashboard.

\- The new database stored a password hash.



The initial Bandit scan reported B105 and B608.

The final scan reported no issues identified.



A clean scan does not prove that an application is completely secure.



## Limitations



This project is for local learning with fictional credentials.

Do not deploy either version as a public login service.



Further production work would include CSRF protection, login rate

limiting, protected persistent secret management, HTTPS, and

appropriate deployment and cookie settings.



The new hashed database does not erase the original plaintext

training database. Generated databases are excluded from Git tracking.



## What I learned



I learned how to identify insecure code, understand its practical

impact, apply fixes, and retest the application. I also learned why

automated scanning should be combined with manual review and testing.

