import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL configuration
MYSQL_CONFIG = {
    'host': os.getenv('SQL_HOST', 'localhost'),
    'user': os.getenv('SQL_USER', 'root'),
    'password': os.getenv('SQL_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'sakila'),
    'charset': 'utf8mb4'
}

# MongoDB configuration (using connection URI)
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
MONGO_CONFIG = {
    'uri': MONGO_URI,
    'database': os.getenv('MONGO_DB', 'movie_search'),
    'collection': os.getenv('MONGO_COLLECTION', 'final_project_121225ptm_Maksym_Kravchenko')
}

# Pagination settings
RESULTS_PER_PAGE = 10
