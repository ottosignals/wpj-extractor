gql_query="""
query users {{
    users(
        offset: {offset},
        limit: {limit},
        userSort: {sort}
    ) 
    {{
        hasNextPage
        hasPreviousPage
        items {{
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
            gender
            isActive
            newsletterInfo {{
                isSubscribed
                dateSubscribe
                dateUnsubscribe
            }}
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
        }}
    }}
}}
"""

bq_schema=[
      {
        "name": "invoiceAddress",
        "type": "RECORD",
        "description": "Fakturacni adresa",
        "fields": [
          {"name": "name", "type": "STRING", "description": "Jmeno"},
          {"name": "surname", "type": "STRING", "description": "Prijmeni"},
          {"name": "firm", "type": "STRING", "description": "Firma"},
          {"name": "phone", "type": "STRING", "description": "Telefon"},
          {"name": "ico", "type": "STRING", "description": "ICO"},
          {"name": "dic", "type": "STRING", "description": "DIC"},
          {"name": "street", "type": "STRING", "description": "Ulice a cislo popisne"},
          {"name": "city", "type": "STRING", "description": "Mesto"},
          {"name": "zip", "type": "STRING", "description": "Postovni smerovaci cislo"},
          {"name": "country", "type": "RECORD", "description": "Zeme",
            "fields": [
              {"name": "code", "type": "STRING", "description": "Kod zeme"},
              {"name": "name", "type": "STRING", "description": "Nazev zeme"}
            ]
          }
        ]
      },
      {
        "name": "deliveryAddress",
        "type": "RECORD",
        "description": "Dodaci adresa",
        "fields": [
          {"name": "name", "type": "STRING", "description": "Jmeno"},
          {"name": "surname", "type": "STRING", "description": "Prijmeni"},
          {"name": "firm", "type": "STRING", "description": "Firma"},
          {"name": "phone", "type": "STRING", "description": "Telefon"},
          {"name": "ico", "type": "STRING", "description": "ICO"},
          {"name": "dic", "type": "STRING", "description": "DIC"},
          {"name": "street", "type": "STRING", "description": "Ulice a cislo popisne"},
          {"name": "city", "type": "STRING", "description": "Mesto"},
          {"name": "zip", "type": "STRING", "description": "Postovni smerovaci cislo"},
          {"name": "country", "type": "RECORD", "description": "Zeme",
            "fields": [
              {"name": "code", "type": "STRING", "description": "Kod zeme"},
              {"name": "name", "type": "STRING", "description": "Nazev zeme"}
            ]
          }
        ]
      },
      {"name": "gender", "type": "STRING", "description": "Pohlavi"},
      {"name": "isActive", "type": "BOOLEAN", "description": "Vraci, zda je uzivatel aktivni"},
      {
        "name": "newsletterInfo",
        "type": "RECORD",
        "description": "Informace o odběru newsletteru",
        "fields": [
          {"name": "isSubscribed", "type": "BOOLEAN", "description": "Vraci, zda je uzivatel prihlasen k newsletteru"},
          {"name": "dateSubscribe", "type": "TIMESTAMP", "description": "Datum prihlaseni k newsletteru"},
          {"name": "dateUnsubscribe", "type": "TIMESTAMP", "description": "Datum odhlaseni od newsletteru"}
        ]
      },
      {"name": "dateRegistered", "type": "TIMESTAMP", "description": "Datum registrace. If the registration date is null, the user is not registered but may be subscribed to the newsletter"},
      {"name": "dateUpdated", "type": "TIMESTAMP", "description": "Datum posledni zmeny"},
      {"name": "dateLogged", "type": "TIMESTAMP", "description": "Datum posledniho prihlaseni"},
      {"name": "note", "type": "STRING", "description": "Poznamka nastavena administratorem u uzivatele"},
      {"name": "bonusPoints", "type": "INTEGER", "description": "Pocet bodu v bonusovem programu"},
      {"name": "id", "type": "INTEGER", "description": "ID uzivatele"},
      {"name": "email", "type": "STRING", "description": "E-mail"},
      {"name": "name", "type": "STRING", "description": "Jmeno"},
      {"name": "surname", "type": "STRING", "description": "Prijmeni"},
      {"name": "userName", "type": "STRING", "description": "Cele jmeno"},
      {"name": "isB2B", "type": "BOOLEAN", "description": "Vraci, zda je uzivatel B2B"}
    ]
