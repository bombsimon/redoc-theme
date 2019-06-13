#!/usr/bin/env python
"""
A script to generate OpenAPI specification from markdown.
"""

import json


def main(src_file="README.md", dst_file="docs/documentation.json"):
    """
    Generate the documentation index from the repository README.
    """
    with open(src_file, "r") as readme:
        markdown = readme.read()

        data = {
            "info": {
                "termsOfService": "https://github.com/bombsimon/redoc-theme",
                "description": markdown,
                "license": {
                    "url": "https://opensource.org/licenses/MIT",
                    "name": "MIT",
                },
                "title": "ReDoc Theme",
                "version": "1.0",
                "contact": {"email": "simon@sawert.se"},
                "x-logo": {"url": "assets/logo.png"},
            },
            "swagger": "2.0",
        }

    with open(dst_file, "w") as doc_json:
        json.dump(data, doc_json, indent=2)


if __name__ == "__main__":
    main()
