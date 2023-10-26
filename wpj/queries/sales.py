gql_query = """
query sales {{
        sales(
        offset: {offset},
        limit: {limit},
        sort: {sort},
        filter: {filter}
    )
    {{
        hasPreviousPage
        hasNextPage
        items {{
            id
            code
            dateCreated
            note
            currency {{
                code
                name
                symbol
                rate
                roundType
                roundDirection
                precision
                decimalMark
            }}
            language {{
                code
                name
                isActive
            }}
            user {{
                gender
                isActive
                dateRegistered
                dateUpdated
                dateLogged
                note
                id
                email
                name
                surname
                userName
                isB2B
                invoiceAddress {{
                    name
                    surname
                    firm
                    phone
                    ico
                    dic
                    street
                    city
                    zip
                    country {{
                        code
                        name
                    }}
                }}
                deliveryAddress {{
                    name
                    surname
                    firm
                    phone
                    ico
                    dic
                    street
                    city
                    zip
                    country {{
                        code
                        name
                    }}
                }}
                newsletterInfo {{
                    isSubscribed
                    dateSubscribe
                    dateUnsubscribe
                }}
            }}
            deliveryType {{
                id
                delivery {{
                    id
                    type
                    name
                    isInPerson
                }}
                payment {{
                    id
                    type
                    name
                }}
            }}
            totalPrice {{
                withVat
                withoutVat
                currency {{
                    code
                }}
            }}
            items {{
                id
                productId
                variationId
                pieces
                piecePrice {{
                    withVat
                    withoutVat
                    vatValue
                    vat
                    currency {{
                        code
                    }}
                }}
                totalPrice {{
                    withVat
                    withoutVat
                    vatValue
                    vat
                    currency {{
                        code
                    }}
                }}
                name
                product {{
                    id
                }}
            }}
        }}
    }}
}}
"""
#{"name": "_created_timestamp", "type": "TIMESTAMP", "defaultValueExpression": "CURRENT_TIMESTAMP()"},
bq_schema = [
    {"name": "id", "type": "INTEGER"},
    {"name": "code", "type": "STRING"},
    {"name": "currency", "type": "RECORD", "mode": "NULLABLE", 
     "fields": [
        {"name": "code", "type": "STRING"},
        {"name": "name", "type": "STRING"},
        {"name": "symbol", "type": "STRING"},
        {"name": "rate", "type": "NUMERIC"},
        {"name": "roundType", "type": "INTEGER"},
        {"name": "roundDirection", "type": "STRING"},
        {"name": "precision", "type": "INTEGER"},
        {"name": "decimalMark", "type": "STRING"}
    ]},
    {"name": "language", "type": "RECORD", "mode": "NULLABLE", 
     "fields": [
        {"name": "code", "type": "STRING"},
        {"name": "name", "type": "STRING"},
        {"name": "isActive", "type": "BOOLEAN"}
    ]},
    {"name": "dateCreated", "type": "TIMESTAMP"},
    {"name": "user", "type": "RECORD", "mode": "NULLABLE", "fields": [
        {"name": "invoiceAddress", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "name", "type": "STRING"},
            {"name": "surname", "type": "STRING"},
            {"name": "firm", "type": "STRING"},
            {"name": "phone", "type": "STRING"},
            {"name": "ico", "type": "STRING"},
            {"name": "dic", "type": "STRING"},
            {"name": "street", "type": "STRING"},
            {"name": "city", "type": "STRING"},
            {"name": "zip", "type": "STRING"},
            {"name": "country", "type": "RECORD", "mode": "NULLABLE", "fields": [
                {"name": "code", "type": "STRING"},
                {"name": "name", "type": "STRING"}
            ]}
        ]},
        {"name": "deliveryAddress", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "name", "type": "STRING"},
            {"name": "surname", "type": "STRING"},
            {"name": "firm", "type": "STRING"},
            {"name": "phone", "type": "STRING"},
            {"name": "ico", "type": "STRING"},
            {"name": "dic", "type": "STRING"},
            {"name": "street", "type": "STRING"},
            {"name": "city", "type": "STRING"},
            {"name": "zip", "type": "STRING"},
            {"name": "country", "type": "RECORD", "mode": "NULLABLE", "fields": [
                {"name": "code", "type": "STRING"},
                {"name": "name", "type": "STRING"}
            ]}
        ]},
        {"name": "gender", "type": "STRING"},
        {"name": "isActive", "type": "BOOLEAN"},
        {"name": "newsletterInfo", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "isSubscribed", "type": "BOOLEAN"},
            {"name": "dateSubscribe", "type": "TIMESTAMP"},
            {"name": "dateUnsubscribe", "type": "TIMESTAMP"}
        ]},
        {"name": "dateRegistered", "type": "TIMESTAMP"},
        {"name": "dateUpdated", "type": "TIMESTAMP"},
        {"name": "dateLogged", "type": "TIMESTAMP"},
        {"name": "note", "type": "STRING"},
        {"name": "id", "type": "INTEGER"},
        {"name": "email", "type": "STRING"},
        {"name": "name", "type": "STRING"},
        {"name": "surname", "type": "STRING"},
        {"name": "userName", "type": "STRING"},
        {"name": "isB2B", "type": "BOOLEAN"}
    ]},
    {"name": "deliveryType", "type": "RECORD", "mode": "NULLABLE", "fields": [
        {"name": "id", "type": "INTEGER"},
        {"name": "delivery", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "id", "type": "INTEGER"},
            {"name": "type", "type": "STRING"},
            {"name": "name", "type": "STRING"},
            {"name": "isInPerson", "type": "BOOLEAN"}
        ]},
        {"name": "payment", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "id", "type": "INTEGER"},
            {"name": "type", "type": "STRING"},
            {"name": "name", "type": "STRING"}
        ]}
    ]},
    {"name": "note", "type": "STRING"},
    {"name": "totalPrice", "type": "RECORD", "mode": "NULLABLE", "fields": [
        {"name": "withVat", "type": "NUMERIC"},
        {"name": "withoutVat", "type": "NUMERIC"},
        {"name": "currency", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "code", "type": "STRING"}
        ]}
    ]},
    {"name": "items", "type": "RECORD", "mode": "REPEATED", "fields": [
        {"name": "id", "type": "INTEGER"},
        {"name": "productId", "type": "INTEGER"},
        {"name": "variationId", "type": "INTEGER"},
        {"name": "pieces", "type": "NUMERIC"},
        {"name": "piecePrice", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "withVat", "type": "NUMERIC"},
            {"name": "withoutVat", "type": "NUMERIC"},
            {"name": "vatValue", "type": "NUMERIC"},
            {"name": "vat", "type": "NUMERIC"},
            {"name": "currency", "type": "RECORD", "mode": "NULLABLE", "fields": [
                {"name": "code", "type": "STRING"}
            ]}
        ]},
        {"name": "totalPrice", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "withVat", "type": "NUMERIC"},
            {"name": "withoutVat", "type": "NUMERIC"},
            {"name": "vatValue", "type": "NUMERIC"},
            {"name": "vat", "type": "NUMERIC"},
            {"name": "currency", "type": "RECORD", "mode": "NULLABLE", "fields": [
                {"name": "code", "type": "STRING"}
            ]}
        ]},
        {"name": "name", "type": "STRING"},
        {"name": "product", "type": "RECORD", "mode": "NULLABLE", "fields": [
            {"name": "id", "type": "INTEGER"}
        ]}
    ]}
]
