
API_HOSTS = {
    "test": "http://localhost:10004/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    "test": "http://localhost:10004/",
    "dev": "",
    "prod": ""
}

DB_HOSTS = {
    "local": {
        "test": {
            "host": "localhost",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        }
    },
    "docker": {
        "test": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        }
    }
}
