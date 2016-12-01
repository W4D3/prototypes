# Prototypes

The repository is home to a simple demos to illustrate how to use the PokitDok APIs. 
Unless otherwise noted, most projects will have:

- README.md: providing an overview of how to setup and use the application.
- setup.sh: installs the application


## Prerequisites
Update your $HOME/.bashrc to export PD_PLATFORM_* environment variables. These variables store the Platform
client credentials for your PokitDok App (you should never check your client_id and secret into publicly available code)

```bash
vi $HOME/.bashrc
export POKITDOK_CLIENT_ID=<client id>
export POKITDOK_CLIENT_SECRET=<client secret>
source $HOME/.bashrc
```

