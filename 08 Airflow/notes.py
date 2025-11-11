#

#! 96. Starting Airflow and Explore homepage

# ^ open: virtual machine

# * cmd -> write: airflow webserver
# * this will activate the webserver, so we can access airflow on our local browser or on the browser on the machine

# * webserver is the UI which by it, we can access airflow
# * to view our DAGS, run dag, pause dag

# * open any browser on your local machine not necessary on vm machine
# * because the machine configuration that the port is external connected to the other port (or port of th emachine not sure)
# * so we can access the both on any browser locally or on vm machine

# * write:localhost:8080
# * it will open: airflow on the vm machine not on the local machine because the two ports are connected

# * login form: write the username: kiwilytics and the provided password

# ^ Explore airflow UI:
# * you will find some DAGs are already loaded

# * message is written above: the scheduler doesn't appear to be running

# ? the scheduler:
# * it is the one who runs dags and airflow

# * till now that we only accessed airflow, we haven't operated it yet

# ^ Operate Airflow:
# * open new cmd -> write: airflow scheduler
# * return to browser
# * verify the scheduler is initiated by refreshing the browser webpage
# * the former message ( the scheduler doesn't appear to be running)
# * will be removed

# ^ we can search the dags by its name or its given tag


# *=================================================================================================

#! 97. Exploring Airflow UI Done

# ^ check cluster activity:
# * cluster is the local machine
# * check status healthy or non healthy

# * what is trigger in airflow cluster activity?
# * what does status of trigger means and also for metaDatabase or scheduler

# * check life metrics and historical metrics

# * check user roles
# * user statistics
# * check when a user had so many failed login


# * check actions: can-read, can-edit

# * check resources

# * action   |   resource
# * can_edit |   password


# * check list of dagrun: there are details such as state. dag id, run id, run type: schedule or manual


# * run type: scheduled - external trigger: true

# * check jobs, audit logs

# * admin, add variable

# ^ air flow configuartion:
# * not to be set on UI but in cfg file or during installation

# ^ check connection
# * connect airflow to database
# * connect to cloud
# * connect to localhost

# ^ check documentation

# *==========================================================================================

#! 98. Running Airflow Dag


# * python operator
# * import hook


# * no of retries in case of failure


# * deal with dag file as it is python file

# * every task should be in a function

# ? initiate DAG:
# * write: with DAG{dagid = 'name'} this dag id , you will find on airflow ui
# * catch up


# ^ identify task:
from tornado.process import task_id

# task will receive name, first task is t1, second is t2

# pass to every task the callable function for this task
# every task has an id

# order the tasks: t1 >> t2
