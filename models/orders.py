query = """
    query orders{{
  orders(
  offset: {offset},
  limit: {limit},
  sort: {sort},
  filter: {filter}
  ) {{
    items {{
    id
    source {{
      source
      name
    }}
    dateCreated
    dateAccept
    dateHandle
    dateUpdated
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
    currencyRate
    code
    userId
    flags
    status {{
      id
      name
    }}
    email
    cancelled
    totalPrice{{
      withVat
      withoutVat
      currency {{
        code
      }}
    }}
    deliveryType{{
      id
      delivery{{
        id
        type
        name
        isInPerson
      }}
      payment{{
        id
        type
        name
      }}
    }}
    priceLevel{{
      id
      name
    }}
    invoiceAddress{{
      name
      surname
      firm
      phone
      ico
      dic
      street
      city
      zip
      country{{
        code
        name
      }}
    }}
    deliveryAddress{{
      name
      surname
      firm
      phone
      ico
      dic
      street
      city
      zip
      country{{
        code
        name
      }}
    }}
    packageId
    noteUser
    noteInvoice
    items{{
      id
      productId
      variationId
      pieces
      piecePrice{{
        withVat
        withoutVat
        vatValue
        vat
       currency {{
        code
        }}
      }}
      totalPrice{{
        withVat
        withoutVat
        vatValue
        vat
       currency {{
        code
        }}
      }}
      vat
      code
      product{{
        id
      }}
      type
      name
    }}
    isPaid
    paidPrice{{
      withVat
      withoutVat
      currency {{
        code
      }}
    }}
    remainingPayment{{
      price
      currency {{
        code
      }}
    }}
  }}
  hasNextPage
  hasPreviousPage
  }}
}}

    """


schema = [
  {"name": "id", "type": "INTEGER"},
  {"name": "source", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "source", "type": "STRING", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"}
    ]
  },
  {"name": "dateCreated", "type": "TIMESTAMP", "mode": "NULLABLE"},
  {"name": "dateAccept", "type": "TIMESTAMP", "mode": "NULLABLE"},
  {"name": "dateHandle", "type": "TIMESTAMP", "mode": "NULLABLE"},
  {"name": "dateUpdated", "type": "TIMESTAMP", "mode": "NULLABLE"},
  {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "code", "type": "STRING", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"},
      {"name": "symbol", "type": "STRING", "mode": "NULLABLE"},
      {"name": "rate", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "roundType", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "roundDirection", "type": "STRING", "mode": "NULLABLE"},
      {"name": "precision", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "decimalMark", "type": "STRING", "mode": "NULLABLE"}
    ]
  },
  {"name": "language", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "code", "type": "STRING", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"},
      {"name": "isActive", "type": "BOOLEAN", "mode": "NULLABLE"}
    ]
  },
  {"name": "currencyRate", "type": "NUMERIC", "mode": "NULLABLE"},
  {"name": "code", "type": "STRING", "mode": "NULLABLE"},
  {"name": "userId", "type": "INTEGER", "mode": "NULLABLE"},
  {"name": "flags", "type": "STRING", "mode": "REPEATED"},
  {"name": "status", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"}
    ]
  },
  {"name": "email", "type": "STRING", "mode": "NULLABLE"},
  {"name": "cancelled", "type": "BOOLEAN", "mode": "NULLABLE"},
  {"name": "totalPrice", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "withVat", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "withoutVat", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "code", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  },
  {"name": "deliveryType", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "delivery", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
          {"name": "type", "type": "STRING", "mode": "NULLABLE"},
          {"name": "name", "type": "STRING", "mode": "NULLABLE"},
          {"name": "isInPerson", "type": "BOOLEAN", "mode": "NULLABLE"}
        ]
      },
      {"name": "payment", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
          {"name": "type", "type": "STRING", "mode": "NULLABLE"},
          {"name": "name", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  },
  {"name": "priceLevel", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"}
    ]
  },
  {"name": "invoiceAddress", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "name", "type": "STRING", "mode": "NULLABLE"},
      {"name": "surname", "type": "STRING", "mode": "NULLABLE"},
      {"name": "firm", "type": "STRING", "mode": "NULLABLE"},
      {"name": "phone", "type": "STRING", "mode": "NULLABLE"},
      {"name": "ico", "type": "STRING", "mode": "NULLABLE"},
      {"name": "dic", "type": "STRING", "mode": "NULLABLE"},
      {"name": "street", "type": "STRING", "mode": "NULLABLE"},
      {"name": "city", "type": "STRING", "mode": "NULLABLE"},
      {"name": "zip", "type": "STRING", "mode": "NULLABLE"},
      {"name": "country", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "code", "type": "STRING", "mode": "NULLABLE"},
          {"name": "name", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  },
  {"name": "deliveryAddress", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "name", "type": "STRING", "mode": "NULLABLE"},
      {"name": "surname", "type": "STRING", "mode": "NULLABLE"},
      {"name": "firm", "type": "STRING", "mode": "NULLABLE"},
      {"name": "phone", "type": "STRING", "mode": "NULLABLE"},
      {"name": "ico", "type": "STRING", "mode": "NULLABLE"},
      {"name": "dic", "type": "STRING", "mode": "NULLABLE"},
      {"name": "street", "type": "STRING", "mode": "NULLABLE"},
      {"name": "city", "type": "STRING", "mode": "NULLABLE"},
      {"name": "zip", "type": "STRING", "mode": "NULLABLE"},
      {"name": "country", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "code", "type": "STRING", "mode": "NULLABLE"},
          {"name": "name", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  },
  {"name": "packageId", "type": "STRING", "mode": "NULLABLE"},
  {"name": "noteUser", "type": "STRING", "mode": "NULLABLE"},
  {"name": "noteInvoice", "type": "STRING", "mode": "NULLABLE"},
  {"name": "items", "type": "RECORD", "mode": "REPEATED",
    "fields": [
      {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "productId", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "variationId", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "pieces", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "piecePrice", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "withVat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "withoutVat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "vatValue", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "vat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
            "fields": [
              {"name": "code", "type": "STRING", "mode": "NULLABLE"}
            ]
          }
        ]
      },
      {"name": "totalPrice", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "withVat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "withoutVat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "vatValue", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "vat", "type": "NUMERIC", "mode": "NULLABLE"},
          {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
            "fields": [
              {"name": "code", "type": "STRING", "mode": "NULLABLE"}
            ]
          }
        ]
      },
      {"name": "vat", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "code", "type": "STRING", "mode": "NULLABLE"},
      {"name": "product", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "id", "type": "INTEGER", "mode": "NULLABLE"}
        ]
      },
      {"name": "type", "type": "STRING", "mode": "NULLABLE"},
      {"name": "name", "type": "STRING", "mode": "NULLABLE"}
    ]
  },
  {"name": "isPaid", "type": "BOOLEAN", "mode": "NULLABLE"},
  {"name": "paidPrice", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "withVat", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "withoutVat", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "code", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  },
  {"name": "remainingPayment", "type": "RECORD", "mode": "NULLABLE",
    "fields": [
      {"name": "price", "type": "NUMERIC", "mode": "NULLABLE"},
      {"name": "currency", "type": "RECORD", "mode": "NULLABLE",
        "fields": [
          {"name": "code", "type": "STRING", "mode": "NULLABLE"}
        ]
      }
    ]
  }
]
