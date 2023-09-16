http://localhost:52795/csp/irisapp/EnsPortal.ProductionConfig.zen

Admin
SYS

docker-compose exec iris bash

halt

pip3 install --target /InterSystems/IRIS/mgr/python .

irispython
from pylotaut import pylotaut

