import json
def items_data_import():
    my_json_string = """[
        {
            "item_amount": 1 ,
            "item_code": "1567153058",
            "item_description": "בגד ים רעות",
            "item_price": 86.39        },
        {
            "item_amount": 1 ,
            "item_code": "4090212978",
            "item_description": "בגד ים תבור",
            "item_price": 76.22        },
        {
            "item_amount": 1 ,
            "item_code": "9673461660",
            "item_description": "בגד ים רם",
            "item_price": 60.59        },
        {
            "item_amount": 1 ,
            "item_code": "14378797",
            "item_description": "בגד ים זיו",
            "item_price": 78.59        },
        {
            "item_amount": 1 ,
            "item_code": "2323505426",
            "item_description": "בגד ים דוראל",
            "item_price": 92.86        },
        {
            "item_amount": 1 ,
            "item_code": "8347090920",
            "item_description": "בגד ים תאיר",
            "item_price": 90.56        },
        {
            "item_amount": 1 ,
            "item_code": "6442266320",
            "item_description": "בגד ים אושרת",
            "item_price": 88.09        },
        {
            "item_amount": 1 ,
            "item_code": "4277049644",
            "item_description": "גינס מישל",
            "item_price": 122.24        },
        {
            "item_amount": 1 ,
            "item_code": "1237958321",
            "item_description": "גינס רונן",
            "item_price": 213.15        },
        {
            "item_amount": 1 ,
            "item_code": "5755760511",
            "item_description": "גינס אלישע",
            "item_price": 194.36        },
        {
            "item_amount": 1 ,
            "item_code": "8277664659",
            "item_description": "גינס אמונה",
            "item_price": 186.39        },
        {
            "item_amount": 1 ,
            "item_code": "9570471151",
            "item_description": "גינס אורין",
            "item_price": 126.94        },
        {
            "item_amount": 1 ,
            "item_code": "1121314223",
            "item_description": "גינס חן",
            "item_price": 124.12        },
        {
            "item_amount": 1 ,
            "item_code": "7107371931",
            "item_description": "גינס אבנר",
            "item_price": 141.59        },
        {
            "item_amount": 1 ,
            "item_code": "3847258194",
            "item_description": "גופייה עידן",
            "item_price": 30.03        },
        {
            "item_amount": 1 ,
            "item_code": "4336335417",
            "item_description": "גופייה רוחמה",
            "item_price": 44.8        },
        {
            "item_amount": 1 ,
            "item_code": "1876310733",
            "item_description": "גופייה יוני",
            "item_price": 21.34        },
        {
            "item_amount": 1 ,
            "item_code": "1144365327",
            "item_description": "גופייה מורי",
            "item_price": 25.44        },
        {
            "item_amount": 1 ,
            "item_code": "7960913741",
            "item_description": "גופייה בילא",
            "item_price": 31.71        },
        {
            "item_amount": 1 ,
            "item_code": "8334595892",
            "item_description": "גופייה נבו",
            "item_price": 34.22        },
        {
            "item_amount": 1 ,
            "item_code": "4886208920",
            "item_description": "גופייה שגיב",
            "item_price": 42.98        },
        {
            "item_amount": 1 ,
            "item_code": "8366833108",
            "item_description": "גרביים גבע",
            "item_price": 16.48        },
        {
            "item_amount": 1 ,
            "item_code": "2188909149",
            "item_description": "גרביים יקותיאל",
            "item_price": 18.84        },
        {
            "item_amount": 1 ,
            "item_code": "3590730394",
            "item_description": "גרביים תאיר",
            "item_price": 17.52        },
        {
            "item_amount": 1 ,
            "item_code": "8620937768",
            "item_description": "גרביים מנשה",
            "item_price": 15.83        },
        {
            "item_amount": 1 ,
            "item_code": "8298880684",
            "item_description": "גרביים גאיה",
            "item_price": 18.6        },
        {
            "item_amount": 1 ,
            "item_code": "1161446598",
            "item_description": "גרביים שיינדל",
            "item_price": 13.69        },
        {
            "item_amount": 1 ,
            "item_code": "3224845125",
            "item_description": "גרביים ארבל",
            "item_price": 10.44        },
        {
            "item_amount": 1 ,
            "item_code": "6154779658",
            "item_description": "חולצה דור",
            "item_price": 85.12        },
        {
            "item_amount": 1 ,
            "item_code": "8267878129",
            "item_description": "חולצה אלישי",
            "item_price": 59.06        },
        {
            "item_amount": 1 ,
            "item_code": "2181188572",
            "item_description": "חולצה זואי",
            "item_price": 50.45        },
        {
            "item_amount": 1 ,
            "item_code": "9254828509",
            "item_description": "חולצה בועז",
            "item_price": 71.95        },
        {
            "item_amount": 1 ,
            "item_code": "951347380",
            "item_description": "חולצה אורלי",
            "item_price": 88.12        },
        {
            "item_amount": 1 ,
            "item_code": "3549240856",
            "item_description": "חולצה עמרם",
            "item_price": 75.25        },
        {
            "item_amount": 1 ,
            "item_code": "3859434799",
            "item_description": "חולצה בלומה",
            "item_price": 41.91        },
        {
            "item_amount": 1 ,
            "item_code": "2567674848",
            "item_description": "חצאית משולם",
            "item_price": 48.89        },
        {
            "item_amount": 1 ,
            "item_code": "2822612502",
            "item_description": "חצאית חן",
            "item_price": 98.33        },
        {
            "item_amount": 1 ,
            "item_code": "3105120606",
            "item_description": "חצאית שגיא",
            "item_price": 70.87        },
        {
            "item_amount": 1 ,
            "item_code": "9695831211",
            "item_description": "חצאית דוד",
            "item_price": 96.13        },
        {
            "item_amount": 1 ,
            "item_code": "4717237273",
            "item_description": "חצאית יוחנן",
            "item_price": 85.09        },
        {
            "item_amount": 1 ,
            "item_code": "9893755999",
            "item_description": "חצאית עופרי",
            "item_price": 97.23        },
        {
            "item_amount": 1 ,
            "item_code": "7116759003",
            "item_description": "חצאית דוריה",
            "item_price": 73.31        },
        {
            "item_amount": 1 ,
            "item_code": "7683336736",
            "item_description": "כובע יסכה",
            "item_price": 37        },
        {
            "item_amount": 1 ,
            "item_code": "2374403595",
            "item_description": "כובע רן",
            "item_price": 39.12        },
        {
            "item_amount": 1 ,
            "item_code": "1847246172",
            "item_description": "כובע יוכבד",
            "item_price": 36.47        },
        {
            "item_amount": 1 ,
            "item_code": "7481941666",
            "item_description": "כובע גולדה",
            "item_price": 32.93        },
        {
            "item_amount": 1 ,
            "item_code": "1814452798",
            "item_description": "כובע ירחמיאל",
            "item_price": 21.34        },
        {
            "item_amount": 1 ,
            "item_code": "4094717382",
            "item_description": "כובע טוהר",
            "item_price": 31.48        },
        {
            "item_amount": 1 ,
            "item_code": "834844617",
            "item_description": "כובע אן",
            "item_price": 34.42        },
        {
            "item_amount": 1 ,
            "item_code": "3956417719",
            "item_description": "מכנס כרמל",
            "item_price": 151.32        },
        {
            "item_amount": 1 ,
            "item_code": "1421428200",
            "item_description": "מכנס יששכר",
            "item_price": 129.67        },
        {
            "item_amount": 1 ,
            "item_code": "5242526260",
            "item_description": "מכנס אוריה",
            "item_price": 100.59        },
        {
            "item_amount": 1 ,
            "item_code": "3333654661",
            "item_description": "מכנס עומר",
            "item_price": 126.7        },
        {
            "item_amount": 1 ,
            "item_code": "916434390",
            "item_description": "מכנס ישי",
            "item_price": 125.52        },
        {
            "item_amount": 1 ,
            "item_code": "9866980351",
            "item_description": "מכנס ישי",
            "item_price": 118.26        },
        {
            "item_amount": 1 ,
            "item_code": "1377096420",
            "item_description": "מכנס יהלי",
            "item_price": 160.26        },
        {
            "item_amount": 1 ,
            "item_code": "4188115870",
            "item_description": "מעיל אפיק",
            "item_price": 253.07        },
        {
            "item_amount": 1 ,
            "item_code": "5020662743",
            "item_description": "מעיל מינדל",
            "item_price": 319.61        },
        {
            "item_amount": 1 ,
            "item_code": "4076995261",
            "item_description": "מעיל מירל",
            "item_price": 233.16        },
        {
            "item_amount": 1 ,
            "item_code": "655519501",
            "item_description": "מעיל אלחנן",
            "item_price": 205.93        },
        {
            "item_amount": 1 ,
            "item_code": "3402258248",
            "item_description": "מעיל דור",
            "item_price": 272.35        },
        {
            "item_amount": 1 ,
            "item_code": "2159477502",
            "item_description": "מעיל גפן",
            "item_price": 269.92        },
        {
            "item_amount": 1 ,
            "item_code": "6396222421",
            "item_description": "מעיל שיר",
            "item_price": 247.33        },
        {
            "item_amount": 1 ,
            "item_code": "7349142410",
            "item_description": "נעלי ילדים ליאור",
            "item_price": 97.82        },
        {
            "item_amount": 1 ,
            "item_code": "9119949807",
            "item_description": "נעלי ילדים רומי",
            "item_price": 116.36        },
        {
            "item_amount": 1 ,
            "item_code": "8830880342",
            "item_description": "נעלי ילדים ענר",
            "item_price": 147.58        },
        {
            "item_amount": 1 ,
            "item_code": "8686131268",
            "item_description": "נעלי ילדים טלי",
            "item_price": 133.78        },
        {
            "item_amount": 1 ,
            "item_code": "951855045",
            "item_description": "נעלי ילדים עילאי",
            "item_price": 128.62        },
        {
            "item_amount": 1 ,
            "item_code": "1056621109",
            "item_description": "נעלי ילדים ינון",
            "item_price": 89.73        },
        {
            "item_amount": 1 ,
            "item_code": "163486778",
            "item_description": "נעלי ילדים אלן",
            "item_price": 126.03        },
        {
            "item_amount": 1 ,
            "item_code": "8227128675",
            "item_description": "נעלי ספורט Nike",
            "item_price": 308.19        },
        {
            "item_amount": 1 ,
            "item_code": "7367332799",
            "item_description": "נעלי ספורט ניו-באלאנס",
            "item_price": 329.21        },
        {
            "item_amount": 1 ,
            "item_code": "6306227806",
            "item_description": "נעלי ספורט ריבוק",
            "item_price": 308.81        },
        {
            "item_amount": 1 ,
            "item_code": "3288667612",
            "item_description": "נעלי ספורט אדידס",
            "item_price": 384.15        },
        {
            "item_amount": 1 ,
            "item_code": "5821355363",
            "item_description": "נעלי ספורט ניו-באלאנס",
            "item_price": 327.89        },
        {
            "item_amount": 1 ,
            "item_code": "2512084877",
            "item_description": "נעלי ספורט SKECHERS",
            "item_price": 411.61        },
        {
            "item_amount": 1 ,
            "item_code": "7635625467",
            "item_description": "נעלי ספורט ריבוק",
            "item_price": 448.86        },
        {
            "item_amount": 1 ,
            "item_code": "4664928890",
            "item_description": "נעלי עקב אסנת",
            "item_price": 182.44        },
        {
            "item_amount": 1 ,
            "item_code": "7091053874",
            "item_description": "נעלי עקב רייזל",
            "item_price": 158.81        },
        {
            "item_amount": 1 ,
            "item_code": "2973196240",
            "item_description": "נעלי עקב אמלי",
            "item_price": 160.32        },
        {
            "item_amount": 1 ,
            "item_code": "767910336",
            "item_description": "נעלי עקב ליאת",
            "item_price": 172.97        },
        {
            "item_amount": 1 ,
            "item_code": "2690133704",
            "item_description": "נעלי עקב אריאל",
            "item_price": 164.02        },
        {
            "item_amount": 1 ,
            "item_code": "2524464684",
            "item_description": "נעלי עקב נח",
            "item_price": 160.21        },
        {
            "item_amount": 1 ,
            "item_code": "2276574390",
            "item_description": "נעלי עקב אביגיל",
            "item_price": 122.26        },
        {
            "item_amount": 1 ,
            "item_code": "5953772362",
            "item_description": "עליונית שחף",
            "item_price": 58.6        },
        {
            "item_amount": 1 ,
            "item_code": "8513106408",
            "item_description": "עליונית מנור",
            "item_price": 62.58        },
        {
            "item_amount": 1 ,
            "item_code": "4988962822",
            "item_description": "עליונית עמרם",
            "item_price": 118.52        },
        {
            "item_amount": 1 ,
            "item_code": "7260536112",
            "item_description": "עליונית לוטם",
            "item_price": 53.88        },
        {
            "item_amount": 1 ,
            "item_code": "9446668118",
            "item_description": "עליונית אלומה",
            "item_price": 59.13        },
        {
            "item_amount": 1 ,
            "item_code": "293114671",
            "item_description": "עליונית נעמי",
            "item_price": 65.71        },
        {
            "item_amount": 1 ,
            "item_code": "5653074818",
            "item_description": "עליונית עיליי",
            "item_price": 91.73        },
        {
            "item_amount": 1 ,
            "item_code": "4741779858",
            "item_description": "שמלה מישל",
            "item_price": 204.01        },
        {
            "item_amount": 1 ,
            "item_code": "3276404751",
            "item_description": "שמלה לני",
            "item_price": 221.28        },
        {
            "item_amount": 1 ,
            "item_code": "2766135554",
            "item_description": "שמלה ירין",
            "item_price": 200.19        },
        {
            "item_amount": 1 ,
            "item_code": "5108103229",
            "item_description": "שמלה יעל",
            "item_price": 237.58        },
        {
            "item_amount": 1 ,
            "item_code": "5328806471",
            "item_description": "שמלה מוריאל",
            "item_price": 198.31        },
        {
            "item_amount": 1 ,
            "item_code": "9625998436",
            "item_description": "שמלה יובל",
            "item_price": 182.24        },
        {
            "item_amount": 1 ,
            "item_code": "4270315532",
            "item_description": "שמלה ליעוז",
            "item_price": 233.75        },
        {
            "item_amount": 1 ,
            "item_code": "9700861624",
            "item_description": "בנזין 95",
            "item_price": 5.67        },
        {
            "item_amount": 1 ,
            "item_code": "8259942840",
            "item_description": "סולר",
            "item_price": 6.84        },
       
        {
            "item_amount": 1 ,
            "item_code": "6740288747",
            "item_description": "ארוחת בוקר זוגית",
            "item_price": 137.64        },
        {
            "item_amount": 1 ,
            "item_code": "1157870899",
            "item_description": "ארוחת בוקר יחיד",
            "item_price": 80.90        },
        {
            "item_amount": 1 ,
            "item_code": "5393856936",
            "item_description": "בירה 02",
            "item_price": 34.60        },
        {
            "item_amount": 1 ,
            "item_code": "580809573",
            "item_description": "בירה 01",
            "item_price": 30.84        },
        {
            "item_amount": 1 ,
            "item_code": "4502023846",
            "item_description": "המבורגר 100 גר",
            "item_price": 50.59        },
        {
            "item_amount": 1 ,
            "item_code": "2090368387",
            "item_description": "המבורגר 250 גר",
            "item_price": 80.90        },
        {
            "item_amount": 1 ,
            "item_code": "8320468950",
            "item_description": "המבורגר 500 גר",
            "item_price": 101.67        },
        {
            "item_amount": 1 ,
            "item_code": "1236533110",
            "item_description": "כריך טונה",
            "item_price": 44.09        },
        {
            "item_amount": 1 ,
            "item_code": "7967399953",
            "item_description": "כריך חלומי",
            "item_price": 44.34        },
        {
            "item_amount": 1 ,
            "item_code": "226114414",
            "item_description": "משקה קל",
            "item_price": 11.91        },
        {
            "item_amount": 1 ,
            "item_code": "59717864",
            "item_description": "עוגה",
            "item_price": 34.92        },
        {
            "item_amount": 1 ,
            "item_code": "7462763763",
            "item_description": "פוטטו קטן",
            "item_price": 25.19        },
        {
            "item_amount": 1 ,
            "item_code": "2892117491",
            "item_description": "פוטטו גדול",
            "item_price": 34.96        },
        {
            "item_amount": 1 ,
            "item_code": "985142542",
            "item_description": "פסטה",
            "item_price": 59.89        },
        {
            "item_amount": 1 ,
            "item_code": "8789717845",
            "item_description": "ציפס קטן",
            "item_price": 20.14        },
        {
            "item_amount": 1 ,
            "item_code": "1618951354",
            "item_description": "ציפס גדול",
            "item_price": 27.39        },
        {
            "item_amount": 1 ,
            "item_code": "2964940852",
            "item_description": "קפה בינוני",
            "item_price": 16.63        },
        {
            "item_amount": 1 ,
            "item_code": "7929784751",
            "item_description": "קפה גדול",
            "item_price": 19.48        },
        {
            "item_amount": 1 ,
            "item_code": "5790929069",
            "item_description": "קפה קטן",
            "item_price": 12.63        },
        {
            "item_amount": 1 ,
            "item_code": "7947555671",
            "item_description": "טלויזיה דגם 07",
            "item_price": 2116.62        },
        {
            "item_amount": 1 ,
            "item_code": "914926804",
            "item_description": "טלויזיה דגם 03",
            "item_price": 5533.30        },
        {
            "item_amount": 1 ,
            "item_code": "4819614243",
            "item_description": "טלויזיה דגם 01",
            "item_price": 1941.80        },
        {
            "item_amount": 1 ,
            "item_code": "7983359133",
            "item_description": "טלויזיה דגם 05",
            "item_price": 5316.18        },
        {
            "item_amount": 1 ,
            "item_code": "6637471363",
            "item_description": "מדיח כלים דגם 08",
            "item_price": 1292.93        },
        {
            "item_amount": 1 ,
            "item_code": "7562781526",
            "item_description": "מדיח כלים דגם 03",
            "item_price": 2681.15        },
        {
            "item_amount": 1 ,
            "item_code": "6412781548",
            "item_description": "מדיח כלים דגם 09",
            "item_price": 2117.34        },
        {
            "item_amount": 1 ,
            "item_code": "2404899988",
            "item_description": "מדפסת דגם 01",
            "item_price": 407.27        },
        {
            "item_amount": 1 ,
            "item_code": "9102706897",
            "item_description": "מדפסת דגם 08",
            "item_price": 557.38        },
        {
            "item_amount": 1 ,
            "item_code": "6731655420",
            "item_description": "מדפסת דגם 04",
            "item_price": 541.93        },
        {
            "item_amount": 1 ,
            "item_code": "7073486520",
            "item_description": "מזגן דגם 05",
            "item_price": 6444.87        },
        {
            "item_amount": 1 ,
            "item_code": "4567309676",
            "item_description": "מזגן דגם 01",
            "item_price": 5216.67        },
        {
            "item_amount": 1 ,
            "item_code": "4139246491",
            "item_description": "מחשב נייד דגם 04",
            "item_price": 5628.39        },
        {
            "item_amount": 1 ,
            "item_code": "5097343767",
            "item_description": "מחשב נייד דגם 09",
            "item_price": 3228.10        },
        {
            "item_amount": 1 ,
            "item_code": "3925555269",
            "item_description": "מחשב נייד דגם 08",
            "item_price": 6497.22        },
        {
            "item_amount": 1 ,
            "item_code": "474160890",
            "item_description": "מחשב נייד דגם 07",
            "item_price": 3521.03        },
        {
            "item_amount": 1 ,
            "item_code": "4473311511",
            "item_description": "מחשב נייד דגם 04",
            "item_price": 4236.99        },
        {
            "item_amount": 1 ,
            "item_code": "8358488608",
            "item_description": "מכונת כביסה דגם 09",
            "item_price": 1980.90        },
        {
            "item_amount": 1 ,
            "item_code": "8347386870",
            "item_description": "מכונת כביסה דגם 08",
            "item_price": 3896.38        },
        {
            "item_amount": 1 ,
            "item_code": "4148723336",
            "item_description": "מכונת כביסה דגם 04",
            "item_price": 1637.16        },
        {
            "item_amount": 1 ,
            "item_code": "4732687425",
            "item_description": "מפזר חום",
            "item_price": 50.91        },
        {
            "item_amount": 1 ,
            "item_code": "4250632720",
            "item_description": "מקרר דגם 02",
            "item_price": 6773.08        },
        {
            "item_amount": 1 ,
            "item_code": "1191145769",
            "item_description": "מקרר דגם 04",
            "item_price": 7136.59        },
        {
            "item_amount": 1 ,
            "item_code": "2123054007",
            "item_description": "סט עכבר ומקלדת",
            "item_price": 104.36        },
        {
            "item_amount": 1 ,
            "item_code": "3439462437",
            "item_description": "סט עכבר ומקלדת",
            "item_price": 136.27        },
        {
            "item_amount": 1 ,
            "item_code": "7550892471",
            "item_description": "עכבר מחשב",
            "item_price": 64.30        },
        {
            "item_amount": 1 ,
            "item_code": "2584806631",
            "item_description": "פלאפון דגם 02",
            "item_price": 5082.56        },
        {
            "item_amount": 1 ,
            "item_code": "749886899",
            "item_description": "פלאפון דגם 01",
            "item_price": 1311.78        },
        {
            "item_amount": 1 ,
            "item_code": "8482862967",
            "item_description": "פלאפון דגם 06",
            "item_price": 1378.67        },
        {
            "item_amount": 1 ,
            "item_code": "4456997639",
            "item_description": "פלאפון דגם 03",
            "item_price": 1512.40        },
        {
            "item_amount": 1 ,
            "item_code": "1992881562",
            "item_description": "פלאפון דגם 04",
            "item_price": 1826.14        },
        {
            "item_amount": 1 ,
            "item_code": "8621232288",
            "item_description": "פלאפון דגם 05",
            "item_price": 5890.74        },
        {
            "item_amount": 1 ,
            "item_code": "9851383903",
            "item_description": "בושם Dior",
            "item_price": 238.19        },
        {
            "item_amount": 1 ,
            "item_code": "2598924651",
            "item_description": "בושם שאנל",
            "item_price": 287.43        },
        {
            "item_amount": 1 ,
            "item_code": "7875404409",
            "item_description": "בושם גו מלון",
            "item_price": 226.71        },
        {
            "item_amount": 1 ,
            "item_code": "1133167617",
            "item_description": "בושם Chloe",
            "item_price": 305.39        },
        {
            "item_amount": 1 ,
            "item_code": "6931946845",
            "item_description": "טיטולים הגיס",
            "item_price": 47.78        },
        {
            "item_amount": 1 ,
            "item_code": "2697254403",
            "item_description": "טיטולים",
            "item_price": 41.02        },
        {
            "item_amount": 1 ,
            "item_code": "4540058383",
            "item_description": "מברשת שיער אבינועם",
            "item_price": 12.77        },
        {
            "item_amount": 1 ,
            "item_code": "6899164040",
            "item_description": "מברשת שיער עילאי",
            "item_price": 19.96        },
        {
            "item_amount": 1 ,
            "item_code": "5125072964",
            "item_description": "מברשת שיער גדליה",
            "item_price": 27.13        },
        {
            "item_amount": 1 ,
            "item_code": "6698996649",
            "item_description": "מברשת שיער אורלי",
            "item_price": 26.12        },
        {
            "item_amount": 1 ,
            "item_code": "7116393964",
            "item_description": "משחת שיניים קולגייט",
            "item_price": 17.43        },
        {
            "item_amount": 1 ,
            "item_code": "6219890568",
            "item_description": "אורל-בי משחת שיניים",
            "item_price": 10.60        },
        {
            "item_amount": 1 ,
            "item_code": "1540001051",
            "item_description": "משחת שיניים קולגייט",
            "item_price": 20.23        },
        {
            "item_amount": 1 ,
            "item_code": "5623131257",
            "item_description": "אורל-בי משחת שיניים",
            "item_price": 14.35        },
        {
            "item_amount": 1 ,
            "item_code": "3674879184",
            "item_description": "סבון גוף הוואי",
            "item_price": 12.70        },
        {
            "item_amount": 1 ,
            "item_code": "6259290740",
            "item_description": "סבון גוף Dove",
            "item_price": 30.09        },
        {
            "item_amount": 1 ,
            "item_code": "8449123884",
            "item_description": "סבון גוף נקה 7",
            "item_price": 14.41        },
        {
            "item_amount": 1 ,
            "item_code": "7090205123",
            "item_description": "סבון גוף קרמה",
            "item_price": 15.01        },
        {
            "item_amount": 1 ,
            "item_code": "950650020",
            "item_description": "שמפו הוואי",
            "item_price": 39.16        },
        {
            "item_amount": 1 ,
            "item_code": "6372156577",
            "item_description": "שמפו פינוק",
            "item_price": 27.36        },
        {
            "item_amount": 1 ,
            "item_code": "5871375723",
            "item_description": "שמפו כיף",
            "item_price": 12.60        },
        {
            "item_amount": 1 ,
            "item_code": "6573858091",
            "item_description": "שמפו הד אנד שולדרס",
            "item_price": 24.69        },
        {
            "item_amount": 1 ,
            "item_code": "5678906677",
            "item_description": "מגבונים האגיס",
            "item_price": 18.90        },
        {
            "item_amount": 1 ,
            "item_code": "5575510278",
            "item_description": "בובה ניתאי",
            "item_price": 46.35        },
        {
            "item_amount": 1 ,
            "item_code": "165010991",
            "item_description": "בובה חננאל",
            "item_price": 69.10        },
        {
            "item_amount": 1 ,
            "item_code": "2466352536",
            "item_description": "בובה לין",
            "item_price": 75.78        },
        {
            "item_amount": 1 ,
            "item_code": "9745763153",
            "item_description": "בובה אוהד",
            "item_price": 70.05        },
        {
            "item_amount": 1 ,
            "item_code": "52892967",
            "item_description": "בובה שגב",
            "item_price": 45.96        },
        {
            "item_amount": 1 ,
            "item_code": "7110253306",
            "item_description": "בובה מטר",
            "item_price": 99.89        },
        {
            "item_amount": 1 ,
            "item_code": "7442696418",
            "item_description": "בובה עדי",
            "item_price": 51.05        },
        {
            "item_amount": 1 ,
            "item_code": "7381983604",
            "item_description": "בובה רימון",
            "item_price": 60.72        },
        {
            "item_amount": 1 ,
            "item_code": "294030830",
            "item_description": "טיטולים בגיס",
            "item_price": 55.36        },
        {
            "item_amount": 1 ,
            "item_code": "1977782703",
            "item_description": "טיטולים",
            "item_price": 55.24        },
        {
            "item_amount": 1 ,
            "item_code": "9738562007",
            "item_description": "כיסא תינוק שוהם",
            "item_price": 162.32        },
        {
            "item_amount": 1 ,
            "item_code": "6186865556",
            "item_description": "כיסא תינוק ליאם",
            "item_price": 140.21        },
        {
            "item_amount": 1 ,
            "item_code": "4359832529",
            "item_description": "כיסא תינוק הדס",
            "item_price": 134.14        },
        {
            "item_amount": 1 ,
            "item_code": "4662176329",
            "item_description": "מדפסת דגם 08",
            "item_price": 535.12        },
        {
            "item_amount": 1 ,
            "item_code": "599003115",
            "item_description": "מוצץ נתיב",
            "item_price": 34.35        },
        {
            "item_amount": 1 ,
            "item_code": "9750693807",
            "item_description": "מוצץ אמיליה",
            "item_price": 35.17        },
        {
            "item_amount": 1 ,
            "item_code": "3894610749",
            "item_description": "מוצץ ארד",
            "item_price": 44.38        },
        {
            "item_amount": 1 ,
            "item_code": "8384042105",
            "item_description": "מוצץ תהל",
            "item_price": 49.56        },
        {
            "item_amount": 1 ,
            "item_code": "8575958052",
            "item_description": "מוצץ שילת",
            "item_price": 40.79        },
        {
            "item_amount": 1 ,
            "item_code": "4745375052",
            "item_description": "מכונית צעצוע סתיו",
            "item_price": 44.83        },
        {
            "item_amount": 1 ,
            "item_code": "7374033791",
            "item_description": "מכונית צעצוע אביאור",
            "item_price": 72.35        },
        {
            "item_amount": 1 ,
            "item_code": "2695821964",
            "item_description": "מכונית צעצוע הענא",
            "item_price": 68.75        },
        {
            "item_amount": 1 ,
            "item_code": "8043184445",
            "item_description": "מכונית צעצוע חנה",
            "item_price": 51.92        },
        {
            "item_amount": 1 ,
            "item_code": "2676287789",
            "item_description": "מכונית צעצוע כפיר",
            "item_price": 55.07        },
        {
            "item_amount": 1 ,
            "item_code": "6783458426",
            "item_description": "מכונית צעצוע חוה",
            "item_price": 87.06        },
        {
            "item_amount": 1 ,
            "item_code": "8240031442",
            "item_description": "מכונית צעצוע ניב",
            "item_price": 89.44        },
        {
            "item_amount": 1 ,
            "item_code": "3893350447",
            "item_description": "מכונית צעצוע אדר",
            "item_price": 76.05        },
        {
            "item_amount": 1 ,
            "item_code": "8954162786",
            "item_description": "נעלי ילדים ישכר",
            "item_price": 105.75        },
        {
            "item_amount": 1 ,
            "item_code": "534969585",
            "item_description": "נעלי ילדים צורי",
            "item_price": 148.17        },
        {
            "item_amount": 1 ,
            "item_code": "6466276482",
            "item_description": "נעלי ילדים אבישי",
            "item_price": 122.68        },
        {
            "item_amount": 1 ,
            "item_code": "4104980290",
            "item_description": "נעלי ילדים רותם",
            "item_price": 142.60        },
        {
            "item_amount": 1 ,
            "item_code": "9380911099",
            "item_description": "נעלי ילדים מנור",
            "item_price": 143.18        },
        {
            "item_amount": 1 ,
            "item_code": "9062733338",
            "item_description": "נעלי ילדים בועז",
            "item_price": 93.15        },
        {
            "item_amount": 1 ,
            "item_code": "4422707685",
            "item_description": "נעלי ילדים לאון",
            "item_price": 119.15        },
        {
            "item_amount": 1 ,
            "item_code": "5844871041",
            "item_description": "עגלה תמיר",
            "item_price": 5198.33        },
        {
            "item_amount": 1 ,
            "item_code": "5250272096",
            "item_description": "עגלה מאור",
            "item_price": 3922.31        },
        {
            "item_amount": 1 ,
            "item_code": "6456600052",
            "item_description": "עגלה דגן",
            "item_price": 4230.40        },
        {
            "item_amount": 1 ,
            "item_code": "3404746005",
            "item_description": "עגלה הודיה",
            "item_price": 4617.16        },
        {
            "item_amount": 1 ,
            "item_code": "8702716923",
            "item_description": "עכבר מחשב",
            "item_price": 108.73        },
        {
            "item_amount": 1 ,
            "item_code": "8594746992",
            "item_description": "ארון אנה",
            "item_price": 1077.50        },
        {
            "item_amount": 1 ,
            "item_code": "823141430",
            "item_description": "ארון מעיין",
            "item_price": 2035.94        },
        {
            "item_amount": 1 ,
            "item_code": "2906974539",
            "item_description": "ארון בניה",
            "item_price": 1135.20        },
        {
            "item_amount": 1 ,
            "item_code": "1866459772",
            "item_description": "ארון שילה",
            "item_price": 2728.69        },
        {
            "item_amount": 1 ,
            "item_code": "4870095087",
            "item_description": "כורסה מאור",
            "item_price": 724.79        },
        {
            "item_amount": 1 ,
            "item_code": "2123147293",
            "item_description": "כורסה עטרה",
            "item_price": 609.29        },
        {
            "item_amount": 1 ,
            "item_code": "8617487502",
            "item_description": "כורסה יונתן",
            "item_price": 907.55        },
        {
            "item_amount": 1 ,
            "item_code": "9685977713",
            "item_description": "כורסה עמנואל",
            "item_price": 693.72        },
        {
            "item_amount": 1 ,
            "item_code": "3174509971",
            "item_description": "כיסא יגל",
            "item_price": 224.69        },
        {
            "item_amount": 1 ,
            "item_code": "8211645607",
            "item_description": "כיסא אליאב",
            "item_price": 195.47        },
        {
            "item_amount": 1 ,
            "item_code": "2453642410",
            "item_description": "כיסא אילעאי",
            "item_price": 233.62        },
        {
            "item_amount": 1 ,
            "item_code": "9357062621",
            "item_description": "כיסא אביתר",
            "item_price": 182.83        },
        {
            "item_amount": 1 ,
            "item_code": "8000168277",
            "item_description": "כיסא תלמיד רני",
            "item_price": 323.57        },
        {
            "item_amount": 1 ,
            "item_code": "7355680433",
            "item_description": "כיסא תלמיד רון",
            "item_price": 303.44        },
        {
            "item_amount": 1 ,
            "item_code": "1204142130",
            "item_description": "כיסא תלמיד שי",
            "item_price": 356.58        },
        {
            "item_amount": 1 ,
            "item_code": "4250438458",
            "item_description": "כיסא תלמיד יוני",
            "item_price": 361.97        },
        {
            "item_amount": 1 ,
            "item_code": "8944867270",
            "item_description": "מחבת פריידא",
            "item_price": 44.68        },
        {
            "item_amount": 1 ,
            "item_code": "2187919329",
            "item_description": "מחבת אלרואי",
            "item_price": 64.33        },
        {
            "item_amount": 1 ,
            "item_code": "9241225934",
            "item_description": "מחבת שביט",
            "item_price": 58.91        },
        {
            "item_amount": 1 ,
            "item_code": "4483999233",
            "item_description": "מחבת קארין",
            "item_price": 60.96        },
        {
            "item_amount": 1 ,
            "item_code": "857112390",
            "item_description": "מנורה מאי",
            "item_price": 84.82        },
        {
            "item_amount": 1 ,
            "item_code": "8099548214",
            "item_description": "מנורה עמנואל",
            "item_price": 46.46        },
        {
            "item_amount": 1 ,
            "item_code": "6962836135",
            "item_description": "מנורה אברהם",
            "item_price": 41.00        },
        {
            "item_amount": 1 ,
            "item_code": "5657301292",
            "item_description": "מנורה יעקב",
            "item_price": 79.89        },
        {
            "item_amount": 1 ,
            "item_code": "8653581163",
            "item_description": "מסמר פלדה",
            "item_price": 10.01        },
        {
            "item_amount": 1 ,
            "item_code": "4065544371",
            "item_description": "מסמר פלדה",
            "item_price": 15.63        },
        {
            "item_amount": 1 ,
            "item_code": "2967342521",
            "item_description": "מסמר פלדה",
            "item_price": 3.72        },
        {
            "item_amount": 1 ,
            "item_code": "8975405137",
            "item_description": "מסמר פלדה",
            "item_price": 6.23        },
        {
            "item_amount": 1 ,
            "item_code": "7493058252",
            "item_description": "מפזר חום",
            "item_price": 56.27        },
        {
            "item_amount": 1 ,
            "item_code": "1372176501",
            "item_description": "מפזר חום",
            "item_price": 54.43        },
        {
            "item_amount": 1 ,
            "item_code": "7131453694",
            "item_description": "מפזר חום",
            "item_price": 54.47        },
        {
            "item_amount": 1 ,
            "item_code": "5724902675",
            "item_description": "מפזר חום",
            "item_price": 50.72        },
        {
            "item_amount": 1 ,
            "item_code": "1492839841",
            "item_description": "סט כוסות אריאלה",
            "item_price": 47.88        },
        {
            "item_amount": 1 ,
            "item_code": "514945506",
            "item_description": "סט כוסות איה",
            "item_price": 68.55        },
        {
            "item_amount": 1 ,
            "item_code": "9664034374",
            "item_description": "סט כוסות נחמיה",
            "item_price": 89.54        },
        {
            "item_amount": 1 ,
            "item_code": "7513470481",
            "item_description": "סט כוסות דיאנה",
            "item_price": 67.49        },
        {
            "item_amount": 1 ,
            "item_code": "1300157479",
            "item_description": "סט צלחות שיראל",
            "item_price": 354.59        },
        {
            "item_amount": 1 ,
            "item_code": "1255249825",
            "item_description": "סט צלחות אסנת",
            "item_price": 548.19        },
        {
            "item_amount": 1 ,
            "item_code": "9417016929",
            "item_description": "סט צלחות יפתח",
            "item_price": 562.46        },
        {
            "item_amount": 1 ,
            "item_code": "3175903687",
            "item_description": "סט צלחות אמילי",
            "item_price": 359.91        },
        {
            "item_amount": 1 ,
            "item_code": "6207824933",
            "item_description": "סיר נון סטיק ליאל",
            "item_price": 147.28        },
        {
            "item_amount": 1 ,
            "item_code": "961037044",
            "item_description": "סיר נון סטיק הניה",
            "item_price": 115.72        },
        {
            "item_amount": 1 ,
            "item_code": "776873805",
            "item_description": "סיר נון סטיק תאיר",
            "item_price": 176.27        },
        {
            "item_amount": 1 ,
            "item_code": "4227012001",
            "item_description": "סיר נון סטיק אמרי",
            "item_price": 137.91        },
        {
            "item_amount": 1 ,
            "item_code": "2643397253",
            "item_description": "סלון 2+3 כרמל",
            "item_price": 3236.29        },
        {
            "item_amount": 1 ,
            "item_code": "4799186577",
            "item_description": "סלון 2+3 שפרה",
            "item_price": 3515.16        },
        {
            "item_amount": 1 ,
            "item_code": "974120598",
            "item_description": "סלון 2+3 עדי",
            "item_price": 5272.47        },
        {
            "item_amount": 1 ,
            "item_code": "6318688232",
            "item_description": "סלון 2+3 דניאל",
            "item_price": 4405.57        },
        {
            "item_amount": 1 ,
            "item_code": "4760495769",
            "item_description": "ריהוט גינה יפה",
            "item_price": 5420.00        },
        {
            "item_amount": 1 ,
            "item_code": "905520308",
            "item_description": "ריהוט גינה ניב",
            "item_price": 2541.65        },
        {
            "item_amount": 1 ,
            "item_code": "9474544123",
            "item_description": "ריהוט גינה יהושע",
            "item_price": 1534.97        },
        {
            "item_amount": 1 ,
            "item_code": "2169471862",
            "item_description": "ריהוט גינה הדס",
            "item_price": 1408.36        },
        {
            "item_amount": 1 ,
            "item_code": "1510203107",
            "item_description": "שולחן צופיה",
            "item_price": 362.77        },
        {
            "item_amount": 1 ,
            "item_code": "563238457",
            "item_description": "שולחן אביחי",
            "item_price": 525.36        },
        {
            "item_amount": 1 ,
            "item_code": "4780146518",
            "item_description": "שולחן שלום",
            "item_price": 418.73        },
        {
            "item_amount": 1 ,
            "item_code": "891522292",
            "item_description": "שולחן סופיה",
            "item_price": 348.74        },
        {
            "item_amount": 1 ,
            "item_code": "5015841160",
            "item_description": "שידה ידידיה",
            "item_price": 162.76        },
        {
            "item_amount": 1 ,
            "item_code": "3149948838",
            "item_description": "שידה דותן",
            "item_price": 194.62        },
        {
            "item_amount": 1 ,
            "item_code": "6966273721",
            "item_description": "שידה צופיה",
            "item_price": 196.74        },
        {
            "item_amount": 1 ,
            "item_code": "6113629946",
            "item_description": "שידה חן",
            "item_price": 176.03
        }
         
    ]
    """
    return json.loads(my_json_string)