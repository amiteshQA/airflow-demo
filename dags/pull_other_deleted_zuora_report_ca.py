from airflow import DAG
import dagfactory

dag_factory = dagfactory.DagFactory("/home/airflow/gcs/dags/scripts/zuora_other_delete_reports_ca.yml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())