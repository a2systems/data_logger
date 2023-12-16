{
    "name": "data_logger",
    "summary": """
        data_logger
        """,
    "description": """
    """,
    "category": "Stock",
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base","stock"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/data_logger.xml"
    ],
    'license': 'LGPL-3',
}
