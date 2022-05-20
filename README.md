## Brownie contract template

### Installation:
install brownie:

```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install eth-brownie
```


Set global environment variables: 
``` 
export ETHERSCAN_TOKEN=<etherscan api token> 
export WEB3_INFURA_PROJECT_ID=<infura api key>
```

Set or generate some real-world address:
```
brownie accounts generate <id>
```
OR, using private key:
```
brownie accounts new <id>
```

### Usage:

To perform contract deployment and ICO, run:

```
brownie run scripts/ICO.py --network ropsten
```

### Tests:
Run:

```
brownie tests
```