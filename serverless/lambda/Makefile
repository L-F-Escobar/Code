.PHONY: fetch-dependencies clean clean-lambda test lambda clean-all

PROJECT             := selenium-lambda
SELEN_LAYER 		:= selenium_layer
TXT_LAYER 			:= requirement_layer
PANDAS_LAYER		:= pandas_layer
LAMBDA		  		:= lambda
ENV					:= lab
STAGE				:= dev
REGION				:= us-east-1
VERSION				:= v1
PUBLISH_ENDPT		:= publish
RESULT_ENDPT		:= result


build:
ifeq ($(TARGET), layers)
	@make layers
endif
ifeq ($(TARGET), lambda)
	@make lambda
endif

deploy:
ifeq ($(TARGET), layers)
	@make deploy-layers
endif
ifeq ($(TARGET), lambda)
	@make deploy-lambda 
endif

test:
	@pytest -s -v --tb=short tests/

circleci:
	@mkdir -p  ./config/ \
	&& mkdir -p config/secrets/ \
	&& touch ./config/secrets/${ENV}.env \
	&& sudo chmod -R 777 /usr/local/share \
	&& sudo chmod -R 777 /usr/local/bin/ \
	&& sudo chmod -R 777 /usr/local/lib/python3.7/site-packages \
	&& make install 

install:
	@pip install -r ./src/requirements.txt \
	&& pip install -r ./tests/requirements.txt ;\

clean-pytest:
	@find . -type d -name __pycache__ -exec rm -r {} \+ \
	&& find . -type d -name .pytest_cache -exec rm -r {} \+ ;\

clean-lambda:
	@find . -type d -name ${LAMBDA} -exec rm -r {} \+ \

clean:
	@ echo "[Cleaning] ..." \
	&& make clean-pytest \
	&& make clean-lambda \
	&& make clean-layers ;

# . config/secrets/${ENV}.env 
deploy-lambda:
	@ echo "Deploying Lambda Stack..." ;\
	cd ${LAMBDA} \
	&& sls deploy -v --env ${ENV} --stage ${STAGE} ;\
	echo "Lambda Stack Deployed..." ;

# make deploy-local-lambda ENV=nonprod STAGE=dev REGION=us-east-1
deploy-local-lambda:
	@ echo "Deploying Lambda Stack..." ;\
	. config/${ENV}.env \
	&& cd ${LAMBDA} \
	&& sls deploy -v --env ${ENV} --stage ${STAGE} ;\
	echo "Lambda Stack Deployed..." ;\

lambda:
	@echo "[Making Lambda] ..." ;\
	make clean-lambda ;\
	mkdir -p ${LAMBDA}/func \
	&& cp ./src/func/engine.py ${LAMBDA}/func/engine.py \
	&& cp ./src/func/selen.py ${LAMBDA}/func/selen.py \
	&& cp ./src/func/publish.py ${LAMBDA}/publish.py \
	&& cp ./src/func/results.py ${LAMBDA}/results.py \
	&& cp -r ./src/lib/ ${LAMBDA}/lib/ \
	&& cp -r ./src/config/ ${LAMBDA}/config/ \
	&& cp ./src/main.py ${LAMBDA}/main.py \
	&& cp serverless.yaml ${LAMBDA}/serverless.yaml ;\
	echo "[Made Lambda] ..."