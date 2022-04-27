from airflow import DAG
import dagfactory


dag_factory = dagfactory.DagFactory("/home/airflow/gcs/scripts/populate_csv_dag_config.yml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())
