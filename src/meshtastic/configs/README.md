Given the headaches + inconsistencies between Android/iOS apps we should ideally use the python CLI for configuring our nodes. Aside from (hopefully) being more reliable this will let us check in configs. 


Useful commands: 

Setup (assuming python is installed - I used 3.9.15)
```
pip install meshtastic
```

Check that it is working with a node connected over serial:
```
meshtastic -s --info
```

Export config from existing node: 
```
meshtastic --export-config > example_config.yaml
```

Configure using local config file:
```
meshtastic --configure default_config.yaml
```
