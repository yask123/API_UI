
# Documentation 
A Web app and an API to crawl, index restaurant facebook pages and google places data.


### API End Point
```http://localhost:8000/ ```


To request data for the given query: 

###Required Parameters


* Facebook access token `fbtoken`

* Google API key `gkey` (Optional)

* Name of the restaurant `name`

* Location of restaurant `location`:

    Format (For City/State/Country) : `Delhi`

    Format (For latitude/longitude) : `lan:28.6139,77.2090`

### Example

```python
import requests

r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"fbtoken":token})
d = json.loads(r.text.strip())
```

```python
>>

```javascript
{
  'google': {
    u'status': u'OK',
    u'next_page_token': u'CoQC_gAAAKmR5ZdHrCzA5YxxXNE7V9Ku0CSuLfE5IqC_F-HrG7CVtPtdnS5Jtj101bk2apPGTHZrNlX_mSJfSmGuDMlaoUDS21vIuqc9wqjTbu0airMpTR-tlE_nSXYVayysNuwPXfpyWAaI1Cp0cZ7MSXFk0cG3BmTZKtGGgLyrMw_6kWQp62GJI8qEWTE_jFpk_pMUvfV_9UUrM36XaukYXXuvVvRFE6CGDTXz7AjmIF9T8ZNDi8N2Bc3eKDYGtCjxNYDYekiNcMZs2X8pmNX0h2PwOn_9ykc1QDiRX_eCryI2LyvRHT_R3-iC3jYz1-jNSsEVdn_TE4F1rD54xo5qWk1avQcSEHbnE583sF5dkWRbLicZ6xgaFDEraGYkl309epfbDoOiX0UM-Fdy',
    u'html_attributions': [
      
    ],
    u'results': [
      {
        u'rating': 4,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAi9s2DPwxabDznD4SEzfNhT57CIoS0tJQrsVUmGGgTzdb0y_VUXHEIUoSED50BUmCcTUs0blEOGNWQjBmstTbdM73tze7dsR9AJbnsz8HdM-yTtaMj7xoDKThRUCvwI_FEhCJtGky-DbtljKuj7JB15wEGhTiTB1yrwAMwiSfwYPuj62bPHWRjw',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.719354,
            u'lng': -73.9898599
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJvVFW2YZZwokRca6P_hbHpmY',
        u'vicinity': u'80 Delancey Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAjYPcQ7Eyaix4lrHzWsMIW6ol_gn1jxW3Gz1qaLsIi4VbQ3vQ2unWIr1Pueo8OQ2_Ei9QHv05ZXKnVuvDu2w5mPdBoLHSr_4crvJP5-4aBVqu17QpfVFUYo_peCcxuq4GEhCSQUs4qajtQCwzf-GXc3rdGhRRNzrwl1o1bwVl1-_Ho7c9zKXaiA',
            u'width': 4320,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/106905294470212349895/photos">David Sonenberg</a>'
            ],
            u'height': 2432
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'e493b381c69f56b47a2a616193d1138d930310ed',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.7,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAASVSLstOrUBlmgxrDYjlKXINK2pdwOFkWEWcFoBoOQmHy4QAVI-dwbu6P7I-yVt6vZ18gOIOVlY0f83EM6y2V5i_KnloUOj41KjXWzHiEOB4PNjYh228lv9T_EStmKOzTEhDIugmmYvoohZ7UkjkRBK3tGhSqFS4CFIXtF8H6-b8tno2ICCdtgg',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.73004459999999,
            u'lng': -73.9916187
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': True
        },
        u'place_id': u'ChIJ32Jzs5tZwokRzw5_7L6oZIw',
        u'vicinity': u'13-25 Astor Pl, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAqnv-SkqMV1bJpX502C3VCobv_iG8IMNowYqk2Ff59oOrgf8MCzi8qus62vbhaIMbfQ457oCB9QtPuQdUdZGm52PBFG1VZ4K4ORLVMGxsNu73ItOldruXucSlrk-P1JsREhCcdLeYZPy-Tx9TDbPj3P89GhQ6Jk6eEnZF27QTore-x424aG-oFQ',
            u'width': 540,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/100205296519265146560/photos">shosh lidor</a>'
            ],
            u'height': 720
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'1e42fb0568957adf5d4ec3b2759f0a5bdca1a340',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.5,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAKgB_O6ecUiYB5929TnJAINmoI71jGtrsOZBRBSrpr61Caz4e9R9EGIys3Pa037q81vwZCdky7cJWPakFYDVDhhFwsDGTneTmZmwgzCEYI6bHEaOCo64HG-Ew-r4BT0MaEhAT8PvKfyAc7FjDZFfW64W4GhRrWY01Q94O7sB7jIGlUX26n_FD7A',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.7464859,
            u'lng': -73.9811797
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJia3urglZwokREhcHn1iZURA',
        u'vicinity': u'3 Park Avenue, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAApZTLeKGMWRfVUWQroPMN8hMi1WBPJM1wTEoZ1KjL_qGWEhWGk6fk6PlIfL2O4cdtKqSkhCKoRJCzHdjHN0P5f1Kw9fXGAo8D5Monof4YuUHhFq_A2smnkYz5C2wVv-DQEhD5t5re9lmwKH1XIaMcuLlEGhSP-t2Wvg9Hzemb2tjkqe7cUERL1g',
            u'width': 3024,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/114965334346603311177/photos">Chad Ferrigno</a>'
            ],
            u'height': 4032
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'f91b0f99cb234d7ce5a23db8a61e40d3369242ce',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 2.8,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAKFv0hLL-ycLuTZS_esbsv57foOdJfHuuNsfKUu-LYJ9l-dVlVYXsH6qsdeKiJXVTjR3UtwWJqg1wQxDuEN1qX9kaOcgaW_4NSzsdJXKXNPl6OyNmtvQwJYuoet5QIWODEhBkh-FhBT10XOgf3G1taztCGhQtPvYhxkIOv2c7j_NNksi1az8hpg',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.7351621,
            u'lng': -73.9897853
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': True
        },
        u'place_id': u'ChIJ2RWg65hZwokRMf8jxA75sQc',
        u'vicinity': u'10 Union Square East, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAesHdgR_ojwHJU2zQ2bqfQs32Aj1KOeTq0Ufn8bXCJVJpu0j0F_rV80qacn9wZCh7h6TxnQC6gjAky5jHKN5XmkVTSE3MVKGcShk-nJ5KOJEjzITJbHF7TJG68XGYJWCOEhCTB6S43Ghu-HCOCBaF4WHgGhSmCXUWCuggmNKNt2v95WwV-ubqTw',
            u'width': 1367,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/116707993342200424883/photos">Mary Jones</a>'
            ],
            u'height': 2048
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'4685dd515cdbc7cb3b56a0ac09fa1ff576bf0725',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.9,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAAwyFUKQe-Cw6jyf5_MZvpK8Kvyrz1R_3R6prgc2mrecxQ9aV64DQH1WQKkwBEJYEld2Nwik3jyrvRzVf6EVpVjnPuJb0Y4iEIX4k8c5hyTE3vlq31xoHEHybCpFBtb8KGEhDF3y3UJOs02rWjMfCN1JNKGhTI6h4WngwvorsyGnJTXqiIrxLjTQ',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.7224935,
            u'lng': -73.99797459999999
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJLX0UK4lZwokRNfkbbR_8FKY',
        u'vicinity': u'72 Spring Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAjYQD5Af20cAu4TTrYw6oPeBcP17E4VHDGA-qj_X1VjRwdla90Yg_919OL24kmBirNPl62aKQlN9seBGaMZY6zqxNq1ULxCH_ix1OPk9M4XIzci0FTKy9_OBUFP4IYhHLEhD-p66DYB2HEqfZNDmf1YmVGhQsTTBPtrCGjDiaXNAHEiOZc2ke8Q',
            u'width': 3264,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/111334605353356844456/photos">Avijit Roy</a>'
            ],
            u'height': 2448
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'fdf6e00feb95882643ea98003f8380be2a39fc44',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.9,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAA9k6dOqkazQpBecKKwlCOdqa-p1LLXaC2OL-gioM7i3q8sMlwuMmT-Xl1PDNpuh_HL3oxgTi_Z_c-MY1ciQ1LkJObuK8RoP8wDuUFilyyY17SdYYzSYEMhQglmAKqKR2DEhC-UvU_dujltfb1Fe-hRX32GhQxgR1UlJh_UzYbgTFfCtR4e_K_Qw',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.754949,
            u'lng': -73.98375899999999
          }
        },
        u'place_id': u'ChIJ1cxOsapZwokR8mvP6PIyTS4',
        u'vicinity': u'1100 Avenue of the Americas, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAVTblo_aBHOGzazcqbamZKpHkUWWvtZ-ZxgsCTFqdkN5NMhBr3ZMgxOvk1jGI-96zT0v4pbKweet2z3LZFt4e7wuQ2NFEDoDh_fp9ABCbgYUN6YRYCU7YIPKq4oaxoWFJEhDbkgBeKh8J4DI4dZLc_sRqGhTvj0ido8ZSiUHx_GSzwR_ShE-QTw',
            u'width': 500,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/103619313090820100649/photos">Frank de Jong</a>'
            ],
            u'height': 335
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'a25a8ec76c0032a069fd1fb850cd205ee6277283',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.9,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAAIN8BJbRjv1EhHP_QL0q6vgQiwWB33OEgdhf1-oh7jYhzdgXKYvF2K7jT3xNakeB8jg5DjgpYsqPNZOOqtEASZrgbmy4SMMaVXqYnPsflr1DhlgeWgquXDxMgL68bl81SEhDgC3As51GEolh71DpozetqGhRfq-OUKZ3scTXSxtMft-db13H7Vg',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.67199950000001,
            u'lng': -73.9775236
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJmZQsMgFbwokRMc5I7kPdQ7w',
        u'vicinity': u'166 7th Avenue, Brooklyn',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAOcBHP4FoY0UefDFYMAQm0DZqt0e6sq28tZJbmyFHZW4j_IAkyddzkz1YBMF-bjiM59XPJnZK4h79pg-XAlaJq6JLu37xHhnyrgvA8R284SisZZCB9l5D446a8AoSzmLJEhDjvqPC7VdWRgLe0c29Mr94GhRNP7wdco7pluERx-9IJfq3eUsu3Q',
            u'width': 1632,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/103034974432133727755/photos">Rob Bbasso</a>'
            ],
            u'height': 1224
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'3d806cafdc6eb8e762ad788a1efc19321dedbd59',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 2.8,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAANAw4UXo8MQYpJp2jzI9rvwCayFOyBekQBxFNWfMHMZCGBlCZAEHj0MaNIY69X03IWJRNoY9cED50arSUsT7a-5KX0tD4qIxDyPmb5xlnHFctSwIwMWO1spoFkSYm6BXLEhBT2gzJKR8XiL1pQ9Z0E_pGGhQk9cftryrWmVeaCNxWl5uXLkU7ZQ',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.7362621,
            u'lng': -73.9911718
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': True
        },
        u'place_id': u'ChIJ3deGbaJZwokRjSujROirkNY',
        u'vicinity': u'25 Union Square West, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAANKHtT_64kCn4CKOWwja4PBHiEU30jyLxAQHyOoTjLhCcx7ho_TrcHl0VbF6ljLyY0Yp2DUhmapolxLqQ0AavFx0ZkspWZ4gi1JDctnWJGDnbkd_aF2NAtifxiYVc5yizEhDWD63tA30UeeiJgPDPaI_aGhSJ8PS_2KxCdH_EA77DURTS03REOg',
            u'width': 400,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/117564338870673968077/photos">Starbucks</a>'
            ],
            u'height': 400
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'10ef04499ccb856f167ef42e3b8639f0d3d17766',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.9,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAkCwlOen3xmO5gN_9L4tAxlVupb-AYclvPdkjPszG72Bt_jB3GqdYl9EFTzhd4o0KOEQumWEIs-ZMVILfvkjK_Rr-aW722BtGkmR6E--IlcRtgdZ5pqSXc1KuHmB_B34DEhC7vg9-y68Hwer0C1AlMKlBGhTHgqeV5QRBsY5F5QPxy-9FBbcGMw',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.7155201,
            u'lng': -74.0089091
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJ2yCB3B5awokRJgRjLuDLEQM',
        u'vicinity': u'125 Chambers Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAA5wwsvlxv6ikr68-D69YjYBikB2RfsXIz-AJ8YJ8TGbF6WRoiPeecw50qKCViuL4khSSSgxmTJl6tKI5vq2Zh6IgD7MXNyupkwfrfr0rIgwEMPLJGd5YvWz_TJg893RpfEhCy7YvZQkPwaO8NdiucTrx6GhRuBvTDV_ULioN9dDaJgSPiOy4wjQ',
            u'width': 1367,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/116707993342200424883/photos">Mary Jones</a>'
            ],
            u'height': 2048
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'd02253ea461efb6fd392ddda0a1b8e0b2e4deaf8',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.9,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAHzZEMZWKThzkCntkYiZulhFft5d8C0VzfvCtq3i1xarj1n1YJGOe00nO2SQ6i4_a5xoGVZf44mv0hFIImqRp-NurHVilHZAmotmYrWZpiVkqGd3zq8BIG28-cVxNo4ZyEhDQUOfPz8gFWFBsVYZgG2gKGhToMbHf8sOk6vzD4077Gb8OM5yGkA',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.75903299999999,
            u'lng': -73.973553
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJBxAIg_tYwokR5O-h2dmnWC4',
        u'vicinity': u'55 East 53rd Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAg2J_rU_nIIbdArJphnHaRsrz4siBySwTVzd0sQBpnncyHFqUYti7CigDXoMyTTNRt0f--hwhLMZ6vu4cGWTOXp587yI5Y82MckuUE7pshyeyXJ33-REG03-SUHQcKbocEhBcS4fYu-7f7BkUdZnL7z5UGhQOQjShCa80ehCQST23TC4BZtwPFA',
            u'width': 2048,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/108899565426739754518/photos">David Ratliff</a>'
            ],
            u'height': 1536
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'21c3818bc7346c6ea1b5bb68a5e3263e9b414199',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.4,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAAlZkK8b_DxEmLsGQcKRbMN1n-vnmq-gUFA2_bF4Fs0AjR9tl0YI8tWH6EttIuMOVRCkRll2zxQcO3MaIUyP87iC66KF8QTXxc0ADg8zFY9JZD-7DKlk5uKCGQXaRorgaCEhC5PyFx1JkE30u23SQZMV02GhQaMMWPvlRO2UA33NCi0Z1em6kidw',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.7742002,
            u'lng': -73.98141489999999
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': True
        },
        u'place_id': u'ChIJj8BYNvVYwokRfNpXqlyfA9s',
        u'vicinity': u'152, 154 Columbus Avenue, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAA2jsu8dd1lauS4BV2jrUmo2yCt1DRZlCKuaG7kXP2T9JChEg1lBgQ-LvDpwKEauuWV25TdI1goPf0l-cLXVvWhUtc2duGrBAKxw9ErEQvpayFpgU4gjlg_e9TrKhZoj-SEhCpxUmF9J-_eUfMIVvfjhX1GhSs2lZhAhIr5r5k0NjWGdajreiqxA',
            u'width': 2340,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/107085084639609629291/photos">Jamie Matthews</a>'
            ],
            u'height': 4160
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'b35ace473dac6978865307e9a43bff11cbce71af',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAATS3pDa6Kp5NFvbVgzo-SkKu62tP2YfPRKzPrtr-4oT9XUJLgTGhUBqMxp09ICx3K3NMSmwsu9MVAafqPfjZAiskNQMjb3_QWDIm6rgd_CZjBsyHRJUCve6QYjCY2_lPVEhCwy6UMevohNLwAglrZiJHxGhSgoqs1OIxJHMv0KAcTXCgO_Z2Svw',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.7549915,
            u'lng': -73.9732619
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJgxIiE_1YwokR9gveeNwG8GU',
        u'vicinity': u'511 Lexington Avenue, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAKfTU7KNMNqDYj_omMZGHX_u_fhiiAI8E7gntFkc_9AbUY_v-iEwBu0E7ZMkUapm1jFzb2v2Rl_1CgQPN3JP8M3tLNZAf4CZR6x1se4WCWmZ6mzDKyHs-Xt3RdoeBQ-zrEhBPbVwysI__5R1-vRy8uCFbGhR3goeY1OtJN2QXEzRi6q0S4RIe7w',
            u'width': 400,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/108183677254950055001/photos">Starbucks</a>'
            ],
            u'height': 400
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'3a6161b0e070e00ca97529777d24b419a1765061',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.1,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAAHenvy2wy1vfPbTpF5rXCjiM8HZ7C00DZlPJT9Z1fmp34nfC9DWaAeZ39Y0P6Rc_QMl98rH_pB7MAn7R0bEQZkw3ezwj7Qh8Oahhv62l09-PXCaoDdmeovATt_BGwitRbEhC3SLTm6B7gyU6QcSrGk5lqGhTnzTwhDThIv1so4jI57WQsuTR2Fg',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.7257744,
            u'lng': -74.0055885
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJ95Cz24xZwokR7UvY056lTb0',
        u'vicinity': u'150 Varick Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAoHFhf9GANNFbiCUUBU6UVMsIodtqyG-ghMnCRjK1aoyFzN-Y_NTwENOxOE4tNQGH41qJPEpkoOyKCYbWzBORluo0Y0wrbxK6DC3NxPiJP6U4hYmPICOGaBIsE05RBpyYEhCv-Qr3ow54YXUY36BzJ-ZEGhQXFFZ-jTkGDxbx4Ir9l2W3_xgHhw',
            u'width': 4160,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/105244083683855824201/photos">Vlad Gydz</a>'
            ],
            u'height': 2340
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'09331084b9917d1dbea5789c14b17d9b10b564ab',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.5,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAT03G1mRGMTjTiTs8clovtxRjbnDVWNqkoOIOVXZ7CAvf3LwiUEcnP8WwlUg3-1T2e3OpbxtaHP8J57kGGbbqjHSTr5BIXyiJSWdBQNajMDzFLa3n8A9-t5slWpsKIp-TEhC7rKip6BY0IcNghrzNUjreGhQTxOdhXNvO3ugdAhZzCeoJXg_Ebg',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.75129039999999,
            u'lng': -73.99230159999999
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': True
        },
        u'place_id': u'ChIJhZJ3Yq5ZwokRdFC1fLmEsyg',
        u'vicinity': u'1 Pennsylvania Plaza, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAQ5Kw9FspOgMvpRXd5kwCvG1Wjiiy-snNpjAYwG2iKUYS-aC9FOunlVEw3L4_lXtRMg_PjhA4OHpD59fz9kKaLwdfHp3_0-ghJqNAzIst3rC26dwdAaiBacOc8UoUJmrbEhBe91Lk0-s7_9G5K6y-XUywGhRycNlaWAzZttGsxa5Z3SH2nXdLpg',
            u'width': 2592,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/105170431124683218627/photos">Marc Gonzalez</a>'
            ],
            u'height': 1936
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'31ac69f9fb0331596eebf55da5eee9d4c02c836b',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.5,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAuUWyoLzDKVkBhTJCQ128IhUEQOchZkxEv8ccXAavgQGOUFy7fXR5ENdnyK3bOB9jNxeSktibmpEZ0x63xQ9gxzbBz6ABp-5gHxQ_tTod3-S_6mawiC-bJV2gOSllHqevEhB0AQdyWe9uw3vgSuv38KUBGhQNg8pAO8-yw7N9KpYyyHVExZNZbw',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.7554999,
            u'lng': -73.9802899
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJH7uQZ_5YwokRyKuuVx5pkUQ',
        u'vicinity': u'2 West 45th Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAcNvSZN39gY3OZuNyKa4E3B5ftz9OZtc0ApW8sePN5k-iJOhvOc034gsSvKV9KjAkKL4-zaKRMUGrA0Lth3aDz2LSag_gjX_J3rUx910Dz8ucGY0hQESQtwAhp_YOSv7yEhAJh37X38A6aae19CsiMWrgGhR6mtZWgGL0eJQ6WLPMn5bmcZmCnQ',
            u'width': 256,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/112626678228222759641/photos">Starbucks</a>'
            ],
            u'height': 256
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'653b34c7531e0e51baff4a2c6b27c7d0bee06de2',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 4.2,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAACPTNwzvgdl7p3x4jcaSWfZCMtR-92Tx30YhmApR2iW1WzCAjo9tBsXHgWYU5Eb0PiE6nTV7-py60sVnHuDNW3SR9k_Pemg5cYRJ5utuWhstGFNKV80pf50YGDCWB5dxOEhDWTZ_mL2l_QJegrhRzhuE0GhQoEsYwkj2EBOIUXghp8sqynRXztg',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.718977,
            u'lng': -74.0026409
          }
        },
        u'place_id': u'ChIJu8aMcYpZwokRzVfQPOOztLw',
        u'vicinity': u'405 Broadway, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAApR_WhWgtLx6pTylWRa7PIXijGeFhzrP0zte2m7pKwEeC_ub9CAeLeoM0YzqxOECBOPDt1aoFE6Nx-XsIyxyr913Vh00kJoiLphT7TkzFU4mEDH5b14COUpsxCkKDgz0AEhCkpMdtljgiSoe9FLIT7ZFuGhRboUIpYikaGAsH_83Er2kSoc2C8Q',
            u'width': 1367,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/116707993342200424883/photos">Mary Jones</a>'
            ],
            u'height': 2048
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'4536be39f8cfd64fe0fb25025b109f16559eff58',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.8,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAA-S8L0r0l--DG8zK_1Y_DRwSY8sW_-UT3dALNfbXXc2yNhpDnFDm2IY_BfJI_kCvm0ZhO2vS5yZO2Oldy_sXMoHXYDCPEtJEbSrB0oeFqdCK9yNRDLPId1LYmMLW5IYC-EhAXATftBGp-LHx9PsmE7DdhGhSar5RMtl5fVChsdiRHull1-k6nIA',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.74691,
            u'lng': -73.9930926
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJ9deo9K9ZwokRBVZ4XIIK5oM',
        u'vicinity': u'315 7th Avenue, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAH7NgOTGcKlxFYENE3uhTrTc1QG-7CFPLMWemop6evjwbczcsPdR0VCXTEdlxClEFUcLRiBBqBhE0yhAgd6-tzbE5bTRyUhTEqn6lw8qKjJW0g4JSrF7doYk5o12u70IkEhDjpoqc3NHURxAna7FTfkdOGhQNtxmmHyQSh6FES4aBuuNXdKZOEw',
            u'width': 4032,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/112393954559953303137/photos">Brent Unkrich</a>'
            ],
            u'height': 3024
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'0d46b07340173574b013fbbf4c6e01b5fe6b1ddf',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.8,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAmp1ZulAXo5puZzHAiHfcc19C8JRT3vAGsBJjYcRptEDLOw0M-EX7J0CgAU3g2cVh2zbSq18XxLlAcuemX2ySYyRBHxnwX9rRVXeMiUs1iXAZ0oO1YSL_WgknVbPZrx9IEhCgw10KCEVm47fCZ_Qx0L50GhTgGky2FeS8UJQSCjSWXvw64kF48Q',
        u'price_level': 1,
        u'geometry': {
          u'location': {
            u'lat': 40.7401405,
            u'lng': -73.9869456
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJqSFfJaFZwokRydO3XgBwnAM',
        u'vicinity': u'304 Park Avenue South, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAACnaXbqILPMZMKklqx88GvocXcOdLzi4ji1axkR3h1t5rnXoij9jah3N47X0NwtUqFhFL2XDlMd8MXibL-WRk6vyWmtPmZ977B7Qx01W3cf77yaz5TXgn5uebA0sV9GRjEhD66Xln9f74BfruXvOnn_3QGhTX8A3EPD7OdILF4sjn0y7KbtHDYg',
            u'width': 4032,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/114622854862828727540/photos">Zev Safran</a>'
            ],
            u'height': 3024
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'aa0acda0a950f2d3bb5b0fa2e03ec83a9ec426a7',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'rating': 3.6,
        u'name': u'Starbucks',
        u'reference': u'CmRdAAAAqHKuik1FJCkRyvMYN_NgGhqJTkSfBGHJp9T-ZflAJVwelGjBvZlnzvWza1CbG1robcu-J0QSewJ4wjPkmLtSseTG-WtrFRS2NbDf4-1ucd0udLhJFCKlIQ1qWsM3q6bpEhCN8zBGK4WzrN7Mhl-iXndDGhR7mAeBVkjMgRjSM8TAy07AxFZLpw',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.758411,
            u'lng': -73.9742152
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJ9Xa3YvxYwokRyDd_Bsi1VrE',
        u'vicinity': u'45 East 51st Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAxpaGV5apxbVNkFHN8Bo9u62pkII-856GKbWZpeEc4bnp8lVtd3DD78J1IpID5xduhfiJhuFgnPAQEWr6QQMN4YqX2aOjUp15Ahw5PwY2TF-_n_Mj8Ob2KySR2Mc0UnD9EhBvc4D3iUgb3huiu1X06TtoGhRTAv23Hmeewh9BZVOApSRvTdpsTA',
            u'width': 400,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/106617928628008038869/photos">Starbucks</a>'
            ],
            u'height': 400
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'bd36ce99babecf09778c1fc150464312d38660ec',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      {
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAeU-x45GSdbQ2V1kKLdhKwxX2Nlik5JdlvpDqJb_Lts6r9DoqJqYZahDi9FtQTiljqfHG99pllWTywWfAkgYkmsacVpFUSK2Yj8iPNqKmDxCcr4sI36J8TWdmTZAmHJ9WEhCtbFT4ouRwvDg5QlDBbw2XGhS1yCtAbEkaTCOfxDI78XNNTU2UpQ',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.75681929999999,
            u'lng': -73.9726963
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJtYiIwvxYwokRMUB-AUgZgmU',
        u'vicinity': u'560 Lexington Avenue, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAnvkDhCQFWKwR3iepsqbL9RkWLFaU-j572qJOmkr2gZfeG8mDtmBHuta2KH-3T794oeC8dT-FDL9EMCHaKdgZ1IK1bXumO4RxTA9qhpLBH8ftYcaMMRWS5Yya-4COtZYREhATA9xWt0CahcJAtuZV6K4TGhT7yyg3L59vV8Dgj1emrGBkPlNJRg',
            u'width': 400,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/110693652775849945879/photos">Starbucks</a>'
            ],
            u'height': 400
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'16b8cfcd94be55f434017e1379592518dc2f382f',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      }
    ]
  },
  'facebook': {
    'website': 'www.starbucks.com ',
    'name': 'Starbucks',
    'parking': "{u'street': 0, u'lot': 0, u'valet': 0}",
    'hours': "{u'sun_1_close': u'22:30', u'sat_1_close': u'23:00', u'sun_1_open': u'07:00', u'fri_1_close': u'23:00', u'thu_1_open': u'06:00', u'tue_1_close': u'23:00', u'sat_1_open': u'06:30', u'mon_1_open': u'06:00', u'mon_1_close': u'23:00', u'wed_1_open': u'06:00', u'wed_1_close': u'23:00', u'tue_1_open': u'06:00', u'fri_1_open': u'06:00', u'thu_1_close': u'23:00'}",
    'phone': '(212) 780-0027',
    'location': "{u'city': u'New York', u'zip': u'100035703', u'country': u'United States', u'longitude': Decimal('-73.9874725'), u'state': u'NY', u'street': u'145 2nd Ave', u'latitude': Decimal('40.7294388')}",
    'fb_page_url': u'http://facebook.com/149957095031686',
    'is_verified': 'False',
    'likes': '244'
  }
}
```

  

