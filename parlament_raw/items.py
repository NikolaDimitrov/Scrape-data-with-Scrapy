from scrapy_jsonschema.item import JsonSchemaItem

class MyItem(JsonSchemaItem):
    jsonschema = {
            "$schema": "http://json-schema.org/draft-07/schema",
            "$id": "http://example.com/example.json",
            "type": "object",
            "title": "The root schema",
            "description": "The root schema comprises the entire JSON document.",
            "default": {},
            "examples": [
                {
                    "Name": "АЛЕКСАНДЪР ТИХОМИРОВ СИМОВ",
                    "Date_of_Birth": "11/07/1977",
                    "Place_of_Birth": "Стара Загора, България",
                    "Job": "журналист",
                    "Language": "английски,руски",
                    "Politic": "БСП за БЪЛГАРИЯ",
                    "Email": "aleksandar.simov@parliament.bg",
                    "Picture_URL": "https://www.parliament.bg/images/Assembly/2799.png"
                }
            ],
            "required": [
                "Name",
                "Date_of_Birth",
                "Place_of_Birth",
                "Job",
                "Language",
                "Politic",
                "Email",
                "Picture_URL"
            ],
            "properties": {
                "Name": {
                    "$id": "#/properties/Name",
                    "type": "string",
                    "title": "The Name schema",
                    "description": "NAME.",
                    "default": "",
                    "examples": [
                        "АЛЕКСАНДЪР ТИХОМИРОВ СИМОВ"
                    ]
                },
                "Date_of_Birth": {
                    "$id": "#/properties/Date_of_Birth",
                    "type": "string",
                    "title": "The Date_of_Birth schema",
                    "description": "DATE OF BIRTH.",
                    "default": "",
                    "examples": [
                        "11/07/1977"
                    ]
                },
                "Place_of_Birth": {
                    "$id": "#/properties/Place_of_Birth",
                    "type": "string",
                    "title": "The Place_of_Birth schema",
                    "description": "PLACE OF BIRTH.",
                    "default": "",
                    "examples": [
                        "Стара Загора, България"
                    ]
                },
                "Job": {
                    "$id": "#/properties/Job",
                    "type": "string",
                    "title": "The Job schema",
                    "description": "JOB.",
                    "default": "",
                    "examples": [
                        "журналист"
                    ]
                },
                "Language": {
                    "$id": "#/properties/Language",
                    "type": "string",
                    "title": "The Language schema",
                    "description": "LANGUAGES.",
                    "default": "",
                    "examples": [
                        "английски,руски"
                    ]
                },
                "Politic": {
                    "$id": "#/properties/Politic",
                    "type": "string",
                    "title": "The Politic schema",
                    "description": "POLITICAL PARTIES.",
                    "default": "",
                    "examples": [
                        "БСП за БЪЛГАРИЯ"
                    ]
                },
                "Email": {
                    "$id": "#/properties/Email",
                    "type": "string",
                    "title": "The Email schema",
                    "description": "THE EMAIL.",
                    "default": "",
                    "examples": [
                        "aleksandar.simov@parliament.bg"
                    ]
                },
                "Picture_URL": {
                    "$id": "#/properties/Picture_URL",
                    "type": "string",
                    "title": "The Picture_URL schema",
                    "description": "URL OF PICTURE.",
                    "default": "",
                    "examples": [
                        "https://www.parliament.bg/images/Assembly/2799.png"
                    ]
                }
            },
            "additionalProperties": True
        }