Through Process
* Sort the meetings on start time.
* A map containing the start time of a meeting and the people that are meeting there.
* Use breadth first search
* Use ordered dictionary to avoid time travel.
* Use seen set to avoid infinity circle.
​
Steps to Follow
1. Create a meeting_dict
2. Add person1, person2 and time to meeting_dict
3. Set has_secret to time 0 and firstperson
4. Run a for loop on time and meeting in meeting_dict
5. Build an adjacency list of persons
6. set a seen set and add persons to it if in adjancy list
7. Start the bfs