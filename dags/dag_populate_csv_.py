from airflow import DAG
import dagfactory


dag_factory = dagfactory.DagFactory("/home/airflow/gcs/dags/testing_anil")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())
