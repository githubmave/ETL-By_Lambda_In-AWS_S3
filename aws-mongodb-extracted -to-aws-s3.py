
def run(event=None, context=None):
	load_dotenv()

	mongodb_client = MongoClient(os.environ['MONGODB_CONNECT_URL'])
	s3_client = boto3.client('s3')

	# upload jobcategories_colletion
	jobcategories_colletion = get_collection(mongodb_client, os.environ['MONGODB_DATABE'], 'jobcategories')
	jobcategories_json = jobcategories_filter(jobcategories_colletion)
	try:
		upload_s3(s3_client, jobcategories_json, os.environ['LOAD_BUCKET_NAME'], 'jobcategories.json')
		print('jobcategories.json has been upload to S3')
	except Exception as error:
		print(error)

	# upload jobs collection
	jobs_collection = get_collection(mongodb_client, os.environ['MONGODB_DATABE'], 'jobs')
	jobs_json = jobs_filter(jobs_collection)
	try:
		upload_s3(s3_client, jobs_json, os.environ['LOAD_BUCKET_NAME'], 'jobs.json' )
		print('jobs.json has been upload to S3')
	except Exception as error:
		print(error)

	# upload users collection
	users_collection = get_collection(mongodb_client, os.environ['MONGODB_DATABE'], 'users')
	users_json = users_filter(users_collection)
	try:
		upload_s3(s3_client, users_json, os.environ['LOAD_BUCKET_NAME'], 'users.json' )
		print('users.json has been upload to S3')
	except Exception as error:
		print(error)

	# upload cities collection
	cities_collection = get_collection(mongodb_client, os.environ['MONGODB_DATABE'], 'cities')
	cities_json = cities_filter(cities_collection)
	try:
		upload_s3(s3_client, cities_json, os.environ['LOAD_BUCKET_NAME'], 'cities.json')
		print('cities.json has been upliad to S3')
	except Exception as error:
		print(error)

		
if __name__ == "__main__":