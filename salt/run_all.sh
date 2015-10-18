docker run -i --name saltmaster -t saltmaster /bin/bash

docker run -i -t --link saltmaster:saltmaster saltminion /bin/bash
