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
            title
            variationTitle
            description
            longDescription
            discount
            visible
            visibility
            weight
            width
            height
            depth
            stores {{
                inStore
                store {{
                    id
                    name
                    type
                    visible
                }}
            }}
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
                }}
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
            }}
            collectionProducts {{
                id
                variationId
                code
                ean
                inStore
            }}
            relatedProducts {{
                id
                variationId
                code
                ean
                inStore
            }}
        }}
    }}
}}
"""
