import pandas as pd
from chatterbox import *

characters = ['old_man', 'old_woman', 'young_boy', 'young_girl', 'normal_voice']
reply_mood = ['stall', 'happy', 'angry', 'neutral', 'confused', 'comply', 'defiant']
response_df = pd.DataFrame(columns = characters, index = reply_mood)

