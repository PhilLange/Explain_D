from functions import sub_id, randomlist, quiz_bio, quiz_psych
import pandas as pd

rands = randomlist()
bio = rands[0]
psych= rands[1]

ok_data = sub_id()
id = ok_data[0]
mzp = ok_data[1]

if id in bio:
    ok_datapsych = quiz_bio()
else:
    ok_datapsych = quiz_psych()


finaldata = pd.DataFrame({"id": [id],
                          "mzp": [mzp]
                          })


