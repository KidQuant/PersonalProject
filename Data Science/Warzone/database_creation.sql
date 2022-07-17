-- Active: 1657008265525@@localhost@3306@warzone

SELECT * FROM gamertags;

UPDATE metaphor SET Date = str_to_date(Date, "%m-%d-%Y");
UPDATE metaphor SET Time = time_format(Time, "%H:%i:%s");

SELECT * FROM quants
ORDER BY Date DESC, Time DESC;

CREATE TABLE qrissy(MatchID text,
					Mode text,
                    Kills int,
                    Deaths int,
                    KDRatio double,
                    LobbyKD double,
                    Date text,
                    Time text,
                    User text);
            