#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = time-series-sandbox

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Clean downloaded data files
clean-all:
	rm -f src/data/**/*

clean:
	rm -f src/data/interim/* src/data/processed/*

explore:
	docker-compose up -d explore

shell:
	docker-compose run --rm -w /usr/src/app explore /bin/bash
