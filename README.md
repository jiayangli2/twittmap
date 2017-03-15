# twittmap
You can visit the twittmap application via
http://tmapenv.pyrwwgvxjf.us-west-2.elasticbeanstalk.com/tmap

Select a keyword, and you will see tweets that match the word appearing on the Google Map.
Each marker on the map represents a tweet.
If the tweet's geotag is available, then the position of the marker represents the geo location of the tweet.
Otherwise, the position corresponding to the tweet is generated randomly.
If you place the mouse on the marker, you can see the text of the tweet.

Bonus:
If you click on a point on the map, tweets that are within 300km of the point you click will appear as markers.
However, in order to not mislead users, only tweets that have the "geotag" will appear. If the location of a tweet is randomly generated, the tweet will be excluded in this search.
To differentiate, the icon of this kind of marker is different from the regular ones for regular search.

Back-end database:
We used Elasticsearch on AWS as our backend database. To stream tweets to elasticsearch, we used logstash and you can find the configuration file in the folder logstash-5.2.2.

Note: My groupmate went on vacation and I took charge of all the commit. Please consider equal grades.

Assignment Team Composition
HW Group 14

Name: Jiayang (Kingsley) Li
UNI: jl4305

Name: Guowei Xu
UNI: gx2127
