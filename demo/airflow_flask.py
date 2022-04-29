from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import yaml
import io
import json
from datetime import datetime
import textwrap
import os
import subprocess

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class MyDumper(yaml.Dumper):  # your force-indent dumper

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


class QuotedString(str):  # just subclass the built-in str
    pass


def quoted_scalar(dumper, data):  # a representer to force quotations on scalars
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')


# add the QuotedString custom type with a forced quotation representer to your dumper
MyDumper.add_representer(QuotedString, quoted_scalar)


@app.route('/dag_parameters', methods=["POST"])
@cross_origin()
def create_yml():
    input_json = request.get_json(force=True)

    # Opening JSON file
    with open(r'C:\My_space\Personal-cloud-repo\airflow-demo\demo\populate_csv.json') as file:
        data = json.load(file)

        start_date = input_json['start_date']
        end_date = input_json['end_date']
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        data['dag_populate_csv']['default_args']['start_date'] = start_date.date()
        data['dag_populate_csv']['default_args']['end_date'] = end_date.date()
        data['dag_populate_csv']['description'] = QuotedString(input_json['description'])
        data['dag_populate_csv']['schedule_interval'] = QuotedString(input_json['schedule'])
        data['dag_populate_csv']['tasks']['task_export_csv']['bash_command'] = QuotedString(input_json['command'])
        data['dag_populate_csv']['default_view'] = QuotedString(data['dag_populate_csv']['default_view'])
        data['dag_populate_csv']['orientation'] = QuotedString(data['dag_populate_csv']['orientation'])
        data['dag_populate_csv']['default_args']['owner'] = QuotedString(
            data['dag_populate_csv']['default_args']['owner'])
        tempData = yaml.dump(data, Dumper=MyDumper, default_flow_style=False)
        # print(tempData)

        tempData = tempData.replace("'\"", '"').replace("\"'", '"')
        os.chdir(r"C:\My_space\Personal-cloud-repo\airflow-demo")
        # print(tempData)
        tmp_path = os.getcwd()
        print(tmp_path)
        yml_file_name = 'scripts/populate_csv_dag_config.yml'
        with open(yml_file_name, 'w') as outfile:
            outfile.write(tempData)

        create_dag_factory(yml_file_name)

    return jsonify({'message': 'YAML & Dag Factory file has been generated successfully'})


def create_dag_factory(yml_file):
    file = 'dags/dag_populate_csv.py'
    with open(file, 'w') as f:
        f.write(textwrap.dedent(f'''\
        from airflow import DAG
        import dagfactory


        dag_factory = dagfactory.DagFactory("/home/airflow/gcs/dags/{yml_file}")

        dag_factory.clean_dags(globals())
        dag_factory.generate_dags(globals())
        '''))
        f.close()
        return 'file created'


@app.route('/pushFiles', methods=["GET"])
@cross_origin()
def push_changes():
    os.chdir(r"C:\My_space\Personal-cloud-repo\airflow-demo\demo")
    print(os.getcwd())
    return subprocess.Popen(r'bash git_clone.sh', shell=True, stdout=subprocess.PIPE).stdout.read()


if __name__ == "__main__":
    app.run()
