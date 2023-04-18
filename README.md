# mlops-zoomcamp

## Overview

MLOps  practice project  from collecting requirements, model design, deployment and monitoring.

 [Sourced from this tutorial](https://github.com/DataTalksClub/mlops-zoomcamp))


### Pre-requisites(packages)

* Linux OS
* Python
* Docker
* MLflow
* Prefect
* Evidently

#### Dataset site.  Newyork Yellow/ Green Taxi Trip Record Data

** [Dataset site](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)




### [1: Introduction](01_intro)

* Download: NewYork Taxi trips dataset from above website.
* Design and train an ML model to predict trip duration. (duration-prediction.ipynb)



### [2: Experiment tracking ](02_experiement_tracking)

* Design experiments
* Track experiments with MLflow.(duration-prediction.ipynb)
* Saving and loading models versions with MLflow. (duration-prediction.ipynb)
* Model registry. (model-registry.ipynb)

#### Start MLFlow server to track experiments.

````

mlflow ui --backend-store-uri sqlite:///mlflow.db

````

### [3:Orchestration](03_orchestration)

* Workflow orchestration. (model-training.ipynb)
````

$ mlflow ui --backend-store-uri sqlite:///mlflow.db

````
* Prefect. (prefect_deploy.ipynb, prefect_flow.ipynb)
````

$ prefect orion start

````
* Turn notebook to pipeline using prefect.(work-queue.py.ipynb)

### [4:Deployment](04_deployment)
* Online Deployment.
   - Web service deployment with Flask and Docker
````

$ cd web-service. 
$ python predict.py
$ python test.py

````
    
   - Web service deployment with Flask and Docker. Model sourced from registry(MLflow)
````
$ cd web-service-webflow 
$ python predict.py
$ python test.py

````
* Offline Deployment
  - Batch Processing with Prefect
````
$ cd batch 
$ python predict.py
$ python test.py
mlflow ui --backend-store-uri sqlite:///mlflow.db

````
  
### [5:Monitoring](05_monitoring)
* Create prediction service
````
$ cd prediction-service 
$ python app.py
$ python test.py


````
* Batch monitoring using Prefect, MongoDB and Evidently
````
$ cd prediction-service 
$ python app.py
 
$ cd evidently_service
$ python app.py

$ cd 05_monitoring
$ python prepare.py # Download datasets
$ python send_data.py # monitor datasets as they are sent to prediction service

$ prefect orion start  # prefect server

````

### [6:Best Practices](06_best_practices)

````
 * Unit testing
````
$ cd unit-test-pytest 
$ pytest

```