class Doc:
    GET = {
        "parameters": [
            {
                "name": "Demo",
                "in": "body",
                "required": "true",
                "description": "Film object that needs to be persisted to the database",
                "schema": {
                    "type": "object",
                    "properties": {
                        'title': {
                            "type": "string",
                        }
                    },
                    "required": ["title"],
                }
            }
        ],
        "responses": {
            "200": {
                "description": "A list of colors (may be filtered by palette)",
                "examples": {
                    "rgb": [
                        "red",
                        "green",
                        "blue"
                    ]
                }
            }
        }
    }
