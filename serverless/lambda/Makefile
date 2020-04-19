.PHONY: fetch-dependencies clean clean-lambda test lambda clean-all

# example: make lambda || make deploy ENV=prod STAGE=dev REGION=us-west-2 RESULT_ENDPT=V2/result PUBLISH_ENDPT=V2/publish
# STAGE := beta, dev
# ENV := lab, nonprod, prod
# REGION := us-west-2 (lab), us-east-2 (nonprod)
# TARGET := user-group, queue, aurora, layer, lambda, gateway

PROJECT             := selenium-lambda
SELEN_LAYER 		:= selenium_layer
OTHER_LAYER 		:= requirement_layer
PANDAS_LAYER		:= pandas_layer
LAMBDA		  		:= lambda
ENV					:= lab
STAGE				:= dev
REGION				:= us-west-2
VERSION				:= V2
PUBLISH_ENDPT		:= publish
RESULT_ENDPT		:= result
OTHER_LAYER 		:= requirement_layer


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


clean-layers:
	@find . -type d -name ${SELEN_LAYER} -exec rm -r {} \+ \
	&& find . -type d -name ${OTHER_LAYER} -exec rm -r {} \+ \
	&& find . -type d -name ${PANDAS_LAYER} -exec rm -r {} \+ ;\

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

# make deploy-layers ENV=luis STAGE=dev REGION=us-west-2
deploy-layers:
	@ echo "Deploying Lambda Layers..." ;\
	cd ${SELEN_LAYER} \
	&& sls deploy -v --region ${REGION} --stage ${STAGE};\
	cd ../${OTHER_LAYER} \
	&& sls deploy -v --region ${REGION} --stage ${STAGE} ;\
	cd ../${PANDAS_LAYER} \
	&& sls deploy -v --region ${REGION} --stage ${STAGE} ;\
	echo "Lambda Layers Deployed..." ;

# make deploy-local-lambda ENV=lab STAGE=dev REGION=us-west-2
# make deploy-local-lambda ENV=nonprod STAGE=dev REGION=us-east-2 
deploy-local-lambda:
	@ echo "Deploying Lambda Stack..." ;\
	. config/secrets/${ENV}.env \
	&& cd ${LAMBDA} \
	&& sls deploy -v --env ${ENV} --stage ${STAGE} ;\
	echo "Lambda Stack Deployed..." ;\

deploy-local-layers:
	@ echo "Deploying Lambda Layers..." ;\
	. config/secrets/${ENV}.env \
	&& cd ${SELEN_LAYER} \
	&& sls deploy -v --region ${REGION} --stage ${STAGE} ;\
	cd ../${SELEN_LAYER} \
	&& sls deploy -v --region ${REGION} --stage ${STAGE} ;\
	echo "Lambda Layers Deployed..." ;



# make testing ENV=cat STAGE=alpha REGION=mordor VERSION=V2 RESULT_ENDPT=result PUBLISH_ENDPT=publish
testing:
	@ echo "testing ..." ;\
	echo ${ENV} ;\
	echo "make deploy --env ${ENV} --stage ${STAGE} --region ${REGION} --result ${VERSION}/${RESULT_ENDPT} --publish ${VERSION}/${PUBLISH_ENDPT}" ;


test:
	@pytest -s -v --tb=short tests/


layers:
	@echo "[Fetching Dependencies] ..." ;\
	make clean-layers ;\
	mkdir -p ${SELEN_LAYER}/ \
	&& pip install -t ${SELEN_LAYER}/selenium/python/lib/python3.6/site-packages selenium \
	&& cp config/sls/seleniumLayer_serverless.yaml ${SELEN_LAYER}/serverless.yaml ;\

	mkdir -p ${SELEN_LAYER}/chromedriver \
	&& cd ${SELEN_LAYER}/chromedriver \
	&& curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip \
	&& unzip chromedriver.zip \
	&& rm chromedriver.zip \
	&& curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-41/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip \
	&& unzip headless-chromium.zip \
	&& rm headless-chromium.zip ;\

	mkdir -p ${PANDAS_LAYER} \
	&& pip install pandas -t ${PANDAS_LAYER}/pandas/python/lib/python3.6/site-packages \
	&& cp config/sls/pandasLayer_serverless.yaml ${PANDAS_LAYER}/serverless.yaml ;\

	mkdir -p ${OTHER_LAYER}/ \
	&& pip install -r src/requirements.txt -t ${OTHER_LAYER}/other/python/lib/python3.6/site-packages \
	&& cp config/sls/requirementLayer_serverless.yaml ${OTHER_LAYER}/serverless.yaml ;\
	echo "[Done] ..."


lambda:
	@echo "[Making Lambda] ..." ;\
	make clean-lambda ;\
	mkdir -p ${LAMBDA}/func \
	&& cp ./src/func/engine.py ${LAMBDA}/func/engine.py \
	&& cp ./src/func/selen.py ${LAMBDA}/func/selen.py \
	&& cp ./src/func/filter.py ${LAMBDA}/func/filter.py \
	&& cp ./src/func/publish.py ${LAMBDA}/publish.py \
	&& cp ./src/func/results.py ${LAMBDA}/results.py \
	&& cp ./src/func/__init__.py ${LAMBDA}/func/__init__.py \
	&& cp -r ./src/lib/ ${LAMBDA}/lib/ \
	&& cp -r ./src/config/ ${LAMBDA}/config/ \
	&& cp -r ./src/func/ui ${LAMBDA}/func/ui \
	&& cp ./src/main.py ${LAMBDA}/main.py \
	&& cp ./src/serverless.yaml ${LAMBDA}/serverless.yaml ;\
	echo "[Made Lambda] ..."