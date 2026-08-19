from dagster import job, op
import os

@op
def ingest():
	os.system("python pipeline/ingest.py")

@op
def validate(_ingest):
	os.system("python pipline/validate.py")

@op
def transform(_validate):
	os.system("cd dbt_pipeline && dbt run --profiles-dir .")

@op
def test_data(_transform):
	os.system("cd dbt_pipeline && dbt test --profiles-dir .")

@job
def ventes_pipeline():
	test_data(transform(validate(ingest())))
