# *SEC Speed*: an Analysis

If you've watched college football over the past 10-ish years, you've likely heard the phrase "SEC Speed" come through your soundbar (most likely from Gary Danielson as Alabama is blowing some poor team's doors off). This topic [hasn't been covered](https://bleacherreport.com/articles/482339-debunking-the-myth-of-sec-speed-is-the-sec-really-faster-than-the-competition) for a while now, and given the Southeastern Conference's recent run of dominance in the sport, I thought it might be time to revisit. Is the SEC really another world when it comes to speed?

---
## Installation
In order to install this repo, you can git clone it to your local machine

    git clone https://github.com/andrewbowen19/secSpeed.git

To install required packages, use the included `requirements.txt` file:

    pip install -r requirements.txt
    
---

## Methods
We scraper each year's combine results dating back to the [2010 NFL Combine](https://www.pro-football-reference.com/draft/2010-combine.htm) from [Pro Football Reference](https://www.pro-football-reference.com), you can run `python combineScraper.py` from the `src` directory. This will produce a .csv file in the `data` directory containing all combine results dataing back to then. 

Then, we grouped each conference's results using [pandas.groupby](https://realpython.com/pandas-groupby/). This can be done using our `analysis.py` script. We grouped non-power 5 conferences together as there were too many schools and I didn't want to make the conference dictionary super long. 

---
## Results

Below are the average 40-yard times for eeach conference at the combine:

**40 yard dash average times by conference**
|Rank|Conference | Average 40-time   |
|----|-----------|-------------------|
| 1. |ACC        |    4.747          |
| 3. |Non Power-5|    4.763          |
| 2. |Big Ten    |    4.763          |
| 4. |Big 12     |    4.774          |
|**5.**|**SEC**  |    **4.784**      |
| 6. |Pac-12     |    4.785          |

Out of the 6 conference groupings, the SEC ranked 5th in terms of 40-yard dash times. You may be telling yourself, "Well certainly the SEC dominated in the 3-cone drill or shuttle run." Unfortunately you would be wrong. The SEC scored last and 4th in those categories, respectively.
___
## Conclusion
Next time you hear "SEC Speed", just know that it's an urban myth, like the yeti or bigfoot. While the SEC has been a dominant conference over the past decade, producing 6 national champions, just know the 'S' in *SEC* doesn't stand for "speed".

### Disclaimer
This is meant to be in jest. If you are an SEC fan, please know that I do admire the level of play in your conference. Mostly this is a way to keep my python fresh and learn some new tools. Go 'Cats!
