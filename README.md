http://localhost:52795/csp/irisapp/EnsPortal.ProductionConfig.zen

http://localhost:52795/csp/irisapp/EnsPortal.LookupSettings.zen

Admin
SYS

docker-compose exec iris bash

halt

pip3 install --target /InterSystems/IRIS/mgr/python .

irispython
from pylotaut import pylotaut

iris session iris
zn "IRISAPP"
do ##class(%SYS.Python).Shell()