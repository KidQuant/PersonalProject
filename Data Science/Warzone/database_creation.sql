-- Active: 1657008265525@@localhost@3306@warzone

SELECT * FROM gamertags;

UPDATE metaphor SET Date = str_to_date(Date, "%m-%d-%Y");
UPDATE metaphor SET Time = time_format(Time, "%H:%i:%s");

SELECT * FROM swagg
Where Mode LIKE '%br_br%'
ORDER BY Date DESC, Time DESC;

CREATE TABLE Crowder(MatchID text,
					Mode text,
                    Kills int,
                    Deaths int,
                    KDRatio double,
                    LobbyKD double,
                    Date text,
                    Time text,
                    User text);

DELETE FROM gamertags
WHERE User = 'Davizzera';