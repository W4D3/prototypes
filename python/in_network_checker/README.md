# In Network Checker

This demo uses the PokitDok eligibility API to check if an input NPI is in or out of network
for a given member's plan information. This version is configured ONLY to check for members of Cigna.

First, set up your environment:
```
./setup.sh
```

Then, activate your environment:
```
source venv/bin/activate
```

Finally, run the app:
```
PYTHONPATH=. python run.py
```

You can access the application at http://localhost:5000/
