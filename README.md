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
We scraper each year's combine results dating back to the [2010 NFL Combine](https://www.pro-football-reference.com/draft/2010-combine.htm) from [Pro Football Reference](https://www.pro-football-reference.com), you can run `python combineScraper.py` from the `src` directory. This will produce a .csv file in the `data` directory containing all combine results dating back to then. 

Then, we grouped each conference's results using [pandas.groupby](https://realpython.com/pandas-groupby/). This can be done using our `analysis.py` script. We grouped non-power 5 conferences together as there were too many schools and I didn't want to make the conference dictionary super long. 

---
## Results

Below are the average 40-yard times for eeach conference at the combine:

**40 yard dash average times by conference -- All Players**
|Rank|Conference | Average 40-time   |
|----|-----------|-------------------|
| 1. |ACC        |    4.747          |
| 3. |Non Power-5|    4.763          |
| 2. |Big Ten    |    4.763          |
| 4. |Big 12     |    4.774          |
|**5.**|**SEC**  |    **4.784**      |
| 6. |Pac-12     |    4.785          |

Out of the 6 conference groupings, the SEC ranked 5th in terms of 40-yard dash times. You may be telling yourself, "Well certainly the SEC dominated in the 3-cone drill or shuttle run." Unfortunately you would be wrong. The SEC scored last and 4th in those categories, respectively across all combine players who participated. Pro-football-reference does not provide data for players who did not participate in certain events, so the world may never know.

### 40 yard dash average time for Skill Players
Another question you may be asking is: "What about skill players?" Well, what about them? [Skill players](https://en.wikipedia.org/wiki/Skill_position) are defined as players that consistently tote the rock. An additional argument in out `analysis.py` script in the `plot_avg_by_conf` function to filter out skill player's performance in different combine events. When only considering skill players, the SEC ranks *2nd* to the Big 12 in 40-yard dash times. In the other combine events for which there is data, the SEC ranks first in **none** of them.

**40 yard dash average times by conference -- All Players**
|Rank|Conference | Average 40-time   |
|----|-----------|-------------------|
| 1. |Big 12     |    4.575          |
| 3. |SEC        |    4.580          |
| 2. |ACC        |    4.594          |
| 4. |Big Ten    |    4.616          |
| 5. |Non Power-5|    4.617          |
| 6. |Pac-12     |    4.633          |

___
## Conclusion
Next time you hear "SEC Speed", just know that it's an urban myth, like the yeti or bigfoot. While the SEC has been a dominant conference over the past decade, producing 6 national champions, just know the 'S' in *SEC* doesn't stand for "speed".

### Disclaimer
This is meant to be in jest. If you are an SEC fan, don't get your undies in a bundle (or whatever you people say down south). Just know that I admire the level of play in your conference. Mostly this is a way to keep my python fresh and learn some new tools. Go 'Cats!
