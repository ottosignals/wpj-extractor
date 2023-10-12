gql_query = """
query Products {{
    products(
        offset: {offset},
        limit: {limit},
        sort: {sort},
        filter: {filter}
    ) 
    {{
        hasNextPage
        hasPreviousPage
        items {{
            id
            variationId
            url
            code
            ean
            inStore
            stores {{
                inStore
                store {{
                    id
                    name
                    type
                    visible
                }}
            }}
            title
            variationTitle
            description
            longDescription
            discount
            producer {{
                id
                name
                active
            }}
            price {{
                withVat
                withoutVat
                vatValue
                vat
                currency {{
                    code
                    rate
                }}
            }}
            visible
            visibility
            weight
            width
            height
            depth
            relatedProducts {{
                id
                variationId
                code
                ean
                inStore
            }}
            collectionProducts {{
                id
                variationId
                code
                ean
                inStore
            }}
            parameters {{
                values {{
                    description
                    text
                    list
                    number
                }}
                parameter {{
                    id
                    name
                    type
                    unit
                }}
            }}
            variations {{
                id
                code
                ean
                title
                inStore
                visible
                weight
            }}
        }}
    }}
}}
"""

bq_schema = [
  {"name": "_created_timestamp", "type": "TIMESTAMP", "defaultValueExpression": "CURRENT_TIMESTAMP()"},
  {"name": "id", "type": "INTEGER"},
  {"name": "variationId", "type": "INTEGER"},
  {"name": "url", "type": "STRING"},
  {"name": "code", "type": "STRING"},
  {"name": "ean", "type": "STRING"},
  {"name": "inStore", "type": "NUMERIC"},
  {
    "name": "stores",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {"name": "inStore", "type": "NUMERIC"},
      {
        "name": "store",
        "type": "RECORD",
        "fields": [
          {"name": "id", "type": "INTEGER"},
          {"name": "name", "type": "STRING"},
          {"name": "type", "type": "STRING"},
          {"name": "visible", "type": "BOOL"}
        ]
      }
    ]
  },
  {"name": "title", "type": "STRING"},
  {"name": "variationTitle", "type": "STRING"},
  {"name": "description", "type": "STRING"},
  {"name": "longDescription", "type": "STRING"},
  {"name": "discount", "type": "NUMERIC"},
  {
    "name": "producer",
    "type": "RECORD",
    "fields": [
      {"name": "id", "type": "INTEGER"},
      {"name": "name", "type": "STRING"},
      {"name": "active", "type": "BOOL"}
    ]
  },
  {
    "name": "price",
    "type": "RECORD",
    "fields": [
      {"name": "withVat", "type": "NUMERIC"},
      {"name": "withoutVat", "type": "NUMERIC"},
      {"name": "vatValue", "type": "NUMERIC"},
      {"name": "vat", "type": "NUMERIC"},
      {
        "name": "currency",
        "type": "RECORD",
        "fields": [
          {"name": "code", "type": "STRING"},
          {"name": "rate", "type": "NUMERIC"},
        ]
      }
    ]
  },
  {"name": "visible", "type": "BOOL"},
  {"name": "visibility", "type": "STRING"},
  {"name": "weight", "type": "NUMERIC"},
  {"name": "width", "type": "NUMERIC"},
  {"name": "height", "type": "NUMERIC"},
  {"name": "depth", "type": "NUMERIC"},
  {
    "name": "relatedProducts",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {"name": "id", "type": "INTEGER"},
      {"name": "variationId", "type": "INTEGER"},
      {"name": "code", "type": "STRING"},
      {"name": "ean", "type": "STRING"},
      {"name": "inStore", "type": "NUMERIC"}
    ]
  },
  {
    "name": "collectionProducts",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {"name": "id", "type": "INTEGER"},
      {"name": "variationId", "type": "INTEGER"},
      {"name": "code", "type": "STRING"},
      {"name": "ean", "type": "STRING"},
      {"name": "inStore", "type": "NUMERIC"}
    ]
  },
  {
    "name": "parameters",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "values",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {"name": "description", "type": "STRING"},
          {"name": "text", "type": "STRING"},
          {"name": "list", "type": "STRING"},
          {"name": "number", "type": "NUMERIC"}
        ]
      },
      {
        "name": "parameter",
        "type": "RECORD",
        "fields": [
          {"name": "id", "type": "INTEGER"},
          {"name": "name", "type": "STRING"},
          {"name": "type", "type": "STRING"},
          {"name": "unit", "type": "STRING"}
        ]
      }
    ]
  },
  {
    "name": "variations",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {"name": "id", "type": "INTEGER"},
      {"name": "code", "type": "STRING"},
      {"name": "ean", "type": "STRING"},
      {"name": "title", "type": "STRING"},
      {"name": "inStore", "type": "NUMERIC"},
      {"name": "visible", "type": "BOOL"},
      {"name": "weight", "type": "NUMERIC"}
    ]
  }
]