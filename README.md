## Project Focus

Airflow works best with workflows that are mostly static and slowly changing. When the DAG structure is similar from one run to the next, it clarifies the unit of work and continuity. Other similar projects include [Luigi](https://github.com/spotify/luigi), [Oozie](https://oozie.apache.org/) and [Azkaban](https://azkaban.github.io/).

Airflow is commonly used to process data, but has the opinion that tasks should ideally be idempotent (i.e., results of the task will be the same, and will not create duplicated data in a destination system), and should not pass large quantities of data from one task to the next (though tasks can pass metadata using Airflow's [XCom feature](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)). For high-volume, data-intensive tasks, a best practice is to delegate to external services specializing in that type of work.

Airflow is not a streaming solution, but it is often used to process real-time data, pulling data off streams in batches.

## Principles

- **Dynamic**: Airflow pipelines are configuration as code (Python), allowing for dynamic pipeline generation. This allows for writing code that instantiates pipelines dynamically.
- **Extensible**: Easily define your own operators, executors and extend the library so that it fits the level of abstraction that suits your environment.
- **Elegant**: Airflow pipelines are lean and explicit. Parameterizing your scripts is built into the core of Airflow using the powerful **Jinja** templating engine.
- **Scalable**: Airflow has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers.

<!-- START Requirements, please keep comment here to allow auto update of PyPI readme.md -->


## Minimum Requirements
- CPU at least minimum of 4 cores
- Memory at least 8 GB of RAM (16 GB or more for larger workloads or multiple services).
- Storage of minimum SSD with at least 20 GB of free space.


## Getting started

1. Clone this repository 
```bash
git clone link_to_this_repo
```

2. Copy .env.example > .env and populate with you configuration

3. Run docker compose up airflow-init, after finish then run docker compose up. Optional you can also start flower using docker compose up --service flower

4. Accessing the web interface 
Once the cluster has started up, you can log in to the web interface and begin experimenting with DAGs.
The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow.

**For More:**
Visit the official Airflow website documentation (latest **stable** release) for help with
[installing Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/),
[getting started](https://airflow.apache.org/docs/apache-airflow/stable/start.html), or walking
through a more complete [tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/).


## Cleaning-up the environment
- Run ```docker compose down --volumes --remove-orphans``` command in the directory you downloaded the **docker-compose.yaml** file
- Remove the entire directory where you downloaded the docker-compose.yaml file ```rm -rf '<DIRECTORY>'```
- Run through this guide from the very beginning, starting by re-downloading the docker-compose.yaml file


## Scheduler Interval

    * * * * * 
    | | | | +--- day of the week (0 - 7) (Sunday is both 0 and 7)
    | | | +----- month (1 - 12)
    | | +------- day of the month (1 - 31)
    | +--------- hour (0 - 23)
    +----------- minute (0 - 59)

    **Or using a shortcut**
    - @none => Don’t schedule, use for exclusively “externally triggered” DAGs
    - @once => Run the DAG once and only once.
    - @hourly => Run the DAG every hour.
    - @daily => Run the DAG once a day at midnight (00:00).
    - @weekly => Run the DAG once a week at midnight on Sunday.
    - @monthly => Run the DAG once a month at midnight on the first day of the month.
    - @quarterly => Run the DAG once a quarter at midnight on the first day of January, April, July, and October.
    - @yearly or @annually => Run the DAG once a year at midnight on January 1.


## Monitor, Access and Trigger Airflow using BuiltIn RestApi
- List Dags
    curl -X GET 'https://{airflow_address}/api/v1/dags' \
    -H 'Content-Type: application/json' \
    --user "username:password"

- Manual Trigger Dags to Run:
    curl -X POST 'https://{airflow_address}/api/v1/dags/{dag_id or dag_name}/dagRuns' \
    -H 'Content-Type: application/json' \
    --user "username:password" 

More info:
    Visit the official docs: https://airflow.apache.org/docs/apache-airflow/2.6.2/stable-rest-api-ref.html


## User Interface

- **DAGs**: Overview of all DAGs in your environment.

  ![DAGs](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/dags.png)

- **Grid**: Grid representation of a DAG that spans across time.

  ![Grid](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/grid.png)

- **Graph**: Visualization of a DAG's dependencies and their current status for a specific run.

  ![Graph](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/graph.png)

- **Task Duration**: Total time spent on different tasks over time.

  ![Task Duration](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/duration.png)

- **Gantt**: Duration and overlap of a DAG.

  ![Gantt](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/gantt.png)

- **Code**: Quick way to view source code of a DAG.

  ![Code](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/code.png)