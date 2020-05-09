Q1="select avg(age) from player;"

Q2="select match_no,play_date from match where audience > 50000 order by match_no asc;"

Q3="select team_id,count(win_lose)  as wl from matchteamdetails where win_lose=='W'  group by team_id order by wl desc ,team_id asc;"

Q4="select match_no,play_date from match where stop1_sec >(select avg(stop1_sec) from match) order by match_no desc;"

Q5="select matchcaptain. match_no,team.name,player.name from matchcaptain inner join team on team.team_id=matchcaptain.team_id inner join player on team.team_id=player.team_id where matchcaptain.captain=player.player_id order by matchcaptain.match_no asc,team.name asc; "

Q6="select match.match_no,player.name,player.jersey_no from player inner join match on player.player_id=match.player_of_match order by match.match_no asc;"

Q7="select team.name, avg(age) from player inner join team on player.team_id=team.team_id group by team.name having avg(age)>26 order by team.name ASc; "

Q8="select player.name,player.jersey_no,player.age,count(gd.player_id) as gs from player inner join goaldetails gd on player.player_id==gd.player_id where age <=27 group by gd.player_id order by gs desc,player.name asc;"

Q9="select goaldetails.team_id,count(goal_id)*100.0/(select count(goal_id) from goaldetails) as percentage  from goaldetails group by team_id;"

Q10="select avg(no_of_goals) as goals_avg from(select count(goal_id) as no_of_goals from goaldetails group by team_id);"

Q11="select p.player_id,p.name,p.date_of_birth from player p where not exists (select * from goaldetails  gd inner join player pl on pl.player_id=gd.player_id where gd.player_id=p.player_id) order by player_id asc;"

Q12="select t.name,m.match_no,audience,audience-(select avg(audience) from matchteamdetails mtd inner join match m on m.match_no=mtd.match_no where t.team_id=mtd.team_id group by mtd.team_id)  as audience  from team t inner join matchteamdetails mtd on t.team_id=mtd.team_id  inner join match m on m.match_no = mtd.match_no order by m.match_no asc;"
