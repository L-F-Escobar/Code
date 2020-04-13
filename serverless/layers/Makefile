.PHONY: build deploy circleci install clean clean-layers deploy-layers deploy-layers-local layers

PROJECT             := layers
SELENIUM_LAYER 		:= selenium_layer
REQ_TXT_LAYER 		:= requirement_txt_layer
ENV					:= example
STAGE				:= dev
REGION				:= us-east1
VERSION				:= v1

build:
ifeq ($(TARGET), layers)
	@make layers
endif

deploy:
ifeq ($(TARGET), layers)
	@make deploy-layers
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

clean-layers:
	@find . -type d -name ${SELENIUM_LAYER} -exec rm -r {} \+ \
	&& find . -type d -name ${REQ_TXT_LAYER} -exec rm -r {} \+ ;\

clean:
	@ echo "[Cleaning] ..." \
	&& make clean-layers ;

deploy-layers:
	@ echo "Deploying Lambda Layers..." ;\
	cd ${SELENIUM_LAYER} \
	&& sls deploy -v ;\
	cd ../${REQ_TXT_LAYER} \
	&& sls deploy -v;\
	echo "Lambda Layers Deployed..." ;

deploy-layers-local:
	@ echo "Deploying Lambda Layers..." ;\
	. config/${ENV}.env \
	&& cd ${SELENIUM_LAYER} \
	&& sls deploy -v ;\
	cd ../${REQ_TXT_LAYER} \
	&& sls deploy -v ;\
	echo "Lambda Layers Deployed..." ;

layers:
	@echo "[Fetching Dependencies] ..." ;\
	make clean-layers ;\
	mkdir -p ${SELENIUM_LAYER}/ \
	&& pip install -t ${SELENIUM_LAYER}/selenium/python/lib/python3.6/site-packages selenium \
	&& cp config/seleniumLayer.yaml ${SELENIUM_LAYER}/serverless.yaml ;\

	mkdir -p ${SELENIUM_LAYER}/chromedriver \
	&& cd ${SELENIUM_LAYER}/chromedriver \
	&& curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip \
	&& unzip chromedriver.zip \
	&& rm chromedriver.zip \
	&& curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-41/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip \
	&& unzip headless-chromium.zip \
	&& rm headless-chromium.zip ;\

	mkdir -p ${REQ_TXT_LAYER}/ \
	&& pip install -r requirements.txt -t ${REQ_TXT_LAYER}/txt/python/lib/python3.6/site-packages \
	&& cp config/ReqTxtLayer.yaml ${REQ_TXT_LAYER}/serverless.yaml ;\
	echo "[Done] ..."