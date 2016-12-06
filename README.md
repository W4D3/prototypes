## Prototypes

The repository is home to a simple demos to illustrate how to use the PokitDok APIs. 
Unless otherwise noted, most projects will have:

- README.md: providing an overview of how to setup and use the application.
- setup.sh: installs the application


## Prerequisites
The following steps create enviornment varibles in your system for your PokitDok client_id and client_secret. 

First: open your `.bashrc` file in your text editor of choice. (I prefer using vi from a terminal):
```bash
vi $HOME/.bashrc
```

Next, add the two lines below to update your `.bashrc` to export `POKITDOK_*` environment variables. You will need to use your client_id and client_secret for your PokitDok application. These variables store the client credentials for your PokitDok App (you should never check your client_id and secret into publicly available code)

```bash
export POKITDOK_CLIENT_ID=<client id>
export POKITDOK_CLIENT_SECRET=<client secret>
```
Lastly, open a terminal and source your `.bashrc` to make the variables accessible in your localhost:

```
source $HOME/.bashrc
```

Once you have set up your environment variables, go to the specific project's README for more set up details:

(Cigna's In-Network Checker)[https://github.com/denisekgosnell/prototypes/tree/master/python/in_network_checker]
