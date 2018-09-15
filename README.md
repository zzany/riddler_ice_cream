# Preliminary Results
With current settings, the odds that the lowest-bucket strategy draws the most popular bucket is ~7%

#Instructions
Be sure to set parameters. Set size of ice cream bucket and size of scoop, and then the number of customers served before you (e.g. if you set NUM_CUSTOMERS_AHEAD to be 100, you are saying you appear as the 101st customer). Assumes every customer gets one scoop.

Assumes customers ahead draw flavors randomly from a power law / Zipf distribution, in which the most popular flavor is twice as popular / likely to be chosen than the second, three times as popular as the third, four times the fourth, etc.

#TODO
Implement different types of distributions. Test different numbers of buckets and customers. Currently defaults to 31 flavors since that's how many Baskin-Robbins has and they were a portfolio company
